from flask import Flask, render_template, request
from replit import db

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.form == 'POST':
    username, password, email = [request.form[_] for _ in ('username', 'password', 'email')]
    # TODO: loginn to account
    return

  return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'POST':
    username, password, email = [request.form[_] for _ in ('username', 'password', 'email')]
    # TODO: create account
    return
    
  return render_template('register.html')

app.run('0.0.0.0', port=81)
