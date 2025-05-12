from vpython import *

# GlowScript 3.0 VPython
# Trajectory of a ball thrown on a rotating space station with 'artificial gravity'
# as seen from the inertial frame and from a frame rotating with the space station.

# Written by Bruce Sherwood, licensed under Creative Commons 4.0.
# All uses permitted, but you must not claim that you wrote it, and
# you must include this license information in any copies you make.
# For details see http://creativecommons.org/licenses/by/4.0

# These "global" variables must be established before the mouse handling routines which set them:
got_velocity = False
velocity = vector(0, 0, 0)
pause = False
rotation = 0
drag = False

class SpaceStation:
    def __init__(self, canvas):
        self.num_boxes = 50  # number of boxes used to create the ring-shaped space station
        self.radius = 10  # inner radius of space station
        self.height = 2  # height of release of ball above the "floor" of the space station
        self.canvas = canvas
        canvas.select()

        # Person in the space station
        self.person = cylinder(pos=vector(0, -self.radius, 0), axis=vector(0, self.height, 0),
                               size=vector(self.height, 2 * 0.1, 2 * 0.1))

        thickness = 0.5  # thickness of space station
        angle_step = 2 * pi / self.num_boxes
        paint = color.red
        red = True
        boxes = [self.person]

        for i in range(self.num_boxes):
            angle = i * angle_step
            box = box(pos=(self.radius + thickness / 2) * vector(cos(angle), sin(angle), 0),
                      size=vector(thickness, 2 * (self.radius + thickness) * sin(angle_step / 2), thickness))
            if red:
                box.color = color.red
                red = False
            else:
                box.color = color.blue
                red = True
            box.rotate(angle=angle, axis=vector(0, 0, 1))
            boxes.append(box)

        self.hull = compound(boxes)

        # Ball in the space station
        self.ball = sphere(pos=self.person.pos + self.person.axis,
                           color=color.orange, size=2 * 0.2 * vector(1, 1, 1))

        self.trail = attach_trail(self.ball, radius=0.1 * self.ball.size.x, pps=10, retain=500)
        self.reset()

    def reset(self):
        global rotation
        self.hull.rotate(angle=-rotation, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
        self.ball.pos = self.person.pos + self.person.axis
        self.trail.clear()
        rotation = 0


def bind_mouse(station, vector1, vector2):
    global pause
    if pause:
        return
    s = station.canvas

    def down():
        global drag, got_velocity, velocity

        def set_velocity():
            vector1.axis = s.mouse.pos - vector1.pos
            vector2.axis = vector1.axis
            if station is station1:
                vector2.axis.x -= scalefactor * initial_velocity
            else:
                vector2.axis.x += scalefactor * initial_velocity
                vector2.size.x = mag(vector2.axis)

        set_velocity()
        drag = True

        def move():
            global drag, pause
            if pause:
                return
            if drag:
                set_velocity()

        def up():
            global drag, got_velocity, velocity, pause
            if pause:
                pause = False
                return
            drag = False
            if mag(vector1.axis) <= station.ball.size.y / 2:
                vector1.axis = vector(0, 0, 0)
            elif mag(vector2.axis) <= station.ball.size.y / 2:
                vector2.axis = vector(0, 0, 0)
            if station is station1:
                velocity = vector1.axis / scalefactor
            else:
                velocity = vector2.axis / scalefactor
            got_velocity = True

        s.bind("mousemove", move)
        s.bind("mouseup", up)

    s.bind("mousedown", down)


# Define birthdates for the rotation period (choosing the quotient closest to 1)
pair1_birthdate = 7  # Example: 7th day of the month
pair2_birthdate = 14  # Example: 14th day of the month
rotation_period = pair2_birthdate / pair1_birthdate  # Rotation period is the quotient

# Create canvas
scene1 = canvas(width=430, height=400, align='left', userspin=False, userzoom=False)
scene2 = canvas(width=430, height=400, align='left', userspin=False, userzoom=False)

scene1.title = """ROTATING SPACE STATION
Inertial frame on the left, rotating frame on the right."""

station1 = SpaceStation(scene1)
station2 = SpaceStation(scene2)

scene1.autoscale = scene2.autoscale = False

omega = 2 * pi / rotation_period  # Angular speed based on the new rotation period
delta_t = 0.001 * 2 * pi / omega
initial_velocity = omega * (station1.radius - station1.height)
scalefactor = 5 / (omega * station1.radius)

velocity1 = arrow(canvas=scene1, pos=station1.ball.pos, color=color.green,
                  axis=vector(0, 0, 0), shaftwidth=0.4, visible=False)

velocity2 = arrow(canvas=scene2, pos=station2.ball.pos, color=color.green,
                  axis=vector(0, 0, 0), shaftwidth=0.4, visible=False)

instruct1 = label(canvas=scene1, pos=vector(0, station1.radius / 2, 0),
                  text="Drag initial velocity in the inertial frame", visible=False)

instruct2 = label(canvas=scene2, pos=vector(0, station2.radius / 2, 0),
                  text="Or drag initial velocity relative to rotating space station", visible=False)

click1 = label(canvas=scene1, pos=vector(0.8 * station1.radius, -1 * station1.radius, 0),
               text="Click to\nstart over", visible=False)

click2 = label(canvas=scene2, pos=vector(0.8 * station2.radius, -1 * station2.radius, 0),
               text="Click to\nstart over", visible=False)

bind_mouse(station1, velocity1, velocity2)
bind_mouse(station2, velocity2, velocity1)

# Main loop
while True:
    station1.reset()
    station2.reset()
    velocity1.axis = vector(0, 0, 0)
    velocity2.axis = vector(0, 0, 0)
    velocity1.visible = velocity2.visible = True
    instruct1.visible = instruct2.visible = True
    while True:
        rate(50)
        if got_velocity:
            break
    velocity1.visible = velocity2.visible = False
    instruct1.visible = instruct2.visible = False
    r = vector(station1.ball.pos)  # initialize r without making it equivalent to ball.pos
    t = 0
    while True:
        rate(0.5 / delta_t)  # slow down the plotting
        rotation += omega * delta_t

        station1.ball.rotate(angle=omega * delta_t, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
        station1.hull.rotate(angle=omega * delta_t, axis=vector(0, 0, 1), origin=vector(0, 0, 0))

        r = r + velocity * delta_t  # update the actual position of the ball (in inertial frame)
        station1.ball.pos = r
        new_r = vector(r)
        station2.ball.pos = new_r.rotate(angle=-omega * t, axis=vector(0, 0, 1))

        if mag(station1.ball.pos) >= station1.radius:  # if ball hits floor, make it stick there
            direction = norm(station1.ball.pos)
            station1.ball.pos = station1.radius * direction
            direction = norm(station2.ball.pos)
            station2.ball.pos = station2.radius * direction
            break
        t += delta_t
    click1.visible = click2.visible = True
    pause = True
    while True:
        rate(50)
        if not pause:
            break
    got_velocity = False
    click1.visible = click2.visible = False
