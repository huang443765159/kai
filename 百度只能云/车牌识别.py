"""
1。网页搜索百度只能云，然后文字识别，车牌识别，
2。点击应用列表-创建应用
3。完成后点击查看应用，得到app_id, api_key, secret_key三个值
4。安装sdk库
    pip3 install baidu-aip
5.测试使用--只能读取照片

"""
from aip import AipOcr

app_id = '21547849'
api_key = 'ifde7dZv2BIrsFDVVx4VUEGU'
secret_key = 'XcUiYNHkXAig2srqrLSVaOPlFK5ubrVG'
client = AipOcr(appId=app_id, apiKey=api_key, secretKey=secret_key)
client.setConnectionTimeoutInMillis(2000)
client.setSocketTimeoutInMillis(2000)


def get_file_content(path):
    with open(path, 'rb') as fp:
        return fp.read()


image = get_file_content('/Users/huangkai/Desktop/ScanCar/3.jpeg')
res = client.licensePlate(image)
print(f"车牌号码：{res['words_result']['number']}")
print(f"车牌颜色： {res['words_result']['color']}")
