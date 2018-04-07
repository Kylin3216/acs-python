import requests
import urllib.parse

from .config import AcsConfig


def open_door(user_id, cabinet_id, client_type):
    data = {"userid": user_id,
            "cabinetid": cabinet_id,
            "clienttype": client_type
            }
    body = urllib.parse.urlencode(data)
    headers = {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}
    req = requests.post(AcsConfig.OPEN_CABINET_URL, data=body, headers=headers)
    return req.json()


def check_door_state(req_id):
    req = requests.get(AcsConfig.CABINET_STATUS_URL, params={"reqid": req_id})
    return req.json()


def get_order(req_id):
    req = requests.get(AcsConfig.REQUEST_URL, params={"reqid": req_id})
    return req.json()


def get_door_state(cabinet_id):
    req = requests.get(AcsConfig.OPEN_SIGNAL_URL, params={"cabinetid": cabinet_id})
    return req.json()
