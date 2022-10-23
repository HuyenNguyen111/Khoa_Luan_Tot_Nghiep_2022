from flask import Blueprint,  redirect, render_template, request

bp = Blueprint('process', __name__, url_prefix='/')


@bp.route("/")
def index():
    return redirect("/start")


@bp.route('/start', methods=('GET', 'POST'))
def start():
    if request.method == 'POST':
        mssv = request.form['mssv']
        hoTen = request.form['hoten']
        return redirect('/end')
    return render_template('start.j2')


@bp.route('/end', methods=('GET', 'POST'))
def end():
    if request.method == 'POST':
        pass
    return render_template('end.j2')
