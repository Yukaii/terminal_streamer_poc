from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run')
def run():
    if request.method == 'POST':
        # TODO
        return 'getting form post'
    else:
        return index()

