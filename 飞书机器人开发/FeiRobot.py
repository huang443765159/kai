"""
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
from requests_toolbelt import MultipartEncoder


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

    def send_message(self, chat_id: str, text: str):
        url = 'https://open.feishu.cn/open-apis/im/v1/messages'
        headers = {'Authorization': self.get_access_token()}
        r_json = {
            "receive_id": chat_id,  # 需要填写chat_id
            "content": text,
            "msg_type": "text"
        }
        params = {'receive_id_type': 'chat_id'}
        req = request(method='POST', url=url, headers=headers, json=r_json, params=params)
        return req.text

    def send_msg(self, msg: str, receive_id: str, receive_id_type: str = 'chat_id'):
        url = 'https://open.feishu.cn/open-apis/im/v1/messages'
        params = {
            'receive_id_type': receive_id_type
        }
        data = {
            'receive_id': receive_id,
            'content': json.dumps({
                'text': msg
            }),
            'msg_type': 'text',
        }
        res = request(url=url, method='POST', params=params, data=data)
        return res.json()

    def get_chat_list(self):
        url = 'https://open.feishu.cn/open-apis/im/v1/chats'
        headers = {'Authorization': self.get_access_token()}
        req = request(method='GET', url=url, headers=headers)
        return req.json()

    def get_messages(self, chat_id: str, page_token: str = ''):  # 获取飞书群聊信息
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
        headers = {'Authorization': self.get_access_token()}
        req = request(method='POST', url=url, headers=headers, params=params, json=r_json)
        return req.json()

    def upload_img(self, img_path: str):
        url = "https://open.feishu.cn/open-apis/im/v1/images"
        form = {'image_type': 'message',
                'image': (open(img_path, 'rb'))}
        multi_form = MultipartEncoder(form)
        headers = {'Authorization': self.get_access_token(),
                   'Content-type': multi_form.content_type}
        req = request(method="POST", url=url, headers=headers, data=multi_form)
        return req.json()

    def upload_img(self, img_bytes: bytes):
        url = "https://open.feishu.cn/open-apis/im/v1/images"
        form = {'image_type': 'message',
                'image': bytes}
        multi_form = MultipartEncoder(form)
        headers = {'Authorization': self.get_access_token(),
                   'Content-type': multi_form.content_type}
        req = request(method="POST", url=url, headers=headers, data=multi_form)
        return req.json()


if __name__ == '__main__':
    import io
    from PIL import Image
    # test = FeiRobot(app_id='cli_a111b1609139900b', app_secret='RHlKlYW4paxgt5RWa6sY9cWCGLYRAqmC')  # 公司机器人
    test = FeiRobot(app_id='cli_a1144f3cf739900d', app_secret='Q53I4k7HBhp6e7DVQlPl2gJrqEBgpkt8')  # 自己机器人
    token = test.get_access_token()
    _chat_id = test.get_chat_list()['data']['items'][0]['chat_id']
    # print(_chat_id)
    # test.send_message()
    # test.send_img()
    message = test.get_messages(chat_id=_chat_id)
    # print(message)
    text = test.send_message(chat_id=_chat_id, text="{\"text\":\"" +
                                                               " 清洗日期：" + str(1) +
                                                               "\\n 清洗数量：" + str(len([0])) +
                                                               "\\n 清洗时间：" + s_time +
                                                               f"--{e_time}" +
                                                               " \"}")
    # print(text)
    # test.send_message(chat_id=_chat_id, text="{\"text\":\""
    #                                          "车牌号： " + '<京A123456>' +
    #                                          " \"}")
    # SEND_IMAGE
    # image_key = test.upload_img(img_path='2.jpg')['data']['image_key']
    # data = test.send_file(receive_id_type='chat_id',
    #                       receive_id=_chat_id,
    #                       content={'image_key': image_key},
    #                       msg_type='image')
    # print(data['msg'])
    # file_key = \
    # test.upload_file(file_path='/Users/huangkai/Desktop/ABPCarDataBase/CarInfos/20220310-水单.xls', file_type='xls')[
    #     'data']['file_key']
    # # _data = test.get_resources(message_id=_chat_id,
    # #                            file_key=file_key)
    # test.send_file(receive_id_type='chat_id',
    #                receive_id=_chat_id,
    #                content={'file_key': file_key},
    #                msg_type='file')
    # test
    test.send_message(chat_id=_chat_id,
                      text="{\"text\":\"""" + '11231313123123123132' + " \"}")  # json.dumps('text')
    img_bytes = open('/Users/huangkai/Documents/CODES4/XYZMengXiuRobot/XYZMengXiuRobot/1.png', 'rb')
    image = Image.open(io.BytesIO(img_bytes.read()))
    img_bytes = io.BytesIO()
    image.save(img_bytes, format='PNG')
    img_info = test.upload_img(img_bytes=img_bytes.getvalue())
    print(22222, img_info)
    img_key = img_info['data']['image_key']
    result = test.send_file(receive_id_type='chat_id', receive_id=_chat_id,
                            content={'image_key': img_key}, msg_type='image')
