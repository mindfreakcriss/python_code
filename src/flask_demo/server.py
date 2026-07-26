# -*- coding: utf-8 -*-

import flask
import config

#static_folder 静态资源目录 默认为static
app = flask.Flask(__name__) #设置服务器
#引入配置文件
app.config.from_pyfile('config.py')

# get 方法
@app.route('/test', methods=['GET']) #设置路由
def test():
    return "hello world!"


# POST 方法，表单数据获取
@app.route('/method', methods=['POST'])
def test_method():
    username = flask.request.form['username']
    password = flask.request.form['password']
    return username + password

# JSON 接收和输出
@app.route('/json', methods=['POST'])
def test_json():
    username = flask.request.json['username']
    password = flask.request.json['password']
    result = {
        "username":username,
        "password":password
    }
    return flask.jsonify(result)

@app.route("/reload", methods=['GET'])
def test_reload():
    return "no need to reload"

@app.route("/config", methods=["GET"])
def test_config():
    result = {
        'project_name' : config.PROJECT_NAME
    }
    return flask.jsonify(result)

if __name__ == "__main__": 
    # gunicorn 代码修改
    #from werkzeug.contrib.fixers import ProxyFix
    #app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run() #设置访问端口，调试模式等

