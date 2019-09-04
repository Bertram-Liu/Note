import json

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost:3306/ajax"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Users(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  uname = db.Column(db.String(30))
  upwd = db.Column(db.String(30))
  nickname = db.Column(db.String(30))
  email = db.Column(db.String(100))

  def to_dict(self):
    dic = {
      'id': self.id,
      'uname': self.uname,
      'upwd': self.upwd,
      'nickname': self.nickname,
      'email': self.email
    }

    return dic


db.create_all()


@app.route('/01-server')
def server01():
  return "这是准备动态加载的内容"


@app.route('/02-server')
def server02():
  # 获取参数
  uname = request.args.get('uname', '')
  users = Users.query.filter(Users.uname.like('%' + uname + '%')).all()
  list = []
  for u in users:
    list.append(u.to_dict())
  return json.dumps(list)


@app.route('/03-checkuname')
def checkuname():
  uname = request.args.get('uname')
  user = Users.query.filter_by(uname=uname).first()
  if user:
    dic = {
      'status': 0,
      'text': '用户名称已存在',
    }
  else:
    dic = {
      'status': 1,
      'text': '通过'
    }
  return json.dumps(dic)

@app.route('/03-reguser',methods=['POST'])
def reguser():
  uname = request.form['uname']
  upwd = request.form['upwd']
  nickname = request.form['nickname']
  email = request.form['email']

  user = Users()
  user.uname = uname
  user.upwd = upwd
  user.nickname = nickname
  user.email = email

  try:
    db.session.add(user)
    db.session.commit()
    dic = {
      'status':1,
      'text':'注册数据成功'
    }
  except Exception as ex:
    print(ex)
    dic = {
      'status':0,
      'text':'注册失败,请联系管理员'
    }
  return json.dumps(dic)



if __name__ == "__main__":
  app.run(debug=True)
