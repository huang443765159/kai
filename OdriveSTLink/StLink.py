import os
os.system('cd /Users/huangkai/Desktop')


os.system("""
openocd -f interface/stlink-v2.cfg -f target/stm32f4x.cfg -c init -c "reset halt" -c "flash write_image erase ODriveFirmware_v3.6-56V.elf" -c "reset run" -c exit

""")
