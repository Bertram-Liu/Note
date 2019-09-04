from flask import Flask, render_template, request
import datetime, os
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

app = Flask(__name__)

# 指定数据库的配置信息,连接到flaskDB的数据库上
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@127.0.0.1:3306/flaskDB"
# 指定信号追踪
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 创建SQLAlchemy的示例 - db , 用于做数据库的操作
db = SQLAlchemy(app)

# 创建Manager实例并指定要管理哪个app
manager = Manager(app)
# 创建Migrate对象,并指定要关联的app和db
migrate = Migrate(app,db)
# 为manager增加数据迁移的子命令
manager.add_command('db',MigrateCommand)



# 创建实体类 - Users,映射到数据库中叫users表
# 创建字段id,主键,自增
# 创建字段username,长度为80的字符串,不允许为空,值唯一,加索引
# 创建字段age,整数,允许为空
# 创建字段email,长度为120的字符串,值唯一
class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(
        db.Integer, primary_key=True
    )

    username = db.Column(
        db.String(80),  # 长度为80
        nullable=False,  # 不允许为空
        unique=True,  # 值唯一
        index=True,  # 增加索引
    )

    age = db.Column(
        db.Integer,
        nullable = True # 允许为空
    )

    email = db.Column(
        db.String(120),
        unique = True
    )

    #增加一个字段 isActive ,默认值为True
    isActive = db.Column(db.Boolean,default=True)

# 创建Student实体类
class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer,primary_key=True)
    sname = db.Column(db.String(30),nullable=False)
    sage = db.Column(db.Integer,nullable=False)
    isActive = db.Column(db.Boolean,default=True)

# 创建Teacher实体类
class Teacher(db.Model):
    __tablename__ = "teacher"
    id = db.Column(db.Integer,primary_key=True)
    tname = db.Column(db.String(30),nullable=False)
    tage = db.Column(db.Integer,nullable=True)

# 创建Course实体类
class Course(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    cname = db.Column(db.String(30),nullable=False)

# db.drop_all()
# 作用:删除所有的表结构
# db.drop_all()


# db.create_all()
# 作用:将所有的实体类生成对应的数据表
# 前提:对应的表不存在的前提下才能生成
# db.create_all()

def generate_timestr():
    """
    根据当前的系统日期时间拼时间字符串
    :return: 年月日时分秒微妙 所组成的字符串
    """
    s = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
    return s


def getext(filename):
    """
    根据传递过来的文件名称,返回对应的文件扩展名
    :param filename: 传递进来的文件名称
    :return: 文件的扩展名
    """
    ext = filename.split('.')[-1]
    return ext


@app.route('/01-file', methods=['GET', 'POST'])
def file_views():
    if request.method == 'GET':
        return render_template('01-file.html')
    else:
        uname = request.form['uname']
        if request.files:
            f = request.files['uimg']
            # 直接使用源文件名进行上传
            # f.save('static/'+f.filename)

            # 使用时间作为文件名 : 时间.扩展名

            # 获取系统时间
            ftime = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
            # 获取文件扩展名
            ext = f.filename.split('.')[-1]
            # 将 ftime.ext拼接到一起
            filename = ftime + '.' + ext
            # 将文件保存在相对路径的static中
            # f.save('static/'+filename)

            # 通过当前文件的地址找到static的地址(绝对路径)
            basedir = os.path.dirname(__file__)
            # 拼完整的保存路径
            upload_path = os.path.join(basedir, 'static', filename)
            f.save(upload_path)
        return "数据处理成功"


@app.route('/02-release', methods=['GET', 'POST'])
def release():
    if request.method == 'GET':
        return render_template('02-release.html')
    else:
        title = request.form['title']
        type = request.form['type']
        content = request.form['content']
        print("标题:%s,类型:%s,内容:%s" % (title, type, content))

        if request.files:
            file = request.files['pic']
            ftime = generate_timestr()
            ext = getext(file.filename)
            filename = ftime + '.' + ext
            base_dir = os.path.dirname(__file__)
            upload_path = os.path.join(base_dir, 'static/upload', filename)
            file.save(upload_path)
            print("上传路径:" + upload_path)
        return "发表博客成功"


if __name__ == "__main__":
    # app.run(debug=True)
    manager.run()
