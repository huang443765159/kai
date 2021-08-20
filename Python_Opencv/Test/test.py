from PIL import Image


rgb_list = Image.open('new_img.png')
# print(list(rgb_list.getdata()))
rgb_data = list(rgb_list.getdata())