import turtle
import colorsys

# Screen Setup for Instagram Reels (9:16)
screen = turtle.Screen()
screen.setup(width=540, height=960)
screen.bgcolor("#030208")  # Cyberpunk Deep Space Background
screen.title("Day 04: Cybernetic Portal - Coding With Vishesh")

# Animation Smoothness Control (Tracer & Delay)
screen.tracer(1, 8)  # Controlled frame delay (~28-30 seconds total)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Cyberpunk Portal Parameters
total_layers = 160
sides = 6  # Hexagonal Cyber Grid Structure

for i in range(total_layers):
    # Dynamic Hue Shift: Neon Cyan (0.5) -> Electric Magenta (0.85)
    hue = (0.5 + (i * 0.0035)) % 1.0
    rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)  # Max Saturation & Brightness
    
    t.pencolor(rgb)
    
    # Depth Scaling & Dynamic Glow Thickness
    size = i * 2.8
    pen_width = max(1, int(i * 0.035))
    t.pensize(pen_width)
    
    # Drawing Polygon for 3D Portal Layer
    t.penup()
    t.goto(0, 0)
    t.setheading(i * 7.5)  # Continuous Rotational Vortex Angle
    t.forward(size * 0.4)
    t.pendown()
    
    for _ in range(sides):
        t.forward(size)
        t.right(360 / sides)

screen.update()
turtle.done()