import numpy as np


def get_py_list(length):
    py_list = list()
    for i in range(length):
        py_list.append(i)
    return py_list


def get_numpy_list(py_list):
    numpy_list = np.array(py_list)
    new_py_list = numpy_list.tolist()
    print('NPY LIST', numpy_list)
    print('PY LIST', new_py_list)
    return numpy_list


def save_numpy_list(numpy_list):
    np.save('NumpyList', numpy_list)
    #  先写，写完之后会生成npy文件在读


def load_numpy_list():
    numpy_list = np.load('NumpyList.npy')
    print(numpy_list)


if __name__ == '__main__':

    _py_list = get_py_list(10)
    __numpy_list = get_numpy_list(_py_list)
    save_numpy_list(__numpy_list)
    load_numpy_list()
