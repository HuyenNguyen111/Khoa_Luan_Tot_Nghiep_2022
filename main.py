from helper.detect import CameraThread
from helper import session
from flask import Flask
from controller.handle import bp
import os
try:
    os.remove('count/request.txt')
except:
    pass

try:
    os.remove('count/response.txt')
except:
    pass


app = Flask(__name__)
app.register_blueprint(bp)

# List = ["Recycling", "Nonrenewable"]


@app.route('/count')
def count():
    with open("count/request.txt", 'w') as f:
        f.write("request")
    while True:
        if os.path.exists('count/response.txt'):
            with open('count/response.txt') as f:
                num = f.read()    
            os.remove('count/response.txt')
            return num

if __name__ == '__main__':
    cam = CameraThread(session)
    cam.daemon = True
    cam.start()
    app.run(debug=True, host="0.0.0.0")
    cam.join()
