from OpenGL.GL import *


vertices = (
    (0, 0, 0),
    (1, 0.7, 0),
    (1, 0, 0)
)

edges = (
    (0, 1),
    (0, 2)
)


def update():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv((1,0,0))
            glVertex3fv(vertices[vertex])



    glEnd()

