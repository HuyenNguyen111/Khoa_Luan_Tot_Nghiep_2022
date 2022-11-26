from helper.detect import detect
from helper import session
from flask import Flask
from controller.handle import bp

app = Flask(__name__)
app.register_blueprint(bp)

# List = ["Recycling", "Nonrenewable"]
labels = ["Plastic_bottle", "Plactic_bottle_detergent", "Plastic_box", "Plastic_bottle_yogurt", "Can", "Foam_box", "Face_mask"]

@app.route('/count')
def count():
    c = detect(session)
    return str(c)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
