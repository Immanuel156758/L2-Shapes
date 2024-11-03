import pgzrun

WIDTH = 600
HEIGHT = 600

def draw():
	screen.fill("dark green")
	r1 = Rect((200,200),(300,300))
	screen.draw.filled_rect(r1,"white")
	screen.draw.line((300,300),(300,400),"red")
	screen.draw.line((300,300),(400,350),"red")
	screen.draw.line((300,400),(400,350),"red")

pgzrun.go()