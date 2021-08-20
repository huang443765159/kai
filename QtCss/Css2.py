from PyQt5.QtWidgets import QPushButton, QWidget, QMainWindow


class Test(QMainWindow):

    def __init__(self):
        super(Test, self).__init__()

        self._widget = QWidget(self)
        self.resize(1000, 1000)
        self._widget.resize(200, 200)
        sheet = f"""
        QWidget 
        {{  
            color: white;
            background-color: rgba(0, 0, 0, 0.5);
            border: 1px rgb(255, 0, 0);
        }}
        """
        self._widget.setStyleSheet(sheet)
        # BTN
        self._btn = QPushButton(self._widget)
        self._btn.resize(100, 50)
        self._btn.setText('hello')
        self._btn.show()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    test = Test()
    test.show()
    sys.exit(app.exec_())
