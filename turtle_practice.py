#Turtle Practice
import turtle

def svTree(depth, length):
	"""Creates a recursive tree with recurion depth = depth and max branch length = length."""
	if depth <= 0:
		return

	if depth == 1:
		turtle.forward(length)
		turtle.backward(length)

	if length <= 0:
		return

	turtle.forward(length)
	turtle.left(60)
	svTree(depth-1, 0.5*length)
	turtle.right(120) #just turns
	svTree(depth-1,0.5*length)
	turtle.left(60)
	#print("Coming back at " + str(length))
	turtle.back(length)
