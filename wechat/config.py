# -*- coding: utf-8 -*-
class WxConfig(object):
    # =======【基本信息设置】=====================================
    # 微信公众号身份的唯一标识。审核通过后，在微信发送的邮件中查看
    APPID = "wx76c5e240e2d14f8f"
    # JSAPI接口中获取openid，审核后在公众平台开启开发模式后可查看
    APPSECRET = "6da45e3dc697ce03e674985e6701e09c"
    # 接口配置token
    TOKEN = "shzk"
    # 受理商ID，身份标识
    MCHID = "18883487"
    # 商户支付密钥Key。审核通过后，在微信发送的邮件中查看
    KEY = "48888888888888888888888888888886"

    # =======【异步通知url设置】===================================
    # 异步通知url，商户根据实际开发过程设定
    NOTIFY_URL = "http://******.com/payback"

    # =======【证书路径设置】=====================================
    # 证书路径,注意应该填写绝对路径
    SSLCERT_PATH = "/******/cacert/apiclient_cert.pem"
    SSLKEY_PATH = "/******/cacert/apiclient_key.pem"

    # =======【curl超时设置】===================================
    CURL_TIMEOUT = 30

    # =======【HTTP客户端设置】===================================
    HTTP_CLIENT = "CURL"  # ( "CURL", "REQUESTS")


class Route:
    def __init__(self, url, func, method=["get", "post"]):
        self.url = url
        self.method = method
        self.func = func
