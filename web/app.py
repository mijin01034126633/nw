# -*- coding: utf8 -*-
from flask import Flask, render_template, request
import hashlib
 #from은 라이브러리의 함수 중 일부분만 가져올 때 (flask 중 Flask 함수만 가져옴.)
app = Flask(__name__) # Flask(__name)__:이 프로그램에서 app.py 자체를 의미.
users = {} # dictionary 할당

@app.route("/")  
def hello():
    return render_template("login.html")

@app.route("/name") # url = url + /name
def name():
    return "mijin"

@app.route("/login", methods=['POST'])
def login():
    id = request.form['id'] 
    pw = request.form['pw']
    if id in users:
        if users[id] == hashlib.sha1(pw).hexdigest():
            return "login ok"
        else:
            return "login fail!"
    else:
        return "login fail!"


@app.route("/join", methods=['GET', 'POST'])
def join():
    if request.method == 'POST': # 사용자로부터 POST 방식으로 요청을 받는다. 
        id = request.form['id'] 
        pw = request.form['pw']
        if id not in users: # users라는 dictionary 안에 없으면
            users[id] = hashlib.sha1(pw).hexdigest() # users dictionary에 저장한다. 
        else: 
            return "duplicate!!!" 
        return  "join ok"
    return render_template("join.html")

#@app.route("/")  
#def hello():
    #return render_template("join.html")

@app.route("/add")
@app.route("/add/<int:num1>")
@app.route("/add/<int:num1>/<int:num2>")
def add(num1=None, num2=None):
    if num1 is None or num2 is None:
        return "/add/num1/num2"
    return str(num1 + num2) #flask는 문자로 결과를 준다. 

@app.route("/sub/<int:num1>/<int:num2>")
def sub(num1, num2):
    return str(num1 - num2)

@app.route("/mul/<int:num1>/<int:num2>")
def mul(num1, num2):
    return str(num1 * num2)

@app.route("/div/<float:num1>/<float:num2>")
def div(num1, num2):
    if num2 != 0.0:
        return str(num1 / num2)
    else:
      return "error"