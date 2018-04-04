# -*- coding: utf-8 -*-
from weixin import WeixinMsg

from .config import WxConfig, Route

msg = WeixinMsg(token=WxConfig.TOKEN)

# 验证token

msgRoute = [
    Route(url="/wx", func=msg.view_func)
]
