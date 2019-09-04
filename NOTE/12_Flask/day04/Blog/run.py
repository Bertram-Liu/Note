from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/list')
def list_views():
    return render_template("list.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        # 接收前端传递过来的参数
        username = request.form['username']
        password = request.form['password']
        return "登录名称:%s,登录密码:%s" % (username, password)


@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        url = request.form['url']
        msg = "用户名称:%s,用户密码:%s,电子邮箱:%s,个人主站:%s" % (username,password,email,url)
        return msg


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
