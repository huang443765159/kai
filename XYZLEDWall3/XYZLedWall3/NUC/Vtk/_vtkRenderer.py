from vtkmodules import all


class VtkRenderer(object):

    def __init__(self, ren_win: all.vtkRenderWindow):
        self._ren_win = ren_win
        self._renderer = all.vtkRenderer()
        self._ren_win.AddRenderer(self._renderer)
        self._interactor = self._ren_win.GetInteractor()

    def add_actor(self, actor):
        if actor.__class__ in [all.vtkAxesActor, all.vtkOpenGLTextActor, all.vtkAssembly, all.vtkActor, all.vtkOpenGLActor]:
            self._renderer.AddActor(actor)
        elif actor.__class__ in [all.vtkScalarBarActor]:
            self._renderer.AddActor2D(actor)
        elif actor.__class__ == list:
            for this_actor in actor:
                self._renderer.AddActor(this_actor)

    def del_actor(self, actor):
        self._renderer.RemoveActor(actor)

    def render_once(self):
        self._interactor.Render()
