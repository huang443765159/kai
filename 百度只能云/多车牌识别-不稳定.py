from aip import AipOcr

app_id = '21547849'
api_key = 'ifde7dZv2BIrsFDVVx4VUEGU'
secret_key = 'XcUiYNHkXAig2srqrLSVaOPlFK5ubrVG'
client = AipOcr(appId=app_id, apiKey=api_key, secretKey=secret_key)
client.setConnectionTimeoutInMillis(5000)
client.setSocketTimeoutInMillis(5000)


def get_file_content(path):
    with open(path, 'rb') as fp:
        print(fp)
        return fp.read()


image = get_file_content('/Users/huangkai/Desktop/ScanCar/8.jpg')
options = dict()
options['multi_detect'] = 'true'
res = client.licensePlate(image, options)
for wr in res['words_result']:
    print(f"车牌号码：{wr['number']}")
    print(f"车牌颜色： {wr['color']}")
