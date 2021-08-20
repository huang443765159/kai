import subprocess


pkt_str = subprocess.run(['cd', '/Users', '/huangkai'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=None)
print(pkt_str.stdout.decode('utf-8'))
