import json
import websocket
import asyncio
from collections import namedtuple


User = namedtuple('User', ['pk', 'name'])


class Skyroom:
    def __init__(self, uri, room_id, username, password, surname):
        self.uri = uri
        self.room_id = room_id
        self.username = username
        self.password = password
        self.surname = surname
        self.ws = None

    def __del__(self):
        if self.ws:
            self.ws.close()

    def connect(self):
        if self.ws is not None:
            return
        ws = websocket.create_connection(self.uri)
        ws.recv()
        self.uid = json.loads(ws.recv())[3]['id']
        ws.send(json.dumps([
            's',
            'user',
            'join',
            {
                'origin': self.uri.split('/')[2],
                'app_id': 155141,
                "room_id": self.room_id,
                "customer_id": "1",
                "username": self.username,
                "password": self.password,
                "nickname": self.surname,
                "platform":{
                    "version": "12.4.9",
                    "os": 0,
                    "browser": 0,
                }
            },
        ]))
        self.ws = ws
        self.data = json.loads(self.ws.recv())

    def users_list(self):
        self.connect()
        data = self.data
        sr_users = data[3]['room']['users']
        users = list()
        for pk, user in sr_users.items():
            users.append(User(pk=pk, name=user['nickname']))
        return users

    def promote(self, user_id):
        self.connect()
        data = [
            "s",
            "user",
            "update",
            {
                "id": user_id,
                "prop": "role",
                "value": 3,
            },
        ]
        # await self.ws.send('["rq","webrtc::1","wrtc-create-consumer-transport",{}]')
        # print(await self.ws.recv())
        self.ws.send(json.dumps(data))
        return self.ws.recv()
