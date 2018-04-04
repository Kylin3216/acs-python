# -*- coding: utf-8 -*-
from weixin.login import WeixinLogin
from .config import WxConfig

auth = WeixinLogin(WxConfig.APPID, WxConfig.APPSECRET)

authRoute = [

]
