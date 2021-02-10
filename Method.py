import requests


class Method:
    def __init__(self):
        self.baseUrl = 'http://localhost:8080'
        self.baseJson = {
            "authKey": "2581946944"
        }
        self.qqNumber = input('输入自己的qq号')
        self.qqNumber = int(self.qqNumber)