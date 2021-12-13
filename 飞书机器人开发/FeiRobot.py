"""
感谢刘硕提供帮助
1-进入飞书开发文档
2-自定义一个机器人
3-开通权限
4-更换图标
5-申请发行和审核
6-审核通过
7-建立群组-拉取机器人-完成
注意：机器人默认只能获取10条消息，可以改成50条，然后如果has_more里还有消息，会返回一个page_token,get_message的时候把这个token传进去即可
"""

import os
import re
import time
import json
import requests
from requests import request


def get_time_stamp(s_time: str, end_time: str) -> list:
    s_array = time.strptime(s_time, "%Y-%m-%d %H:%M:%S")
    e_array = time.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    s_stamp = time.mktime(s_array)
    e_stamp = time.mktime(e_array)
    return [s_stamp, e_stamp]


s_time = "2021-11-26 00:00:00"
e_time = "2021-11-27 00:00:00"


class FeiRobot:

    def __init__(self, app_id: str, app_secret: str):
        self._app_id = app_id
        self._app_secret = app_secret

    def get_access_token(self) -> str:
        url = 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal'
        r_json = {
            'app_id': self._app_id,
            'app_secret': self._app_secret,
        }
        req = request(method='POST', url=url, json=r_json)
        data = req.json()
        return f'Bearer {data["tenant_access_token"]}'

    def send_message(self):
        url = 'https://open.feishu.cn/open-apis/im/v1/messages'
        headers = {'Authorization': self.get_access_token()}
        r_json = {
            "receive_id": "oc_5add5dffc829badda9ce5e449b4478ed",
            "content": "{\"text\":\"hello \"}",
            "msg_type": "text"
        }
        params = {'receive_id_type': 'chat_id'}
        req = request(method='POST', url=url, headers=headers, json=r_json, params=params)
        print(req.text)

    def get_chat_list(self):
        url = 'https://open.feishu.cn/open-apis/im/v1/chats'
        headers = {'Authorization': self.get_access_token()}
        req = request(method='GET', url=url, headers=headers)
        return req.json()

    def get_messages(self, chat_id: str, page_token: str = ''):
        url = 'https://open.feishu.cn/open-apis/im/v1/messages'
        headers = {'Authorization': self.get_access_token()}
        t_stamp, e_stamp = get_time_stamp(s_time=s_time, end_time=e_time)
        params = {'container_id_type': 'chat', 'container_id': chat_id,
                  'start_time': int(t_stamp), 'end_time': int(e_stamp),
                  'page_size': 50}
        if page_token:
            params['page_token'] = page_token
        req = request(method='GET', url=url, headers=headers, params=params)
        return req.json()

    def get_resources(self, message_id: str, file_key: str):
        url = f'https://open.feishu.cn/open-apis/im/v1/messages/{message_id}/resources/{file_key}'
        params = {'type': 'image'}
        headers = {'Authorization': self.get_access_token()}
        req = request(method='GET', url=url, headers=headers, params=params)
        with open(f'1.jpg', 'wb') as f:
            f.write(req.content)
        f.close()
        return req.content

    def upload_file(self, file_path: str, file_type: str, duration: int = None):
        url = 'https://open.feishu.cn/open-apis/im/v1/files'
        headers = {'Authorization': self.get_access_token()}
        file_name = os.path.basename(file_path)
        r_json = {'file_type': file_type, 'file_name': file_name}
        if duration is not None:
            r_json['duration'] = duration
        with open(file_path, 'rb') as f:
            req = request(method='POST', url=url, headers=headers, files={'file': f}, data=r_json)
        return req.json()

    def send_file(self, receive_id_type: str, receive_id: str, content: dict, msg_type: str):
        url = 'https://open.feishu.cn/open-apis/im/v1/messages'
        params = {'receive_id_type': receive_id_type}
        r_json = {'receive_id': receive_id, 'content': json.dumps(content), 'msg_type': msg_type}
        print(r_json)
        headers = {'Authorization': self.get_access_token()}
        req = request(method='POST', url=url, headers=headers, params=params, json=r_json)
        return req.json()


if __name__ == '__main__':
    # test = FeiRobot(app_id='cli_a1144f3cf739900d', app_secret='Q53I4k7HBhp6e7DVQlPl2gJrqEBgpkt8')
    test = FeiRobot(app_id='cli_a111b1609139900b', app_secret='RHlKlYW4paxgt5RWa6sY9cWCGLYRAqmC')
    token = test.get_access_token()
    _chat_id = test.get_chat_list()['data']['items'][0]['chat_id']
    # test.send_message()
    # test.send_img()
    message = test.get_messages(chat_id=_chat_id)
    for one_message in message['data']['items']:
        if 'image_key' in one_message['body']['content']:
            _image_key = one_message['body']['content']
            _message_key = one_message['message_id']
            infos = re.split(r'[:{}''""]', _image_key)
            for info in infos:
                if info.startswith('img_v2') or info.startswith('file_v2'):
                    _key = info
                    print(_key, _message_key)
    infos = message['data']
    if infos['has_more']:
        page_token = infos['page_token']
        new_message = test.get_messages(chat_id=_chat_id, page_token=page_token)
        for one_message in new_message['data']['items']:
            if 'image_key' in one_message['body']['content']:
                _image_key = one_message['body']['content']
                _message_key = one_message['message_id']
                infos = re.split(r'[:{}''""]', _image_key)
                for info in infos:
                    if info.startswith('img_v2') or info.startswith('file_v2'):
                        _key = info
                        print(_key, _message_key)
    # for data in message['data']:
    #     print(message['data']['page_token'])
        # print(message['data']['items'])
        # print(message['data']['has_more'])
        # if data == 'has_more':
        #     page_token = message['sender']['page_token']
        #     print(page_token)

    # _data = test.get_resources(message_id='om_2eb2b23f3c2d712df94240f48f059753',
    #                            file_key="file_v2_c71bb5fc-3eba-4d98-8099-fb48618494bg")
