import threading


event = threading.Event()
event.set()  # 直接停止阻塞，执行wait内容，wait在等待超时时间内无set则不执行
if event.wait(2):  # 如果等待2s无set则什么也不发生
    print(1)
