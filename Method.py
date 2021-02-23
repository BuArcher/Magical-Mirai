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

        
class Application(Method):
    def sendFriendMessage(self, target):  # 发送消息给好友
        url = self.baseUrl + '/sendFriendMessage'
        key = Method.verify(self)
        data = {{
            "sessionKey": key,
            "target": target,
            "messageChain": [
                {"type": "Plain", "text": "hello\n"},
                {"type": "Plain", "text": "world"},
                {"type": "Image", "url": "https://i0.hdslb.com/bfs/album/67fc4e6b417d9c68ef98ba71d5e79505bbad97a1.png"}
            ]
        }}
        html = requests.post(url=url, json=data)
        msg = html.json()
        messageId = html.json()
        if msg == 'success':
            print("发送成功")
            return messageId
        else:
            print('发送失败')

    def sendGroupMessage(self, target):
        """

        :param target: 群号
        :return:
        """
        key = self.verify()
        url = self.baseUrl + '/sendGroupMessage'
        data = {
            "sessionKey": key,
            "target": target,
            "messageChain": [
                {"type": "Plain", "text": "hello\n"},
                {"type": "Plain", "text": "world"},
                {"type": "Image", "url": "https://i0.hdslb.com/bfs/album/67fc4e6b417d9c68ef98ba71d5e79505bbad97a1.png"}
            ]
        }
        html = requests.post(url=url, json=data)
        msg = html.json()
        if msg['msg'] == 'success':
            print("发送成功")
            return msg['messageId']
        else:
            print('发送失败')

