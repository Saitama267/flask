from flask import Flask
import json
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/save")
def save():
    f = open('data.json', 'r+', encoding='utf-8')
    json_file = json.load(f)
    ln = len(json_file)
    t = datetime.now()
    dt = {
    "id":ln,
    "date_now":t,
    "name":"noname",
    "description":"no description"
    }
    json_file.append(dt)
    json_data = json.dumps(json_file, indent=4, ensure_ascii=False)
    f = open('data.json', 'w', encoding='utf-8')
    f.write(json_data)
    f.close()
    return json_data