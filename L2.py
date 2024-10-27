import pgzrun
import random

WIDTH = 600
HEIGHT = 600
def draw():
	w = 600
	h = 0
	screen.fill("black")
	screen.draw.text("hello",center=(300,300),color="blue")
	for i in range(15):
		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)
		rectangle = Rect((10,240),(w,h)) # type: ignore
		rectangle.center = (300,300)
		screen.draw.rect(rectangle,(r,g,b))  # type: ignore
		w = w-40
		h= h+40

pgzrun.go()
