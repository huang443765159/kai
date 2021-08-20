with open('test.txt', "a") as fp:
    fp.write('hello')
    fp.close()


with open('test.txt', "r") as fp:
    data = fp.read()
    print(data)
    fp.close()
