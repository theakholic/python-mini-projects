from turtle import *
def spiral(length):
	if length < 1 or length > 1000:
		return
	forward(length)
	rt(90)
	spiral(length - 5)

def spiral_b(length, angle=90,parameter=0.9):
	if length < 1 or length > 1000:
		return
	forward(length)
	rt(angle)
	spiral_b(parameter*length,angle,parametercl)

def svtree_2(length, level=5, angle=60,parameter=0.5):
	"""Create a recursive side view tree using turtle graphics."""
	if level <= 0 or length < 1:
		return
	fd(length)
	lt(angle)
	svtree(length*parameter, level - 1, angle, parameter)
	
	rt(2*angle)
	
	svtree(length*parameter, level - 1, angle, parameter)
	lt(2*angle)
	bk(length)



def svtree_2(length, level=5, angle=60,parameter=0.5):
	"""Create a recursive side view tree using turtle graphics."""
	if level <= 0 or length < 1:
		return
	fd(length)
	lt(2*angle)
	svtree(length*parameter, level - 1, angle, parameter)
	rt(angle)
	svtree(length*parameter, level - 1, angle, parameter)
	rt(2*angle)
	svtree(length*parameter, level - 1, angle, parameter)
	rt(angle)
	svtree(length*parameter, level - 1, angle, parameter)
	lt(2*angle)
	bk(length)


def koch(length,max_level=3):
	if max_level == 0:
		fd(length)
		return
	koch(length/3.0, max_level - 1)
	lt(60)
	koch(length/3.0, max_level - 1)
	rt(120)
	koch(length/3.0, max_level - 1)
	lt(60)
	koch(length/3.0, max_level - 1)



def snowflake(sidelength, levels):
    """ fractal snowflake function
          sidelength: pixels in the largest-scale triangle side
          levels: the number of recursive levels in each side
    """
    koch( sidelength, levels )
    right(120)
    koch( sidelength, levels )
    right(120)
    koch( sidelength, levels )
    right(120)

