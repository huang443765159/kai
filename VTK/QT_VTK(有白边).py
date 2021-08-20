from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import vtk


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.widget = QWidget()
        self.gl = QGridLayout()
        self.vtk_widget = QVTKRenderWindowInteractor(self.widget)
        self.gl.addWidget(self.vtk_widget)

        self.ren = vtk.vtkRenderer()
        self.vtk_widget.GetRenderWindow().AddRenderer(self.ren)
        self.i_ren = self.vtk_widget.GetRenderWindow().GetInteractor()

        self.widget.setLayout(self.gl)
        self.setCentralWidget(self.widget)

        sphere = vtk.vtkSphereSource()
        sphere.SetCenter(0, 0, 0)
        sphere.SetRadius(5.0)

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(sphere.GetOutputPort())

        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetColor(0, 0, 1)

        self.ren.AddActor(actor)
        self.ren.ResetCamera()

        self.show()
        self.i_ren.Initialize()
        self.i_ren.Start()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)

    win = MainWindow()

    sys.exit(app.exec_())
