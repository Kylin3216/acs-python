# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template, make_response, redirect, session, request
from flask_cache import Cache
from config import Config
from weixin import Map
from wechat import msgRoute, payRoute, mpRoute, authRoute
from acs import acsAuth

Flask.secret_key = "acs"

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})


@app.route("/")
def index():
    token = session.get(Config.TOKEN_KEY)
    print(token)
    if not token:
        return redirect("/login")
    return render_template("index.html")


@app.route("/login", methods=["get", "post"])
def login():
    if request.method == "POST":
        name = request.form['name']
        code = request.form['code']
        data = acsAuth.get_token(name, code)
        token = Map(data)
        if token.get("access_token"):
            session[Config.TOKEN_KEY] = data
            return "ok"
        else:
            return "验证码错误"
    return render_template("login.html")


@app.route("/getSmsCode")
def sms_code():
    data = acsAuth.sms_code(request.args.get("telephone"))
    print(data)
    if data['status']:
        session[Config.TOKEN_KEY] = data['obj']
        return "ok"
    return data['message']


# 微信消息路由
for route in msgRoute:
    app.add_url_rule(rule=route.url, view_func=route.func, methods=route.method)

# 公众号路由
for route in mpRoute:
    app.add_url_rule(rule=route.url, view_func=route.func, methods=route.method)

# 微信支付路由
for route in payRoute:
    app.add_url_rule(rule=route.url, view_func=route.func, methods=route.method)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'404error': str(error)}), 404)


@app.errorhandler(500)
def server_error(error):
    return make_response(jsonify({'500error': str(error)}), 404)


app.run()
