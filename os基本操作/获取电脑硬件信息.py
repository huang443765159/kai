import os

output = os.popen("/usr/sbin/system_profiler SPHardwareDataType")
print(output.read())


# 只打印序列好
cmd = "/usr/sbin/system_profiler SPHardwareDataType | fgrep 'Serial' | awk '{print $NF}'"
output = os.popen(cmd)
print(output.read())
