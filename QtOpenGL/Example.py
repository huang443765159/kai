"""
MAC:
pip3 install PyopenGL PyOpenGL_accelerate

RASPBERRY:
EXTRA: sudo apt-get install python3-pyqt5.qtopengl

使用OPENGL添加背景色后会出现叠影，不可设置背景色
"""


from PyQt5.QtCore import Qt, QPointF, QTimer, QVariantAnimation
from PyQt5.QtWidgets import (
    QApplication,
    QGraphicsItem,
    QGraphicsView,
    QGraphicsScene,
    QGraphicsEllipseItem,
)
import sys, random
from PyQt5.QtOpenGL import QGL, QGLFormat, QGLWidget


class Circle(QGraphicsEllipseItem):
    def __init__(self, x, y, r):
        super().__init__(0, 0, r, r)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)
        self.setPos(x, y)
        self.setBrush(Qt.black)
        self.setRect(0, 0, r, r)

        self._animation = QVariantAnimation(duration=10000)
        self._animation.valueChanged.connect(self.setPos)
        self._animation.finished.connect(self.create_random_point)

    def create_random_point(self):
        pos = random.sample(range(0, 600), 2)
        self.move_to(*pos)

    def move_to(self, x, y):
        self._animation.setStartValue(self.pos())
        self._animation.setEndValue(QPointF(x, y))
        self._animation.start()
        self.update()

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionHasChanged:
            self.setBrush(Qt.blue if self.collidingItems() else Qt.red)
        return super().itemChange(change, value)


class GraphicView(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.setViewport(QGLWidget(QGLFormat(QGL.SampleBuffers)))
        scene = QGraphicsScene(self)
        self.setScene(scene)
        self.setSceneRect(0, 0, 600, 600)
        # self.setStyleSheet('background-color: rgba(255, 0, 0, 255)')

        for _ in range(10):
            pos = random.sample(range(0, 600), 2)
            circle = Circle(*pos, 100)
            circle.create_random_point()
            self.scene().addItem(circle)


app = QApplication(sys.argv)
view = GraphicView()
view.show()
sys.exit(app.exec_())
