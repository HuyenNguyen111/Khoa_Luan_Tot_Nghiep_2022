from flask import Blueprint,  redirect, render_template, request
from helper import detect, session
from multiprocessing import Process, Event
import json
import requests
from config import Config

bp = Blueprint('process', __name__, url_prefix='/')

event = Event()
exec = Process(target=detect, args=(event, session))


@bp.route("/")
def index():
    return redirect("/start")


@bp.route('/start', methods=('GET', 'POST'))
def start():
    global exec, event
    event.clear()

    if request.method == 'POST':
        print('------- start --------')
        data = {
            "studentID": request.form['mssv'],
            "name": request.form['hoten'],
            "department": request.form['department']
        }
        with open('result.json', 'w') as f:
            json.dump(data, f)
        exec.start()
        return redirect('/end')
    get_dpm = requests.get(url=Config.SERVER_URL+"/get-dpm/")
    return render_template('start.html', departments=get_dpm.json())


@bp.route('/end', methods=('GET', 'POST'))
def end():
    global exec, event
    if request.method == 'POST':
        print("------ end ----------")
        event.set()
        exec.join()
        exec = Process(target=detect, args=(event, ))
        with open('result.json', 'r') as f:
            data = json.load(f)
        data['note'] = request.form['note']
        requests.post(Config.SERVER_URL+'/post-data/', data=data)
    return render_template('end.html')
