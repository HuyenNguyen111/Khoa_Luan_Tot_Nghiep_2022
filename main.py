from helper.detect import detect
from helper import session
from flask import Flask
from controller.handle import bp

app = Flask(__name__)
app.register_blueprint(bp)


@app.route('/count')
def count():
    c = detect(session)
    return str(c)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
