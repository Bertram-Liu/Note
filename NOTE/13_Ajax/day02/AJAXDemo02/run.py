from flask import Flask, render_template, request
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost:3306/ajaxdb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['DEBUG'] = True

db = SQLAlchemy(app)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(30))
    upwd = db.Column(db.String(30))
    nickname = db.Column(db.String(30))
    email = db.Column(db.String(30))

    def to_dict(self):
        #将本类中的属性们封装到一个字典中并返回
        dic = {
            'id':self.id,
            'uname':self.uname,
            'upwd':self.upwd,
            'nickname':self.nickname,
            'email':self.email
        }
        return dic

@app.route('/01-get')
def ajax_get():
    return render_template("01-get.html")


@app.route('/01-server')
def server01():
    uname = request.args.get('uname')
    return "请求的参数为:" + uname


@app.route('/02-reg')
def reg_views():
    return render_template('02-reg.html')


@app.route('/02-server')
def server02():
    # 1.接收前端传递过来的uname的值
    uname = request.args['uname']
    # 2.取db中判断uname的值是否存在
    user = Users.query.filter_by(uname=uname).first()
    # 3.响应结果回去前端
    if user:
        return "用户名称已存在"
    else:
        return "通过"


@app.route('/03-post')
def post_views():
    return render_template("03-post.html")


@app.route('/03-server', methods=['POST'])
def server03():
    # 接收请求数据
    uname = request.form['uname']
    age = request.form['age']
    return "用户名:%s,年龄:%s" % (uname, age)


@app.route('/04-users')
def users_views():
    return render_template('04-users.html')


@app.route('/04-server')
def server04():
    users = Users.query.all()
    s = ""
    for u in users:
        s += "%s_%s_%s_%s_%s|" % (u.id, u.uname, u.upwd, u.nickname, u.email)
    s = s[0:-1]
    return s


@app.route('/05-json')
def json_views():
    return render_template('05-json.html')


@app.route('/05-server')
def server05():
    dic = {
        'name': "lvzemaria",
        'age': 30,
        'gender': 'male'
    }
    # 将dic转换为JSON格式的字符串
    return json.dumps(dic)


@app.route('/06-users')
def users06():
    return render_template('06-users.html')


@app.route('/06-server')
def server06():
    # 查询users表中所有的数据再转换成JSON字符串
    users = Users.query.all()
    list = []
    for u in users:
        list.append(u.to_dict())
    jsonStr = json.dumps(list)
    print(jsonStr)
    return jsonStr


if __name__ == "__main__":
    manager.run()
