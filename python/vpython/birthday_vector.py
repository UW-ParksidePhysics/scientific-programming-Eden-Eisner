from vpython import *

# GlowScript 3.0 VPython
# Written by Ruth Chabay, licensed under Creative Commons 4.0.
# All uses permitted, but you must not claim that you wrote it, and
# you must include this license information in any copies you make.
# For details see http://creativecommons.org/licenses/by/4.0

# Scene setup
scene.background = color.white
scene.width = 600
scene.height = 600
scene.forward = vector(-0.5, -0.3, -1)

scene.caption = """To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""

# Axes setup
x_axis = cylinder(color=vector(1, 0, 0), pos=vector(0, 0, 0), axis=vector(10, 0, 0), radius=0.3)
x_label = label(pos=vector(11, 0, 0), text="x", color=color.red, opacity=0, height=30, box=0)

y_axis = cylinder(color=color.green, pos=vector(0, 0, 0), axis=vector(0, 10, 0), radius=0.3)
y_label = label(pos=vector(0, 11, 0), text="y", color=color.green, opacity=0, height=30, box=0)

z_axis = cylinder(color=color.blue, pos=vector(0, 0, 0), axis=vector(0, 0, 10), radius=0.3)
z_label = label(pos=vector(0, 0, 11), text="z", color=color.blue, opacity=0, height=30, box=0)

# Vector setup: Using numbers from birthdates and months (e.g., 6, 9, and 15)
# Chosen birthdate values: 6 (month), 9 (year), and 15 (day)
vector_data = vector(6, 9, 15)  # Vector chosen with numbers from birthdates (6, 9, 15)

# Create the vector in the scene
vector_arrow = arrow(pos=vector(0, 0, 0), axis=vector_data, color=color.cyan, shaftwidth=0.5)

# Label for the vector
vector_label = label(pos=vector(6, 9, 15), text="(6, 9, 15)", color=color.cyan, opacity=0, height=30, box=0)

