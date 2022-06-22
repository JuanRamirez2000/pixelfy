from flask import Flask
from flask_cors import  CORS

app = Flask(__name__)
CORS(app)

PASSWORD = ""
PUBLIC_IP_ADDRESS = ""
DBNAME = ""
PROJECT_ID = ""
INSTANCE_NAME = ""

@app.route('/home')
def get_current_time():
    return {'home': "HELLO WORLD!"}
