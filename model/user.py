class RegisterUser:
    def __init__(self, phone, code, wx_openid=None, ap_openid=None):
        self.phoneNumber = phone
        self.smsCode = code
        self.weiXinOpenId = wx_openid
        self.aliPayOpenId = ap_openid
