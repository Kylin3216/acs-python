# -*- coding: utf-8 -*-
from weixin import WeixinError
from weixin.pay import WeixinPay

from .config import WxConfig

pay = WeixinPay(WxConfig.APPID, WxConfig.MCHID, WxConfig.KEY, WxConfig.SSLKEY_PATH, WxConfig.SSLCERT_PATH)


def js_pay(openid, body, out_trade_no, fee, attach):
    try:
        raw = pay.jsapi(openid=openid, body=body, out_trade_no=out_trade_no, total_fee=fee, attach=attach)
        return raw
    except WeixinError as err:
        return str(err)


payRoute = [

]
