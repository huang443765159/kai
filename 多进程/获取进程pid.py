import multiprocessing
import time
import os


def work():
    # 查看当前进程
    current_process = multiprocessing.current_process()
    print("work:", current_process)
    # 获取当前进程的编号
    print("work进程编号:", current_process.pid, os.getpid())
    # 获取父进程的编号
    print("work父进程的编号:", os.getppid())
    for i in range(10):
        print("工作中....")
        time.sleep(0.2)
        # 扩展： 根据进程编号杀死对应的进程
        os.kill(os.getpid(), 9)


if __name__ == '__main__':

    # 查看当前进程
    current_process = multiprocessing.current_process()
    print("main:", current_process)
    # 获取当前进程的编号
    print("main进程的编号:", current_process.pid)

    # 创建子进程
    sub_process = multiprocessing.Process(target=work)
    # 启动进程
    sub_process.start()

    # 主进程执行打印信息操作
    for i in range(20):
        print("我在主进程中执行...")
        time.sleep(0.2)
