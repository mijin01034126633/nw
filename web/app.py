# -*- coding: utf8 -*-
from flask import Flask, render_template, request, g, redirect, session, escape
import hashlib
import sqlite3

DATABASE = 'database.db'

app = Flask(__name__)
app.secret_key = '_fkfkfkfkfkfkfkfkfkfkfkfkfkfkf8989'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g,'_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False, modify=False):
    cur = get_db().execute(query, args)
    if modify:
        try:
            get_db().commit()
            cur.close()
        except:
            return False
        return True
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv   
 
@app.route('/logout')
def logout():
    session.pop('id', None)
    return redirect('/login')

@app.route("/")  
def hello():
    if 'id' in session:
        return u'로그인 완료 %s <a href="/logout">logout</a>' % escape(session['id'])
    return render_template("login.html")

@app.route("/name") # url = url + /name
def name():
    return "mijin"

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        id = request.form['id'].strip() 
        pw = hashlib.sha1(request.form["pw"].strip()).hexdigest()
        sql ="select * from user where id='%s' and password='%s'" % (id, pw)
        if query_db(sql, one=True):
            # 로그인이 성공한 경우 - session 사용
            session['id'] = id
            return redirect("/")
        else:
            # 로그인이 실패한 경우
            return "<script>alert('join fail');history.back(-1);</script>"

    if 'id' in session:
        return redirect("/")

    return render_template("login.html")


@app.route("/join", methods=['GET', 'POST'])
def join():
    if request.method == 'POST': # 사용자로부터 POST 방식으로 요청을 받는다. 
        id = request.form["id"].strip()
        pw = hashlib.sha1(request.form["pw"].strip()).hexdigest()

        sql = "select * from user where id='%s'" % id # 중복 ID 검사
        if query_db(sql, one=True):
            return "<script>alert('join fail');history.back(-1);</script>"
        
        sql = "insert into user(id, password) values('%s', '%s')" % (id, pw)
        query_db(sql, modify=True)
    
        return redirect("/login")

    if 'id' in session:
        return redirect("/")

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