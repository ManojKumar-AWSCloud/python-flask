from flask import Flask

app = Flask(__name__)
@app.route('/home')
def home():
    return "Welcome to the Home Page!"
#app.run(port=5008, debug=True)