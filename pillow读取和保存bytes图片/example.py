from io import StringIO, BytesIO

import numpy as np
from PIL import Image

import cv2

car_img_bytes = b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x02\x00v\x00v\x00\x00\xff\xef\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xdb\x00C\x00\x08\x06\x06\x07\x06\x05\x08\x07\x07\x07\t\t\x08\n\x0c\x14\r\x0c\x0b\x0b\x0c\x19\x12\x13\x0f\x14\x1d\x1a\x1f\x1e\x1d\x1a\x1c\x1c $.\' ",#\x1c\x1c(7),01444\x1f\'9=82<.342\xff\xdb\x00C\x01\t\t\t\x0c\x0b\x0c\x18\r\r\x182!\x1c!22222222222222222222222222222222222222222222222222\xff\xc0\x00\x11\x08\x00p\x01H\x03\x01"\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x00\x1f\x00\x00\x01\x05\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\xff\xc4\x00\xb5\x10\x00\x02\x01\x03\x03\x02\x04\x03\x05\x05\x04\x04\x00\x00\x01}\x01\x02\x03\x00\x04\x11\x05\x12!1A\x06\x13Qa\x07"q\x142\x81\x91\xa1\x08#B\xb1\xc1\x15R\xd1\xf0$3br\x82\t\n\x16\x17\x18\x19\x1a%&\'()*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz\x83\x84\x85\x86\x87\x88\x89\x8a\x92\x93\x94\x95\x96\x97\x98\x99\x9a\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xff\xc4\x00\x1f\x01\x00\x03\x01\x01\x01\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\xff\xc4\x00\xb5\x11\x00\x02\x01\x02\x04\x04\x03\x04\x07\x05\x04\x04\x00\x01\x02w\x00\x01\x02\x03\x11\x04\x05!1\x06\x12AQ\x07aq\x13"2\x81\x08\x14B\x91\xa1\xb1\xc1\t#3R\xf0\x15br\xd1\n\x16$4\xe1%\xf1\x17\x18\x19\x1a&\'()*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x92\x93\x94\x95\x96\x97\x98\x99\x9a\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xff\xda\x00\x0c\x03\x01\x00\x02\x11\x03\x11\x00?\x00\xea\x0e\x18\x1aX\xd7\x06\x9c\xaa\x0fnjA\x19\xc7\xb5}<]\x95\x8e;^C\xc2\x86QPO\x1b\x0e\x9c\xd4\xb9 \xe0S\x1d\x8fzj\xf7\x1b\xb5\xacA\x0f3\xe3\xae:\x8a\xd9\x821$*H\xe7\xbdc\xc63r\x19H\r\x83[\xd6\xdc.84\xab\xbd\x02\x94\x11\x9fy\x0e\x10\x8c\xf1\x8e3X\xf6p\x04\xbc\x93\x807\xb6\xe5\xe3\xd8WGv\xa0\xf4\xac\x98\x93\x178\xda0I\xc9\x14\xa8\xce\xe8\x89\xc5s\\\xb2c9\xc8=j\x85\xca\x80\xc3#\x9e\xa2\xb5p0}+.\xe9p\xc0\xee\xcbc\x9a\xd2\x9b\xd6\xc2\xab\xa2\xd0\xac2*\xdd\xb2\x16\x19\xc1\xc5V\x03\x8e\x95\xa5j\x07\x94\x0f c\xa5oQ\xd9\x1c\xf4\xd73$\x8dp}\xaab\x068\xa8\x8b\x84\\\x9e\x94\xdbk\xa8\xa6\x93`e\xdc;f\xb9$\xaf\xa9\xd7\x14\x92\xd4Y#\x05y\xaai\x1b\t\x8eP`\x1e9\xfdkVD\xc8\xaa\xfe^\x1b4\xe3;\x03\x82c\xe3\x84/N\x94\xf3\x1e\x07J\x947N\x95\x1c\xb3*\x8e\xb5\x0eM\x8dE$F\xc9\xc7J\xa9sm\xbd~S\x8e\xf5\xa0\x83zn\x1c\x8a\x8d\xc5Td\xc5(\xa6\x8c\xc0J\x90\xa4\xf3\xefVcS\x8aE\x8b7!\x88\xe3\x07\x8cw\xab\x89\x18Q\xedZ9\xa35L\x80\xa7\x14\xc7\x88\xed\xab\xfe_\x1e\xf5\x1b\x02\xb5\x9f9N\r#\x12P\xc9+\x8c\x923\xc6jkiw\x1d\xa6\xad\\F\n\xe7\x00\xfdj\xb4V\xac\xb2,\x83\xb7j\xd5\xb8\xca6fq\xe6\x8c\x8d\x05\x18\\\xfa\xd42\x83\xb4\x81\xde\xa5@H\x02\x9c\xd1\x9ct\xaeEM)\x1d\xcd\xfb\xa5\x05%O\xb5I\xbf8\xab!\x17\x18#\x9a\xab\xb4\xab\xf3]*\xcc\xe4\xa8\xdad\xcb\xce)\xe7\xa51N\x05X\x8f\x0c\x07\x1c\xd4\xca\xc5A\xb6D"\xefQ\xba\x90Eh\x08\xc6\xda\x86H\xc6x\xe9P\xa4\x8b\xb1P\x8ex\xa7\xa8\xe34\xae6\x91J8\x15\x8dd\x9a\xb9\xa56\xd8\xf5<\n}D\x0f\x14\xec\xd7\x935\xa9\xd2\xb6\x1c9\xa5\x18\x1d\xa9\x99\xe6\x97956\x18\xfc\n\xf9\x0e\xbe\xba\xcf\x15\xf2-D\xc9\x91\xf5b7z\xb0\x8d\x91T\xd5\xf1V#9\xe9\xd2\xbe\x8e\xda\x1c)\xdcBXK\xc8\xe2\x92C\x9e\x95.3U\xa4|3c\xb58\xbb\xbb\r\xec\x10\x03\xe7\x9c\x8f\x97\x8c\x11\xd6\xb6"8\xc0\xc61X\xf6Gu\xc3\x1d\xc4\x8fOJ\xd3\'h\xc8\xa9\xad\xd8\x9awH|\xed\xdcu\xf5\xaaK\x18\x078\xeajW\x7f0`\xff\x00:\x928\xf2+(\xfb\xabSm\x18\xd3\xf7MeNC\xcb\xd7\x8f\xe5\xedZ\xcc6\x83\xdb\x15\x91p\xc0\xb9<n$\xd7E\'vaY;h1\xc0\xc6OA\xda\xb4\xa0\\B\xa3`Q\x8e\xd5\x98\x8d\xc8\x07\x15\xab\x06\xef(n\x18\xf6\xadj\xecgN6dW$\x84>\x95\x9ff\x88\xf3\x12\x00\x0c0w\x01\xfdkF\xe4\x12\x87\x00\x11\xdc\x1e\xf5N\xd0l\x9b\x18\xc7\xb7j\x98?u\x84\xaf\xcc\xacm\'\xdc\x19\xf4\xa8\x88\xc3u\xa7tQ\x8a\x89\x88V\xac-\xa9\xd1f\xd17\xe3\xc5P\xbe\'*\xa0\xf5\xe4\xd5\xec\xf1Yw\xd2m\x90\x1ey8\xe3\x9c\x8cUA^D\xcfB\xd5\x83l\x1bO\x7fJ\xb8\xe0\x1a\xa7f\x1b \x81\xda\xae\x11\xc5\x13\xb5\xc7\x15\xa6\xa4*\x00\x92\xac\xa2\xf1T\xe2\x90}\xa3ks\xcfz\xb8\x0e*\x19h\xa7ut`\x9a00w\x10\x0f\xb78\xfe\xb5n`\n\x0e\x84\x8e\x86\xa2\x96\xdd%`X\x02\x01\xc8\xcdHSh\xe2\x96\x82*\xcf\x80\x83q\xc2\xe7\x14\xdbe\xc4C\'q\xf5\xa2\xf0\x83\x19\\\xf2\x08\xa7Y\xf3\x00\xf7\xad\x17\xc2E\xae\xcb\x08\x00\x05\xa8IRi\n\x0e\xa0t\xa5PB\x91\x9e\xb5Z+s\x1d\xd9\x90(\xdas\x93P\xcdR\'t\xc1\xe2\xaa\xce\xbb~j\xbc\xe75J\xe4\x86V_\xce\x9cY\x9dE\xa0\xc8\x99N\t\xabp\xe0\xbe\x05g\xa8\xec\xbcU\xdbu\'\r\x9e@\xfaV\x93DSl\xbd\xb4\x05\xc0\xa8$\\\n\x95w\x11\x9a\xabq)C\x8f\xeb\\\xe9;\x9b\xbd\x88_\x05\xb1\xe9N\x1d*=\xd99\xefN\xdd\xf2\xd1Y;\n\x0fP\xedJ)\x06M:\xbc\xa9\xadN\xa8\xea\x83\xa1\xa7f\x93\xad\x03\x83PP\xa0\xe2\xbeG\xaf\xae\x07Z\xf9\x1e\xb3\x992>\xa5U-\x1f\x1c\x123\xcd>\xd4\xb0f\xeb\xb4\x0f\x9b\xebQ\xa3|\xa0w\xc5L\xaf\x88\xf3\xef_J\xd5\x91\xc1k2UrK\x13\xf8UR\xc5\x9d\xb3\x9c\x9e\xd5:\xb0\xcesQ\x9d\xa1\x89\x02\xa6+P\x95\xda\x1fg\xc4\xb8\x03\x04\xf3\xf8V\x83\x9c)\xaav\xe7\xf7\x81\x87\x06\xad3\x0c\x12y\xc7j*j\xf5\x14J\xd0HK.O=\xebR\x14\xeb\x9e\xd5\xcf\xa4\xd8\xbfX\xc8\x00\x90\xcd\x9c\xfa\x11]\x05\xb4\x9b\x94\x13\xc1\xac\xaa\xc6\xca\xe6\x94\xa4\x99\x15\xc2\x80\t=k\x0eo\xf5\xa7\x8c\x0e\xd5\xbbv\x03\x0e:\xf75\x8b \xcc\x8c1\xd0\xf1Za\xd9\x95{\xf4 (\x08\xc6\x01\xcfcZ\xb0q\n\x82sY\xc5y\x04g\xa8\xce\x06x\xefZq(\xd9\xed[\xd5z\x13F\xddFL>C\x8e\xb8\xa8-c\x12\xbe9\x07\x00\x9a\xb6\xe9\x91\x81\xd6\x9fk\x1e\xc6\x07\x9ez\xd6\x1c\xf6Z\x1d\x1e\xce\xecy\\pj\x06\xfb\xfc\x1e\xf5re\x1b\xb3\x8e\xd5P\x91\xbf\x8a\x95+\x94\xd3C\x9b\x8e\xbdk:\xe8fj\xd2+\x9a\xcb\xbb\x01\xe6\x8d\x97\xb0#\xeb\x93Z\xc3s\x19\xa4\xf7.\xd8\x9c\x12\xab\xdb\xad\\~W\x15V\xd0azU\x969\x06\xa2\xa7\xc48\xecSQ\x89\xd7<\xe4\xf2@\xad\x05m\xdcUX\xd3\x0f\x9e\xd8\xa9\xfa\x0c\x8a\x86\xcbM\x8e#\x06\x946A\x06\xb3\xde\xec\x0b\xe1\tpwg\x00\xd5\xc9\x0f\xc9\x90y\xa5\xca>b\x95\xfe\xe0\x9f.9"\x96\xc5\xb2\xbbOQ\xc5,\xc3q\x04\x9e\x95$C\x0b\xd3\x9a\xd1?v\xc4\xa5fY\xd9\xdcS\x90v\xa6\xa3\xfc\xbc\xd1\x1c\xaa\xef\x85\xe7\x8c\xd6N\xe6\xb7\x1c\xc0\x11\xf4\xac\xdb\xac%\xc3(\xe0\xb0\r\xc7z\xbc\xef\xb4\xe3\xa6j\x9c\xe8w\x03\x8f\xa5]=\x19\x95]\x88c\x1c\x8a\xbf\t\xc75@\x82\x08>\x95<s\x10rkY+\x98\xd3\x91\xa2\x1f\x02\xaa\\F&9\xc7#\x8a\xb3\x0b,\xb1\xfb\xd4l\n\x93\x93\xcek\x9dh\xce\x96\xee\xb43\xc6Q\x8a\x93\xc8\xe3\x8ax<RN\x80\xc8\x0fqB\xd5\xd5\xd6\x17&\x9d\xef\xa90\x1cPE8\x0e)1\xcdx\xf3z\x9d\x91\xd83KI\x8fJZ\xcc`8\xaf\x91\xeb\xeb\x8c\xd7\xc8\xf5\x9dBd}:$\xc3T\x82L\xf0*\xbbw4\xd4f\x04\x11\xc8\xaf\xac\x8c.\x8f1\xb9_R\xebJQ:\x0c\xfdi\x04\xa1\xb2{z\x1a\x81\xc9e\x18\xa4\\\x81\xd2\x9f\xb3DNl\xb3\x14\xe4>3\xc5L\xf7[G^k-\x9c\xa1\xc8\xe9Q\xc9q\xe6FT\xe7\r\xd7\xe9C\xa4\x99\n\xa3\xb0\xe3p\x92^\xab\xe7#\xa0 t5\xd1\xd9J\xe6/\x98\x82{\xd7#j\xa6G\x95\x86C\x03\x8e?:\xe9,]\xbc\xb1\xbb\xef\x0e\rg^\x11\x8clk\x86m\x97&\x97\xe59\xac\xe7 \xbeGz\x9a\xec\x86^\x0f \xd5\x04\x94\x9e\xa3\x93\xd6\xb3\xa3\x1e\xa8\xd2\xab,\xa8\x00\x83Wa;\x94\xd5\x00\xc0~5,R\xf9g\xb9\x04\xe6\xb4\x92l\xc6\x12\xb3\xb1wv\xd3\xcd\\\x8f\x04\x0f_Z\xa0\x1c8\xc8\xe9R\xc7.\xdf\x94\x1e+\x96ql\xec\x84\xcbS\x1e\xbd\xcdg#a\xcf\xa6x\xc5>y\xc8\xce9\xf6\xaai+\x199=;\np\x83\x14\xa4i\x01\xbb\x9c\xd5Y`\xcbdT\xc8\xf9\xe8sC6O5Z\xa2ZLX\x14\xacj\x0fP9\xa7\x920}j%\x93\x04\x83L\x96L\'\x07\x9aZ\xb0\xd1"X\x88f>\x9e\xb58\xf4\xac\xfbW(H\xc9\xe7\xaf5kw~\xd4J-\x04Z(\xcbg\x9b\xc4\x94\x9c\x85\x06\xaf\x03\x88\xc5\x1dz\xd2\xf6\xa3\x99\xf5\x1a\x8d\xb5d\x12\x9c\x01RB\xd9\x8b\'\xaeqP\xdc\xc8\xbf.*H[+\xd2\x9fK\x872\xbe\x84\xf2 h\xba\x81\xc5g\xd9$\xc9p\xdb\xdb<\xe5rs\x8fZ\xbe\xa4\x15!\xbaSV \xac\x1b\xa9\xc7Z\x94\xec\x1a\x92I\x869\x15\x04\xdc\xf1\x8a\x9c\x0c\xf2j\xbc\xad\x96=(@\xd5\xd1\tBz\nk\x02\x83\x90q\x9cf\xac\x95*\x01\x14\xf6@\xeb\x8a\xbeb9P\xb6a\xb99\xca\x9e\x9c\xd5\x87\\\xd4P/\x94\xbb@\xc0\xa9X\xf1YKWr\xe2g\xdc\x8cHzb\x98\x86\x8b\x87\xdd3{\x9e\x06{RE\xf7\xa8\xa9~CJn\xefR\xd0\xe8(\xc6)\xc0Q^<\xb7:\x90\x98\xa4"\x9ei\xb8\xa8\x0b\r\xe6\xbeG\xaf\xae\xb1_"\xd4L\x99\x1fO\xf9X\xedB\xa1\xf4\xab\x04\x03M\xc0\xe3\x9a\xf6\xe1\x8c\xd2\xc74\xa9&\xc8\xfc\xae\xb4\x8c\x9cU\x80\x05\x04(\x15\xa7\xd7\x15\xc8\xf6\x08\xa0\xf1\x93\xd7\xa5W0\x1e\xb8\xad6\ni\xa1@>\x95\x7f\\V&XT\xca\x96\xd1\xed8\xda=kb\x00\x152\x08\xc6;U\x16\x87$2\xf0G \x83S$\x9bF3\xcdsV\xc4s\xa3j4\x94U\x85\xb8s\x9fj\xa8\x83,O\xafz\xb5 \x12\nj\xc5\x8a\xbaU\xd2B\xa9F\xefA6\x91R\x01\x9cf\x90\xaf\xbd8f\xba}\xb2h\xc7\xd8\xb1\xc3*84\xf0\xecE0\x0cu\xa7\x8fj\x87R#\xf6LL\x920j=\x85\\c\x91S\x01N\xc0<U*\x8b\xa0\x9d61d\xd9\xd2\x9f\xe6\xfa\x8aM\x80\x9av\xc1\xde\x8ex\x93i"=\xf9\xe7\xb55\xb2}\xc5J\x10\x0e\x83\x14\xe1\x18\xfaQ\xcd\x115&V*\xd8\xc8\xe0\x83\xda\xac\xa4\xa7 \x1a_,R4|\x82)\xb9E\x84`\xd1#0\xea*\'\x97\x00\x8a]\xa4\x0ej\'C\x8a\x95cF\xdd\x88\x1eB\xc7\x93V\xad\x9c\x86\x00\xd5S\x19\xdd\x8a\xb3\x12\x90\x07\xad\\\x9cTEN-\xbdK\xa5w\x0c\x8a\x85\xa6\x11\xb0S\xd7\x1cS\x84\x85GL\xd5[\x99\x0b\x10T\x0c\xff\x00J\xe7\x8b\xe6f\xf2\x8f)a\xe5\xc2\xd5w9!\xc1\xe6\xa2\xde[\x8ap\xce1\xda\xb7P\xb1\xcd9\xca\xe5\xd8\xa4Y\x13\xdf\xde\x9d\xca\x1a\xa0\x18\xa1\xe0U\x84\x97 \x7fZ\x99@p\x9d\xf7-\x87\x14\x8e\xe0\x03Qo\x00S\x0bq\xf5\xac\xf9M\\\x92\xd8\xab \xfd\xfb\x1cv\xeb\x9a\x9a1L\xc6\\\xd4\xe8\xb8\xfaR\xac\xed\x1b\x15M\x93\x01\xc0\xa7b\x9c\xa3\x81K\x8a\xf1\xa5\xb9\xd7\x1d\x86\x11HV\xa5"\x9b\xb6\xa4\x08\x88\xaf\x91+\xeb\xf6Q_ TT\xe8L\x8f\xa3\xbf\xb6\x13\x00\x96\x07\xb0\xc1\xc1\xf5\xa7\xae\xac\x84\x8c6\x0f\xd7\xbdyB\xf8\xa6T\xc8\xda\xfc\xf5 \xf0\x7fJ\xb1\x17\x8aB\x80\x0e\xe2\xa7\x86\xc3t\x1e\xa2\xba=\x8c\x89g\xa8\xae\xa6\xab\xd5\xbaz\x9ejE\xbfI\x18\xfe\xf1Kw\xe7\x1c{W\x97/\x8aTg\xccvP>\xe9\xc8\xe9\xef\xe9S\x0f\x13\xc6\x10\xb3\xbb\x01\xfe\xc9\x04\xd1\xc9 =)o\xe29\xf9\xc6>\xb4\x1b\xe4\xcf^\xbd\xeb\xce\x13\xc5(q\x8b\x86\xe9\xc3\x14\xc1\xfa{\xd4\x89\xe2A\xb8\xa9\x95[>\xdd?\xc2\x8eY\x81\xe8\xd1\xde!8\xdc\x009\xc74\xf1:\x9c\x90x\xef^{\x1f\x89\x14\x1coQ\xe8OZ\xb2\x9e"\r\xf3\x07\x03\x1dNs\x93\xebI\xc6CL\xef\x16`W\xe59\xfcy\xa7\x1b\x95\xc0\xc3s\\R\xeb\xe0\x8d\xcd!\xe0\xf2\xc0\xd4\xdf\xdbJ\xc7\x05\x98)\xef\xebS\xcd!\x9dp\xb8\x07\xa1\xce)\xe2pq\\\x82k\xe1\x98|\xf8#\xa3\x0e\x01\xa9\xbf\xb6\xc1]\xc5\x86z\x1fJ\xbfi$\x07T&\xcfzr\xce\xa0\xf5\xe6\xb9\x8f\xed\x94\x00\x10\xeb\xf5\x07\x15"kHA\xc1\x1b\x87Pq\xfdi\xaa\xb2\x0b#\xa7\x13)\xefN\x12\xaf\xadsk\xab\x02\xd8=\x0f`9\x15*\xea\x8ax\x07\x1f\xef\x1a\xa5ZHVGD%_Zr\xc8\x08<\xd7>5D\xe0\x8czu\xa9\x06\xa0\x9d\xf8=\x86{\xff\x00J~\xdaB\xe4F\xe8u\xf5\xa7n^\x95\x88\x97\xe0\xf49>\x95,w\xe1\x80\xc3\x0e\x99\xe4\xe0\xd1\xed\xd8\xb9Q\xb2\x08#\x8aAY\xab|:\xee\xa7\xad\xe0=\xff\x00Z\xa8\xe2\x18\xb9\x0b\xf4\x84f\xaa\x0b\xb3\xdc\xae;\x1e\xf4\xf1t\xa4u\xab\xfa\xc0\xbd\x98\xe9\x13\r\x91RD\xe0\x1ag\x9e\xa4b\xa2.\x01\xe0\xd4\xbcCj\xccj\t\x17\x1f\x07\xe9U\x8a\x93J\x93z\xf4\xa9U\x95\xbb\xf1N\x9e#\x94\xa7\x04\xc8\xd60;sF\xccT\xe0\x0c\xe3#\xf3\xa6\xb6\x07\xa5uG\x14\x99\x8b\xa2\x88\xf6\x83\x8aP\x00\xedN\xc0\xf5\xa5\xdb\xc5_\xd6\x11\x1e\xc4`\xc9\xa1\xb3\xda\x9c\x074\x15\xc9\xa7\xed\xa2\x1e\xcd\x8cU\xc1\xa9\xd0qL\njd\xaez\xd5nm\x08X\x98\x1c\x01N\xa8\xf3K\xba\xbc\xe7\xb9\xb8\xee\xf4g\x9anh\xcf\x15!pj\xf8\xfe\xbe\xbe<\xd7\xc85\x13\xe8L\x8d\xcd\xa0\x8a\nv\xf5\xa4\x12/\xad;x5^\xd2D\x8d\x11\xfb\xd3|\xb1\x9f\xba?*\x93p\xa5$b\x9f\xb5\x90\x9b!e\xc9\xf9\xb9\xf4\xcd7i\x00\x81\xd0\xd4\xc7\xebI\xd2\x9a\xac\xc1\x11\x00G \x9c\xff\x00{<\xd2\x86u\xce\xd7e9\xcf\x07\xbd?\xa8\xa5\xc7\x15^\xdd\x85\xc1g\x95[v\xf1\x920N94\xf5\xbf\xbaL\xae\xed\xcb\xdb\xe6 \x8a`\x14m\x14{^\xe5\\\x9cj\xf7h0\xaf\x91\xdc3\x13\x9a\x91u\xcb\x94#\r\xecr21T\x8a\x8e\xf4\xd2\x82\x8fh\x85tj\xaf\x88g\r\x9c\xf4\xed\xb7 \xd4\xc9\xe2Y\x14\xfc\xe0\xb0#\x83\x8eG\xebX{)\nb\x9f\xb4\x88\\\xe8\xd3\xc4\xe0\x8cyl=\x99\xb3\x83\xf5\x152x\xa0\x12\x15\x81\xcfPA\xcf>\x95\xc9\x959\xfaR\x10M\x1c\xd1c;\x88\xfcQ\x08\xc6\xe7\xd8O\xf1g\xa1\xf4\xf6\xab1x\x95\x1c\x7f\xae\xf9\x87\x0cNO\x1f^\xf5\xe7\xd8\xc7AHY\xbdq\xf4\xa6\xb9\x18\\\xf4\xa4\xf1\x14g\x05\xa7O\xf6I`\x01\xfcj\xc0\xd7wa\x9a^G\xbf"\xbc\xb9\\\xe7$\x0c\xfa\xe2\x9e.%V\xdc%rq\x8eM\x1c\xb0\xee\x17=au\xc5U\r\x86v#\xa88\xe3\xd6\xa7Mt\x10>~\x0f\\W\x92-\xf4\xeaI\x12\x1c\xe7 \xfa\x1a\x995k\xc5\xff\x00\x96\xb8o\xef\x02sG\xb3]\xc7\xa1\xeb\x89\xac\x83\xfca\x805:j\xfd\xbc\xc5a\xd8\xa1\xcek\xc8\x93^\xbcL\r\xc3=r8\xcf\xb6*t\xf1\x1c\xf9%\x94!\x1f\xdc\xe3?\xe1G\xb3b\xb9\xeb\x91\xeb\x0b\x80X\x9c\x1fB*\xc2\xea\xc0\x1c\x11\xc7\xea+\xc8\xe2\xf1<\x83\xac{\x81\xeb\xbf\x8f\xc0\xf5\xab1x\xa8\x06\xf9\x8c\x88{`\xff\x00Z=\x9b\x19\xeb+\xaaFG\x07\xdf\xdf\xf2\xa9SU\x85\xc0\xdb!\xf7\x0c\xb8\xaf,\x8f\xc5\x91\x10Y\xa5*G!\xb3\xcd\\\x8b\xc51K\x8f\xde\x9d\xde\xa0\x12?\x02*}\x9c\x80\xf4\xe4\xbfS\xfcCnq\x9fzx\xbfBp8\xfe\xb5\xe6\xd1\xf8\x92=\xdf4\xab\x8299\xab\x91x\x83x\xfd\xd9\x01s\xc6\xc6\xcf\xe9G,\x90\xcf@[\xc4=\x1b\xf0\xefR%\xc8a\xd4\x7f\xdfU\xc1\rr=\xf8\x05\xf3\xdf\x9c\xf3S\xc5\xad\xa0\x19\xf3\x07\x1d\xb0\x7f\x9d/y\x08\xee\x05\xc2\xff\x00z\xa4Y\x94\x9f\xbc>\xb5\xc6G\xae)a\x97S\xdb$\xf4\xfcj\xc0\xd7B\xf0\x1c\x06\xed\x93\x8f\xd6\x974\x80\xeb\x84\x99\xefOYW\xd6\xb9T\xd6N2H\xfc\x0e@\xab\x0b\xacF\xdf26\x0fpN3G4\x84t\x9e`\xf5\xa7\t\x01\xef\\\xf2\xea\xb1\x920\xd9\xcf\xf7\xb8\xc5X\x8fRR\xe3\x90G\xa6j\x1bc6\xb7\x0c\xd2\xee\xcde\xad\xf2\xfd\xe2N3\x83\xedS-\xd2\xb79\x1b}sO\x98e\xea\xf9\n\xbe\xb4[\x85\xf5\xcd|\x97Q6K?\xff\xd9'


def test():
    # 读取图片bytes
    with open('1.jpg', 'rb') as f:
        content = f.read()
        print(content)  # BYTES
    # 把bytes存储成照片
    img = Image.open(BytesIO(content))
    bytes_io = BytesIO()
    img.save(bytes_io, format='JPEG')
    img_bytes = bytes_io.getvalue()
    with open('2.jpg', 'wb') as f:
        f.write(img_bytes)


def test1():
    # 把bytes存储成照片
    img2 = Image.open(BytesIO(car_img_bytes))
    img3 = cv2.cvtColor(np.asarray(img2), cv2.COLOR_RGB2BGR)
    cv2.imwrite('3.jpg', img3)


def test2():
    # TO_BYTES
    frame = cv2.imread('1.jpg')
    _, data = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 50])
    tx_data = data.tobytes()
    # TO_LIST
    rx_data = np.frombuffer(tx_data, np.uint8)
    img = cv2.imdecode(rx_data, 1)
    print(img)
    cv2.imwrite('4.jpg', img)


test2()
