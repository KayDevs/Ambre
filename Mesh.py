from pyglet.gl import *

#TODO: texture buffer, material pixel shaders
#TODO: vertex shaders kinematics
class Mesh():
	def __init__(self):
		self.buffer = (GLuint)(0) #the vertex buffer object
		glGenBuffers(1, self.buffer)
	def load(self, vertices):
		self.vertices = vertices #the actual vertices array
		data_gl = (GLfloat * len(vertices))(*vertices) #vertices array formatted for OpenGL
		glBindBuffer(GL_ARRAY_BUFFER, self.buffer)
		glBufferData(GL_ARRAY_BUFFER, len(vertices)*4, data_gl, GL_STATIC_DRAW)
	def bind(self):
		glBindBuffer(GL_ARRAY_BUFFER, self.buffer)
	def vertex(self):
		self.bind()
		glVertexPointer(3, GL_FLOAT, 0, 0)
	def draw(self):
		glLoadIdentity()
		self.vertex()
		glDrawArrays(GL_TRIANGLES, 0, len(self.vertices)//2)
