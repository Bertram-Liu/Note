from flask import Flask, render_template, request, redirect
import datetime, os, math
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy import or_, func

app = Flask(__name__)

# 指定数据库的配置信息,连接到flaskDB的数据库上
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@127.0.0.1:3306/flaskDB"
# 指定信号追踪
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 指定启动模式为调试模式
app.config['DEBUG'] = True

# 指定增删改操作完成后自动提交
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

# 创建SQLAlchemy的示例 - db , 用于做数据库的操作
db = SQLAlchemy(app)

# 创建Manager实例并指定要管理哪个app
manager = Manager(app)
# 创建Migrate对象,并指定要关联的app和db
migrate = Migrate(app, db)
# 为manager增加数据迁移的子命令
manager.add_command('db', MigrateCommand)


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
        nullable=True  # 允许为空
    )

    email = db.Column(
        db.String(120),
        unique=True
    )

    # 增加一个字段 isActive ,默认值为True
    isActive = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return "<Users %r>" % self.username


# 创建Student实体类
class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    sname = db.Column(db.String(30), nullable=False)
    sage = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)


# 创建Teacher实体类
class Teacher(db.Model):
    __tablename__ = "teacher"
    id = db.Column(db.Integer, primary_key=True)
    tname = db.Column(db.String(30), nullable=False)
    tage = db.Column(db.Integer, nullable=True)
    # 增加一个属性,cid,引用自 course表的主键id
    cid = db.Column(
        db.Integer,
        db.ForeignKey('course.id')
    )


# 创建Course实体类
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(30), nullable=False)
    # 增加反向引用关系属性:针对 Teacher
    teachers = db.relationship(
        "Teacher",
        backref="course",
        lazy="dynamic"
    )


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


@app.route('/03-add')
def add_views():
    user = Users()
    user.username = '老魏'
    user.age = 30
    user.email = "laowei@163.com"

    db.session.add(user)
    # db.session.commit()
    return "增加数据成功"


@app.route('/04-register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('04-register.html')
    else:
        # 接收前端数据
        username = request.form['username']
        age = request.form['age']
        email = request.form['email']
        isActive = False
        if 'isActive' in request.form:
            isActive = True
        # 创建Users对象,并赋值
        user = Users()
        user.username = username
        user.email = email
        user.age = age
        user.isActive = isActive

        # 将Users对象保存回数据库
        db.session.add(user)
        return "增加数据成功"


@app.route('/05-query')
def query_views():
    # 1. 测试 db.session.query() 方法
    # query = db.session.query(Users)
    # print(query)
    # print("type:", type(query))

    # 2.查询 users 表中所有的数据
    # users = db.session.query(Users).all()
    # for user in users:
    #     # user 表示每一个 Users 类型的对象
    #     print("id:%s,姓名:%s,年龄:%s,邮箱:%s,激活:%s" % (user.id,user.username,user.age,user.email,user.isActive))

    # 3.查询 users 表中的第一条数据并打印输出
    user = db.session.query(Users).first()
    print("id:%s,姓名:%s,年龄:%s,邮箱:%s,激活:%s" % (user.id, user.username, user.age, user.email, user.isActive))
    # 4.查询 users 表中共有多少条数据
    count = db.session.query(Users).count()
    print("users表中共有%d条数据" % count)

    return "查询成功"


@app.route('/06-filter')
def filter_views():
    # 1. 测试filter方法的使用和返回值
    # 1. 查询Users实体中age大于30岁的users的信息
    # result = db.session.query(Users).filter(Users.age>30)
    # print(result)
    # print("type:",type(result))

    # 2.查询email中包含ao的users的信息
    # users = db.session.query(Users).filter(
    #     Users.email.like("%ao%")
    # ).all()
    # print(users)

    # 3.通过 filter_by 查询年龄=30的users的信息
    users = db.session.query(Users).filter_by(age=30).all()
    print(users)
    return "执行查询成功"


@app.route('/07-query', methods=['GET', 'POST'])
def query07_views():
    if request.method == 'GET':
        # 接收前端传递过来的kw参数值,如果没有则为''
        kw = request.args.get('kw', '')
        users = db.session.query(Users).filter(
            or_(
                Users.username.like('%' + kw + '%'),
                Users.email.like('%' + kw + '%')
            )
        ).all()
        return render_template('07-query.html', users=users, kw=kw)
        # else:
        #     kw = request.form['kw']
        #     users = db.session.query(Users).filter(
        #         or_(
        #             Users.username.like('%' + kw + '%'),
        #             Users.email.like('%' + kw + '%')
        #         )
        #     ).all()
        #     return render_template('07-query.html', users=users, kw=kw)


@app.route('/08-page')
def page_views():
    # 1.每页显示的记录数 - pageSize
    pageSize = 2
    # 2.当前想看的页数 - page
    # 接收前端传递过来的参数 - page ,如果没传递参数的则默认为1
    page = int(request.args.get('page', 1))

    # 查询第page页的数据
    # 跳过(page-1)*pageSize条数据,再获取前pageSize条
    # ost:通过page以及pageSize计算出来要跳过的记录数
    ost = (page - 1) * pageSize

    # 通过pageSize 和 ost 查询对应的数据
    users = db.session.query(Users).limit(pageSize).offset(ost).all()

    # 计算尾页页码
    # 通过 pageSize 和 总记录数 计算尾页页码
    totalCount = db.session.query(Users).count()
    lastPage = math.ceil(totalCount / pageSize)

    # 计算上一页页码
    # 如果page大于1的话,上一页则为page-1,否则上一页为1,将结果保存在 prevPage
    prevPage = 1
    if page > 1:
        prevPage = page - 1

    # 计算下一页页码
    # 如果page 小于 lastPage 的话,下一页则为page+1,否则下一页就是lastPage,将结果保存在nextPage
    nextPage = lastPage
    if page < lastPage:
        nextPage = page + 1

    return render_template('08-page.html', users=users, prevPage=prevPage, nextPage=nextPage, lastPage=lastPage)


@app.route('/09-orderby')
def orderby_views():
    users = db.session.query(Users).order_by(
        "age desc,id").filter(Users.age > 18).all()
    for u in users:
        print("ID:%s,姓名:%s,年龄:%s" % (u.id, u.username, u.age))

    return "查询成功"


@app.route('/10-aggregate')
def aggregate_views():
    # 查询users表中所有人的总年龄，平均年龄，最大年龄和最小年龄
    # result = db.session.query(
    #     func.sum(Users.age),
    #     func.avg(Users.age),
    #     func.max(Users.age),
    #     func.min(Users.age)
    # ).filter(Users.age>30).all()
    # print("总年龄:%d,平均年龄:%.2f,最大年龄:%d,最小年龄:%d" % result[0])


    # 查询按isActive分组,每组的人数
    # select isActive,count(id) from users group by isActive
    # result = db.session.query(
    #     Users.isActive,
    #     func.count(Users.id)
    # ).group_by('isActive').all()
    # print(result)


    # 查询出年龄大于"老魏"的年龄的users的信息

    users = db.session.query(
        Users
    ).filter(
        Users.age > db.session.query(
            Users.age
        ).filter_by(
            username='老魏'
        ).first()[0]).all()

    print(users)
    return "聚合查询成功"


@app.route('/11-update')
def update_views():
    user = Users.query.filter_by(id=2).first()
    user.username = "魏老师"
    user.isActive = False
    db.session.add(user)
    return "修改数据成功"


@app.route('/12-update', methods=['GET', 'POST'])
def update12_views():
    if request.method == 'GET':
        # 1.取id
        id = request.args['id']
        # 2.查对象
        user = Users.query.filter_by(id=id).first()
        # 3.渲染页面
        return render_template('12-update.html', user=user)
    else:
        # 1.接收数据
        # 2.接收数据 & 查询对象 & 修改数据
        id = request.form['id']
        user = Users.query.filter_by(id=id).first()
        user.username = request.form['username']
        user.age = request.form['age']
        user.email = request.form['email']
        user.isActive = False
        if 'isActive' in request.form:
            user.isActive = True
        # 3.保存回数据库
        db.session.add(user)
        return redirect('/07-query')


@app.route('/13-regtea')
def regtea():
    # 方案1:声明一个teacher对象并赋值,同时指定cid的值来关联对应的课程id
    # teacher = Teacher()
    # teacher.tname = "魏老师"
    # teacher.tage = 35
    # teacher.cid = 1
    # db.session.add(teacher)

    # 方案2:声明teacher并赋值,通过course属性来关联对应的Course信息
    # 通过 teacher.course 得到关联的course对像
    # teacher.course的类型是 Course
    # 查询出id=2的course的信息
    cour = Course.query.filter_by(id=2).first()
    tea = Teacher()
    tea.tname = "王老师"
    tea.tage = 33
    tea.course = cour
    # tea.cid = cour.id
    db.session.add(tea)
    return "增加老师成功！"


if __name__ == "__main__":
    # app.run(debug=True)
    manager.run()
