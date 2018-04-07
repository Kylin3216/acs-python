import urllib.parse
import requests

from .config import AcsConfig


def sms_code(tel):
    req = requests.get(AcsConfig.SMS_CODE_URL, params={"telephone": tel})
    return req.json()


def register_user(user):
    req = requests.post(AcsConfig.REGISTER_URL, data=user)
    return req.json()


def get_token(telephone, code):
    data = {"client_id": "ktiot",
            "client_secret": "pte&dVdrt235$io",
            "grant_type": "password",
            "username": telephone,
            "password": code
            }
    body = urllib.parse.urlencode(data)
    headers = {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}
    req = requests.post(AcsConfig.ACS_TOKEN_URL, data=body, headers=headers)
    return req.json()


def refresh_token(token):
    data = {"client_id": "ktiot",
            "client_secret": "pte&dVdrt235$io",
            "grant_type": "refresh_token",
            "refresh_token": token
            }
    body = urllib.parse.urlencode(data)
    headers = {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}
    req = requests.post(AcsConfig.ACS_TOKEN_URL, data=body, headers=headers)
    return req.json()
