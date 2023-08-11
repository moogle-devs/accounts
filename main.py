from flask import Flask, render_template
from replit import db

app = Flask(__name__)

@app.route('/')
def index():
  return

app.run('0.0.0.0', port=81)
