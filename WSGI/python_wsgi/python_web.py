from flask import Flask,render_template
from flask import request
import json


app = Flask(__name__)

@app.route('/postInfo',methods=['GET', 'POST'])
def postInfo():
    """获取post请求的信息"""
    content = request.json            #获取请求中的body(json格式),得到字典
    print(content)
    print(content['user'])           #获取字典中的value
    name = request.args.get("name")   #获取url中的请求参数
    print(name)
    data = request.data               #获取请求body中的数据
    print(data)
    return "hello hello"


@app.route('/transfJson', methods=['GET', 'POST'])
def transfJson():
    """响应json信息"""
    d = {"name":"jerry","passwd":1234,"age":20}    #字典信息
    return json.dumps(d)     #只能以json的格式响应


@app.route('/transfMat', methods=['GET','POST'])
def signin_form():
    """响应一个列表"""
    li = [[1,2,3],[4,5,6],[7,8,9]]     #列表信息
    return json.dumps(li)             #只能以json的格式响应列表信息，不能响应array or matrix



@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'


if __name__ == '__main__':
    app.run(host='192.168.1.108')