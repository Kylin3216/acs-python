# -*- coding: utf-8 -*-
from flask import jsonify, request, json
from weixin.mp import WeixinMP
from .config import WxConfig, Route
import urllib.parse

mp = WeixinMP(WxConfig.APPID, WxConfig.APPSECRET)


# 获取token
def token(): return mp.access_token


# 获取js ticket
def ticket(): return mp.jsapi_ticket


# js签名
def get_wx_config():
    return mp.jsapi_sign(url=request.url)


mpRoute = [
    Route(url='/mp/token', method=['get'], func=token),
    Route(url='/mp/ticket', method=['get'], func=ticket),
]
