from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import json
import subprocess

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)

@socketio.on('run')
def handle_message(data):
    with subprocess.Popen(['python3', '-u', 'countdown.py', data["args"]], stdout=subprocess.PIPE, bufsize=1, universal_newlines=True) as process:
        for line in process.stdout:
            line = line.rstrip()
            socketio.emit('data', {'data': line })

