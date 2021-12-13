import os
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QObject


class Test(QObject):

    def load_file(self, path):
        file_type_list = 'stl File (*.mp4 *.png *.jpeg);; All File (*.*)'
        files = QFileDialog.getOpenFileNames(caption='选择多文件',
                                             directory=path,
                                             filter=file_type_list,
                                             options=QFileDialog.DontUseNativeDialog)[0]

        # file = QFileDialog.getOpenFileName(caption='选取单文件',
        #                                    directory=path,
        #                                    filter = file_type_list,
        #                                    options=QFileDialog.DontUseNativeDialog)[0]

        # packet = QFileDialog.getExistingDirectory(caption='选取文件夹',
        #                                           directory=path,
        #                                           filter=file_type_list,
        #                                           options=QFileDialog.DontUseNativeDialog)[0]  # 起始路径


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    test = Test()
    test.load_file(path=os.getcwd())
    sys.exit(app.exec_())
