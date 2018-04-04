# -*- coding: utf-8 -*-
from weixin.pay import WeixinPay

from .config import WxConfig

pay = WeixinPay(WxConfig.APPID, WxConfig.MCHID, WxConfig.KEY, WxConfig.SSLKEY_PATH, WxConfig.SSLCERT_PATH)

payRoute = [

]
