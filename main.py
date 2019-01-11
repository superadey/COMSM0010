#!/usr/bin/env python
from flask import Flask, flash, redirect, render_template, request, url_for
from pprint import pprint as pp
from weather import query_api

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'home.html',
        data=[{'name':'Bristol'}, {'name':'London'}, {'name':'Cardiff'},
        {'name':'Birmingham'}, {'name':'Exeter'}, {'name':'Swansea'},
        {'name':'Surrey'}, {'name':'Brighton'}, {'name':'Reading'},
        {'name':'Swindon'}, {'name':'Chippenham'}])

@app.route("/result" , methods=['GET', 'POST'])
def result():
    data = []
    error = None
    select = request.form.get('comp_select')
    resp = query_api(select)
    pp(resp)
    if resp:
       data.append(resp)
    if len(data) != 2:
        error = 'Bad Response from Weather API'
    return render_template(
        'weather.html',
        data=data,
        error=error)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
