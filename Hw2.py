import pgzrun

WIDTH = 600
HEIGHT = 600

def draw():
	screen.fill("dark green")
	screen.draw.filled_circle((300,300),200,"white")
	screen.draw.filled_circle((300,300),150,"black")
	screen.draw.filled_circle((300,300),100,"blue")
	screen.draw.filled_circle((300,300),50,"red")
	screen.draw.filled_circle((300,300),20,"yellow")

pgzrun.go()