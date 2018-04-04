# -*- coding: utf-8 -*-
from flask import jsonify, request, json
from weixin.mp import WeixinMP
from .config import WxConfig, Route
mp = WeixinMP(WxConfig.APPID, WxConfig.APPSECRET)


# 获取token
def token(): return mp.access_token


# 获取js ticket
def ticket(): return mp.jsapi_ticket


# js签名
def js_sign():
    try:
        data = json.loads(request.get_data())
        url = json.dumps(data['url'])
        return jsonify(mp.jsapi_sign(url=url))
    except KeyError:
        return jsonify({"error": "参数不正确"})


mpRoute = [
    Route(url='/mp/token', method=['get'], func=token),
    Route(url='/mp/ticket', method=['get'], func=ticket),
    Route(url='/mp/js_sign', method=['post'], func=js_sign)
]
