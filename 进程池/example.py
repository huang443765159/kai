import multiprocessing


def test(num: int):
    print(num)


if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=5)
    for i in range(5):
        pool.apply_async(func=test, args=(i, ))
    pool.close()
    pool.join()

'不添加close/join的话 会直接退出程序，可以加阻塞代码阻塞一下'
