from flask import Blueprint,  redirect, render_template, request
from helper import detect, session
from multiprocessing import Process, Event
import json

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
            "mssv": request.form['mssv'],
            "hoTen": request.form['hoten']
        }
        with open('result.json', 'w') as f:
            json.dump(data, f)
        exec.start()
        return redirect('/end')
    return render_template('start.j2')


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
        print(data)
    return render_template('end.j2')
