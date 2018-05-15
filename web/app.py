# -*- coding: utf8 -*-
from flask import Flask, render_template, request, g, redirect, session, escape
import hashlib
import sqlite3
# g: 어디든 갈 때 사용
# redirect: 로그인에 성공한 사람이 또 한 번 로그인하려할 때 다시 로그인 할 필요없다고 돌려보냄.
# session: 로그인 유지, 서버가 사용자의 정보를 고유한 값으로 가지고 있다. 
# escape: 보안. 취약점 알아낼 때 일부러 넣은 코드인데 escape가 없으면 코드로 인식. 
# hashlib: 입력 값이 같으면 결과 값이 항상 같다. 

DATABASE = 'database.db'

app = Flask(__name__) # Flask 초기화
app.secret_key = '_fkfkfkfkfkfkfkfkfkfkfkfkfkfkf8989' # session을 생성할 때 데이터를 암호화. 암호화는 key가 있어야한다. 

def get_db(): 
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE) # sqlite에 database에 접근하는 method가 있다. 
    return db

@app.teardown_appcontext
def close_connection(exception): 
    db = getattr(g,'_database', None)
    if db is not None:
        db.close() # 연결을 끊어야 할 때는 끊어야한다. 

def query_db(query, args=(), one=False, modify=False): # 기본 query_db는 select만 처리. 
    cur = get_db().execute(query, args) # get_db(): database의 connection을 취함. 
    if modify:
        try:
            get_db().commit()
            cur.close()
        except:
            return False 
        return True
    rv = cur.fetchall() # data가 존재하면 fetch. 
    cur.close()
    return (rv[0] if rv else None) if one else rv   # 바깥 쪽 if문 부터 해석
 
@app.route('/logout')
def logout():
    session.pop('id', None)
    return redirect('/login') 

@app.route("/")  # /는 제일 처음 보이는 화면이며 index라고 부른다.
def hello():
    if 'id' in session:
        return u'로그인 완료 %s <a href="/logout">logout</a>' % escape(session['id'])
    return render_template("login.html")

@app.route("/name") # url = url + /name
def name():
    return "mijin"

@app.route("/login", methods=['GET', 'POST']) # GET은 사용자가 주소창에서 login을 요청했을 때
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
            return "<script>alert('login fail');history.back(-1);</script>" # history.back: '뒤로가기'와 같은 기능
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