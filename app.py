# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template, redirect, make_response, session, request, g, url_for
from flask_cache import Cache
from config import Config, check_client, ClientType
from weixin import Map, WeixinLogin
from wechat import msgRoute, payRoute, mpRoute, get_wx_config, wxPay
from wechat.config import WxConfig
from acs import acsAuth, acsDoor
from model import OrderData
import random
from datetime import datetime

Flask.secret_key = "acs"

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
wx_login = WeixinLogin(WxConfig.APPID, WxConfig.APPSECRET)


def wx_authorized(func):
    def decorator(*args, **kwargs):
        if Config.OPENID not in session:
            return func(*args, **kwargs)
        callback = url_for("authorized", _external=True)
        url = wx_login.authorize(callback, "snsapi_base")
        return redirect(url)

    return decorator


def login_require(func):
    def decorator(*args, **kwargs):
        if Config.TOKEN_KEY not in session:
            # todo 需判断是否有效
            return func(*args, **kwargs)
        return redirect("/login")

    return decorator


# ********************页面路由********************
@app.before_request
def before_request():
    client = check_client(str(request.user_agent))
    g.client = client
    if client == ClientType.CLIENT:
        return render_template("error.html", client=client, type="200")


@app.route("/")
@wx_authorized
@login_require
def index():
    if g.client == ClientType.WEI_XIN:
        data = get_wx_config()
        return render_template("index.html", config=data, client=g.client)
    return render_template("index.html", client=g.client)


@app.route("/authorized")
def authorized():
    code = request.args.get("code")
    if not code:
        return "ERR_INVALID_CODE", 400
    data = wx_login.access_token(code)
    openid = data.openid
    session[Config.OPENID] = openid
    return redirect("/")


@app.route("/login", methods=["get", "post"])
def login():
    if request.method == "POST":
        name = request.form['telephone']
        code = request.form['code']
        data = acsAuth.get_token(name, code)
        token = Map(data)
        if token.get("access_token"):
            session[Config.TOKEN_KEY] = data
            return "ok"
        else:
            return "验证码错误！"
    return render_template("login.html", client=g.client)


@app.route("/door")
def door():
    return render_template("door.html", client=g.client, door="1")


@app.route("/order")
def order():
    paid = [
        OrderData(1, "1000", "测试商品1已支付", "测试商品1", datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")),
        OrderData(2, "400", "测试商品2已支付", "测试商品2", datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")),
        OrderData(3, "600", "测试商品3已支付", "测试商品3", datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")),
        OrderData(4, "800", "测试商品4已支付", "测试商品4", datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S"))
    ]
    unpaid = [
        OrderData(3, "1000", "测试商品未支付", "测试商品", datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S"), False)
    ]
    if g.client == ClientType.WEI_XIN:
        data = get_wx_config()
        return render_template("order.html", client=g.client, config=data, paid=paid, unpaid=unpaid)
    return render_template("order.html", client=g.client, paid=paid, unpaid=unpaid)


@app.route("/doQrCode")
def do_qr_code():
    result = request.args.get("qrCode")
    return redirect(url_for("door", result=result))


# ********************api路由********************

# api 发送验证码
@app.route("/getSmsCode/<telephone>")
def sms_code(telephone):
    data = acsAuth.sms_code(telephone)
    if data['status']:
        if data['obj']:
            session[Config.USER_KEY] = data['obj']
        return "ok"
    return data['message']


@app.route("/openDoor/<door_id>")
def open_door(door_id):
    # req = acsDoor.open_door(1, door_id, g.client)

    return "ok"


@app.route("/checkDoorState")
def check_door_state():
    r = random.random()
    print(r)
    if r < 0.5:
        return "false"
    return "ok"


@app.route("/doJsPay", methods=["post"])
def do_js_pay():
    order_id = request.form["orderId"]
    data = wxPay.js_pay(order_id)
    return data


# 微信消息路由
for route in msgRoute:
    app.add_url_rule(rule=route.url, view_func=route.func, methods=route.method)

# 公众号路由
for route in mpRoute:
    app.add_url_rule(rule=route.url, view_func=route.func, methods=route.method)

# 微信支付路由
for route in payRoute:
    app.add_url_rule(rule=route.url, view_func=route.func, methods=route.method)


# ********************错误处理********************

@app.errorhandler(404)
def not_found(error):
    client = check_client(str(request.user_agent))
    return render_template("error.html", client=client, type="404", error=str(error))


@app.errorhandler(500)
def server_error(error):
    client = check_client(str(request.user_agent))
    return render_template("error.html", client=client, type="500", error=str(error))


app.run()
