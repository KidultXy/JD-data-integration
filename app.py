from flask import Flask, render_template, request, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

# 实例化flask，获得app
app = Flask(__name__)
app.secret_key = ' key'

# 连接 database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'xy020206'
app.config['MYSQL_DB'] = 'jd'
# 初始化 MySQL
mysql = MySQL(app)

# ==========login&register===========
@app.route('/', methods=['GET', 'POST'])
def index():
    # msg存储事件响应信息，如果错误，则给出提示
    msg = ''
    # 检查"username"和"password" POST 请求是否存在 (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:

        username = request.form['username']
        password = request.form['password']
        # 如果帐户存在于我们数据库的表单表中
        # 使用MySQL检查表单是否存在
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user_info WHERE username = %s AND password = %s', (username, password))
        # 抓取记录
        account = cursor.fetchone()
        # 如果账户存在
        if account:
            # 创建session存储信息（以便后面路由使用）
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            # 成功登录，渲染主页
            msg = 'Logged in successfully!'
            return render_template('view.html')
        # 账户不存在
        else:
            # 输出信息提示，账户不存在/密码错误/用户名错误
            msg = 'Incorrect username/password!'
    return render_template('index.html', msg=msg)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    return index()

@app.route('/login/register', methods=['GET', 'POST'])
def register():
    # msg存储事件响应信息，如果错误，则给出提示
    msg = ''
    # 检查"username"和"password" POST 请求是否已经存在 (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
      # 使用MySQL检查表单是否存在
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user_info WHERE username = %s', (username,))
        account = cursor.fetchone()
        # 检测账户是否已经注册过，并检查注册信息是否符合要求（用户名是否仅包含字母和数字/邮箱是否符合X@X.X）
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # 账号不存在，且表单数据有效，插入新的账号到accounts表中
            cursor.execute('INSERT INTO user_info VALUES (NULL, %s, %s, %s)', (username, password, email,))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
            # 如果成功，返回登录界面登录
            return render_template('view.html', msg=msg)
    elif request.method == 'POST':
        # 表单为空，给出提示信息
        msg = 'Please fill out the form!'
    return render_template('register.html', msg=msg)

# ==========home&details===========
# 分发路由
@app.route('/view')
# 定义函数传入页面
# welcome主页
def view():
    return render_template("view.html")

# 全部商品&搜索
@app.route('/search', methods=['GET', 'POST'])
def search():
    # 通过表单抓取需要查询的内容
    content = request.form.get('search-content')
    datalist = []
    cur = mysql.connection.cursor()
    sql = "select * from products_basic_info "
    if content != None:
        sql+= "where title like \"%"
        sql+=content
        sql+="%\""
    print(sql)
    # 生成游标，查询跟content有关的数据
    cur.execute(sql)
    # 逐行遍历
    result = cur.fetchall()
    for item in result:
        datalist.append(item)
    cur.close()
    print(datalist)
    return render_template("search.html", basic_infos=datalist)

# 全部商品信息展示看板
@app.route('/result')
def result():
    # 产品销售地区分布
    distri_info = []
    cur = mysql.connection.cursor()
    sql = "SELECT distribution,count(product_id) AS total FROM `products_details_info` GROUP BY distribution ORDER BY total DESC;"
    cur.execute(sql)
    result = cur.fetchall()
    for item in result:
        distri_info.append(item)

    # 产品销售地区分布
    brand_info = []
    sql2 = "SELECT brand,count(product_id) AS total FROM `products_details_info` GROUP BY brand ORDER BY total DESC LIMIT 0,14;"
    cur.execute(sql2)
    result2 = cur.fetchall()
    for item2 in result2:
        brand_info.append(item2)
    print(brand_info)

    # 厚度信息
    thick_info = []
    sql3 = "SELECT thickness,count(product_id) AS total FROM `products_details_info` GROUP BY thickness ORDER BY thickness;"
    cur.execute(sql3)
    result3 = cur.fetchall()
    for item3 in result3:
        thick_info.append(item3)

    # 屏幕刷新频率信息
    rate_info = []
    sql4 = "SELECT refresh_rate,count(product_id) AS total FROM `products_details_info` GROUP BY refresh_rate ORDER BY refresh_rate;"
    cur.execute(sql4)
    result4 = cur.fetchall()
    for item4 in result4:
        rate_info.append(item4)

    # 内存信息
    memory_info = []
    sql5 = "SELECT memory,count(product_id) AS total FROM `products_details_info` GROUP BY memory ORDER BY memory;"
    cur.execute(sql5)
    result5 = cur.fetchall()
    for item5 in result5:
        memory_info.append(item5)

    # 显卡信息
    gracard_info = []
    sql6 = "SELECT graphics_card,count(product_id) AS total FROM `products_details_info` GROUP BY graphics_card ORDER BY total DESC LIMIT 1,10"
    cur.execute(sql6)
    result6 = cur.fetchall()
    for item6 in result6:
        gracard_info.append(item6)
    print(gracard_info)

    cur.close()

    return render_template("result.html", datalist=distri_info, brand_info=brand_info, thick_info=thick_info, rate_info=rate_info, memory_info=memory_info, gracard_info=gracard_info)

# 商品详细页面(product_id对应)
@app.route('/result/<product_id>')
def product_result(product_id):
    datalist = []
    details = []
    cur = mysql.connection.cursor()
    # 商品评论信息
    sql = "select * from products_comment_info where product_id="
    sql += product_id
    cur.execute(sql)
    result = cur.fetchall()
    for item in result:
        datalist.append(item)

    # 商品详细信息
    sql2 = "select * from products_details_info where product_id="
    sql2 += product_id
    # print(sql2)
    cur.execute(sql2)
    result2 = cur.fetchall()
    for item2 in result2:
        details.append(item2)
    # print(details)
    cur.close()
    return render_template("details.html", datalist=datalist, product_id=product_id, details=details)

# 分工信息
@app.route('/team')
def team():
    return render_template("team.html")

if __name__ == '__main__':
    app.run()
