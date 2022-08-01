import struct
import json

a = b'{"PlateResult":{"bright":0,"carBright":0,"carColor":255,"car_brand":{"brand":255,"type":255,"year":65535},"car_location":{"RECT":{"bottom":1086,"left":535,"right":1166,"top":879}},"colorType":1,"colorValue":0,"confidence":88,"direction":4,"enable_encrypt":0,"fake_plate":0,"featureCode":true,"license":"\xcb\xd5PC3K36","license_ext_type":0,"location":{"RECT":{"bottom":970,"left":771,"right":976,"top":902}},"plate_distance":0,"plate_true_width":0,"timeStamp":{"Timeval":{"sec":1658747570,"usec":488645}},"timeUsed":0,"triggerType":8,"trigger_time_end":0,"trigger_time_start":0,"type":1},"active_id":0,"clipImgSize":0,"cmd":"ivs_result","fullImgSize":157469,"id":112,"imageformat":"jpg","timeString":"2022-07-25 19:12:50"}'


b = json.loads(a.decode('gbk'))

print(b)
print(b['fullImgSize'])

