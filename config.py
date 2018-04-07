import re


class Config:
    TOKEN_KEY = "_token"
    USER_KEY = "_user"


class ClientType:
    CLIENT = 0
    WEI_XIN = 1
    ALI_PAY = 2


def check_client(ua):
    wx = re.search("MicroMessenger", ua, re.I)
    ap = re.search("AlipayClient", ua, re.I)
    return ClientType.WEI_XIN
    # if wx:
    #     return ClientType.WEI_XIN
    # if ap:
    #     return ClientType.ALI_PAY
    # return ClientType.CLIENT
