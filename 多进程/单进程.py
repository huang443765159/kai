import multiprocessing
import time


def run_proc():
    """子进程要执行的代码"""
    while True:
        print("----2----")
        time.sleep(1)


if __name__ == '__main__':
    # 创建子进程
    sub_process = multiprocessing.Process(target=run_proc)
    # 启动子进程
    sub_process.start()
    while True:
        print("----1----")
        time.sleep(1)
