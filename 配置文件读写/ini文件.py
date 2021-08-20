from configparser import ConfigParser


pump_ini_path = 'Pump1.ini'
pump_ini = ConfigParser()
pump_ini.read(pump_ini_path)
# 读

print(pump_ini.sections())
print(pump_ini.get('ALKALI CHEM', 'lib'))
print(pump_ini.getfloat('ALKALI CHEM', 't_delay'))

# 写
pump_ini.set('HIGH WATER', 't_delay', '11')
with open(pump_ini_path, 'w') as file_obj:
    pump_ini.write(file_obj)
