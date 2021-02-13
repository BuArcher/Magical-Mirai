import requests
import websocket
import json


class Method:
    def __init__(self):
        self.baseUrl = 'http://localhost:8080'
        self.baseJson = {
            "authKey": "2581946944"
        }
        self.qqNumber = input('输入自己的qq号')
        self.qqNumber = int(self.qqNumber)

    def monitor(self):
        key = self.verify()
        url = 'ws://localhost:8080/message?sessionKey=' + key
        ws = websocket.create_connection(url=url)
        i = 1
        while i == 1:
            msg = ws.recv()
            msg = json.loads(msg)
            print(msg)
        return msg
