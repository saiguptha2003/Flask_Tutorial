from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
data=[
('panduranga sai guptha','b','ap21110010091','pandurangasai guptha','fad'),
('panduranga sai guptha','b','ap21110010091','pandurangasai guptha','fad'),
('panduranga sai guptha','b','ap21110010091','pandurangasai guptha','fad'),
('panduranga sai guptha','b','ap21110010091','pandurangasai guptha'),
('panduranga sai guptha','b','ap21110010091','pandurangasai guptha'),
('panduranga sai guptha','b','ap21110010091','pandurangasai guptha'),
('panduranga sai guptha','b','ap21110010091','pandurangasai guptha'),
('panduranga sai guptha','b','ap21110010091','pandurangasai guptha'),
('panduranga sai guptha','b','ap21110010091','pandurangasai guptha'),
('panduranga sai guptha','b','ap21110010091','pandurangasai guptha'),
('panduranga sai guptha','b','ap21110010091','pandurangasai guptha'),
('panduranga sai guptha','b','ap21110010091','pandurangasai guptha'),
('panduranga sai guptha','b','ap21110010091','pandurangasai guptha'),
('panduranga sai guptha','b','ap21110010091','pandurangasai guptha'),
('panduranga sai guptha','b','ap21110010091','pandurangasai guptha'),
('panduranga sai guptha','b','ap21110010091','pandurangasai guptha'),
('panduranga sai guptha','b','ap21110010091','pandurangasai guptha'),
('panduranga sai guptha','b','ap21110010091','pandurangasai guptha'),

('panduranga sai guptha','b','ap21110010091','pandurangasai guptha'),
('panduranga sai guptha','b','ap21110010091','pandurangasai guptha'),
('panduranga sai guptha','b','ap21110010091','pandurangasai guptha'),
('panduranga sai guptha','b','ap21110010091','pandurangasai guptha'),
('panduranga sai guptha','b','ap21110010091','pandurangasai guptha'),
('panduranga sai guptha','b','ap21110010091','pandurangasai guptha'),
('panduranga sai guptha','b','ap21110010091','pandurangasai guptha'),
('panduranga sai guptha','b','ap21110010091','pandurangasai guptha'),
('panduranga sai guptha','b','ap21110010091','pandurangasai guptha'),
('panduranga sai guptha','b','ap21110010091','pandurangasai guptha'),
('panduranga sai guptha','b','ap21110010091','pandurangasai guptha'),
('panduranga sai guptha','b','ap21110010091','pandurangasai guptha'),
('panduranga sai guptha','b','ap21110010091','pandurangasai guptha'),
('panduranga sai guptha','b','ap21110010091','pandurangasai guptha'),
('panduranga sai guptha','b','ap21110010091','pandurangasai guptha'),
('panduranga sai guptha','b','ap21110010091','pandurangasai guptha'),
('panduranga sai guptha','b','ap21110010091','pandurangasai guptha'),
('panduranga sai guptha','b','ap21110010091','pandurangasai guptha'),
]

@app.route('/')
def index():
    return render_template('sid.html',entries=data)

@app.route('/order')
def order():
    return render_template('index.html')

def action():
    action1()

app.run(debug=True)
      
