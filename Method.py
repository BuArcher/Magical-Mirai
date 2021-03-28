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


class Getlist(Method):  # 获取列表
    def friendList(self):  # 好友列表
        midurl = self.baseUrl + '/friendList?'
        key = self.verify()
        data = 'sessionKey=' + key
        url = midurl + data
        midmsg = requests.get(url=url)
        p = midmsg.json()
        i = 0
        while i < len(p):
            json = p[i]
            print(json['nickname'])
            i += 1

    def groupList(self):
        midurl = self.baseUrl + '/groupList?'
        key = self.verify()
        data = 'sessionKey=' + key
        url = midurl + data
        midMsg = requests.get(url=url)
        p = midMsg.json()
        i = 0
        while i < len(p):
            json = p[i]
            print(json['name'])
            i += 1

    def memberList(self, target: int, state: None, printing: bool):
        """

        :param target: 群号
        :param state: 用途
        :param printing:妈的字符型是否打印
        :return: 处理完的json
        """
        target = str(target)
        state = str(state)
        printing = bool(printing)
        midUrl = self.baseUrl + '/memberList?'
        sessionKey = 'sessionKey=' + self.verify() + '&'
        urlTarget = 'target=' + target
        url = midUrl + sessionKey + urlTarget
        midMsg = requests.get(url=url)
        p = midMsg.json()
        if printing:
            i = 0
            while i < len(p):
                json = p[i]  # 转换成json处理
                try:
                    if state == 'id':
                        print(json['id'])
                    elif state == 'memberName':
                        print(json['memberName'])
                    elif state == 'permission':
                        print(json['permission'])
                    i += 1
                except:
                    print('导出失败')
        else:
            return p


class Judge(Getlist):
    def judge(self, target: int):
        target = int(target)
        table = Getlist.memberList(self=self, target=target, state='12', printing=False)  # 判断权限
        i = 0
        while i < len(table):
            msg = table[i]
            while msg['id'] == self.qqNumber:
                finalNum = i
                break
            i += 1
        material = table[finalNum]
        if material['permission'] != 'MEMBER':
            return True
        else:
            print('本账号权限不足')
            return False
