import json
import pyglet
from pyglet.window import *
from pyglet.gl import *
from Mesh import *
from Material import *

def vec(*floats):
	return (GLfloat * len(floats))(*floats)

window = pyglet.window.Window()

glEnable(GL_DEPTH_TEST)
glDepthFunc(GL_LESS)
glEnable(GL_CULL_FACE)
glCullFace(GL_BACK)
glEnableClientState(GL_VERTEX_ARRAY)

vertices = [
0.0, 0.0, 0.0,
window.width, 0.0, 0.0,
window.width, window.height, -2.0
]

vs = open('./basic_vs.glsl')
vs_lines = vs.readlines()
fs = open('./basic_fs.glsl')
fs_lines = fs.readlines()

newMesh = Mesh()
newMesh.load(vertices)
newMaterial = Material(vs_lines, fs_lines)

@window.event
def on_draw():
	window.clear()
	if(newMaterial.linked):
		newMaterial.bind()
	newMesh.draw()

@window.event
def on_key_press(symbol, modifiers):
	if symbol == key.SPACE:
		print "cool"

@window.event
def on_mouse_press(x, y, button, modifiers):
	if button == mouse.LEFT:
		if modifiers & key.MOD_SHIFT:
			print 'Alt Attack'
		else:
			print 'Attack'


pyglet.app.run()
