import json
import pyglet
from pyglet.window import *
from pyglet.gl import *
from Mesh import *

window = pyglet.window.Window()

glEnable(GL_DEPTH_TEST)
glDepthFunc(GL_LESS)
glEnableClientState(GL_VERTEX_ARRAY)

vertices = [
0.0, 0.0, 0.0,
window.width, 0.0, 0.0,
window.width, window.height, 0.0
]

newMesh = Mesh()
newMesh.load(vertices)

@window.event
def on_draw():
	window.clear()
	newMesh.draw()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
		print "left"

@window.event
def on_mouse_press(x, y, button, modifiers):
	if button == mouse.LEFT:
		if modifiers & key.MOD_SHIFT:
			print 'Alt Attack'
		else:
			print 'Attack'


pyglet.app.run()
