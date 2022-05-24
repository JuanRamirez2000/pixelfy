from flask import Flask
from flask_cors import  CORS

app = Flask(__name__)
CORS(app)

@app.route('/home')
def get_current_time():
    return {'home': "HELLO WORLD!"}
