from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@127.0.0.1:3306/blogDB"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command("db", MigrateCommand)


# 创建User实体类,映射到 user 表
# id , 整数,主键,自增
# username , 字符串(30),不允许为空,唯一
# password , 字符串(30),不允许为空
# email , 字符串(100) , 不允许为空,唯一
# url , 字符串(120) , 允许为空
class User(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(30),
        nullable=False,
        unique=True
    )

    password = db.Column(
        db.String(30),
        nullable=False
    )

    email = db.Column(
        db.String(100),
        nullable=False,
        unique=True
    )

    url = db.Column(
        db.String(200),
        nullable=True
    )

# 博客主题 - Topic ,映射到 topic 表
# id , title , blogType , images , content
class Topic(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(30),nullable=False)
    blogType = db.Column(db.Integer,nullable=False,default=1)
    images = db.Column(db.String(200),nullable=True)
    content = db.Column(db.Text,nullable=False)



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


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        url = request.form['url']
        msg = "用户名称:%s,用户密码:%s,电子邮箱:%s,个人主站:%s" % (username, password, email, url)
        return msg


if __name__ == "__main__":
    # app.run(debug=True, host="0.0.0.0", port=5000)
    manager.run()
