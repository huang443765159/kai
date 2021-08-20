import vtk

# Visualize
colors = vtk.vtkNamedColors()
# Create points
p0 = [0.0, 0.0, 0.0]
p1 = [1.0, 0.0, 0.0]
p2 = [1.0, 1.0, 0.0]
p3 = [0.0, 1.0, 0.0]
p4 = [2.0, 0.0, 0.0]
p5 = [2.0, 1.0, 0.0]


# LineSource: draw a line with two points
def createLine1():
    lineSource = vtk.vtkLineSource()
    lineSource.SetPoint1(p1)
    lineSource.SetPoint2(p2)

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(lineSource.GetOutputPort())
    return mapper


# LineSource Multi-point continuous straight line
def createLine2():
    lineSource = vtk.vtkLineSource()
    points = vtk.vtkPoints()
    points.InsertNextPoint(p0)
    points.InsertNextPoint(p1)
    points.InsertNextPoint(p2)
    points.InsertNextPoint(p3)
    lineSource.SetPoints(points)

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(lineSource.GetOutputPort())
    return mapper


# LineSource multi-point set geometry + topology
def createLine3():  # 多条线添加 一个points_actor添加多条线段
    # Create a vtkPoints object and store the points in it
    points = vtk.vtkPoints()
    points.InsertNextPoint(p0)
    points.InsertNextPoint(p1)
    points.InsertNextPoint(p2)
    points.InsertNextPoint(p3)
    points.InsertNextPoint(p4)
    points.InsertNextPoint(p5)

    # Create a cell array to store the lines in and add the lines to it
    lines = vtk.vtkCellArray()

    # for i in range(0, 5, 2):
    #     line = vtk.vtkLine()
    #     line.GetPointIds().SetId(0, i)
    #     line.GetPointIds().SetId(1, i + 1)
    #     lines.InsertNextCell(line)
    line = vtk.vtkLine()  # 默认为2个端点，
    # print(line.GetPointIds())
    # line.GetPointIds().SetNumberOfIds(4)  # 可以设置为N个端点
    line.GetPointIds().SetId(0, 0)  # SetId第一个参数为端点ID， 第二个参数为点的ID
    line.GetPointIds().SetId(1, 1)
    lines.InsertNextCell(line)
    line.GetPointIds().SetId(0, 1)
    line.GetPointIds().SetId(1, 4)
    # line.GetPointIds().SetId(2, 4)
    lines.InsertNextCell(line)
    # Create a polydata to store everything in
    linesPolyData = vtk.vtkPolyData()

    # Add the points to the dataset geometry
    linesPolyData.SetPoints(points)

    # Add the lines to the dataset topology
    linesPolyData.SetLines(lines)

    # Setup actor and mapper
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(linesPolyData)
    return mapper


def main():
    renderer = vtk.vtkRenderer()
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.SetWindowName("Line")
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)
    # Visualize
    colors = vtk.vtkNamedColors()
    renderer.SetBackground(colors.GetColor3d("Silver"))

    actor = vtk.vtkActor()
    # The first way
    # actor.SetMapper(createLine1())
    # The second way
    # actor.SetMapper(createLine2())
    # The third way
    actor.SetMapper(createLine3())

    actor.GetProperty().SetLineWidth(4)
    actor.GetProperty().SetColor(colors.GetColor3d("Peacock"))
    renderer.AddActor(actor)

    renderWindow.Render()
    renderWindowInteractor.Start()


if __name__ == '__main__':
    main()
