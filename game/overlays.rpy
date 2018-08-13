image blue:
    "#01e"
    alpha 0.05

image blue2:
    "#2c00e5"
    alpha 0.1

image yellow:
    "#e8e24c"
    alpha 0.03


transform overlay_transform(max_alpha):
    on show:
        alpha 0.0
        linear 1.0 alpha max_alpha
    on hide:
        alpha max_alpha
        linear 0.5 alpha 0.0

image overlay:
    "blue" with Dissolve(1.5)
    choice:
        1.0
    choice:
        1.2
    choice:
        2.3
    choice:
        1.8
    "blue2" with Dissolve(1.5)
    choice:
        1.1
    choice:
        1.5
    choice:
        2.0
    choice:
        2.2
    "yellow" with Dissolve(1.5)
    1.6
    repeat


image asteroid:
    "asteroid.png"
    alpha 0.9
    subpixel True
    rotate 0
    choice:
        linear 5.0 rotate 360
    choice:
        linear 4.0 rotate 360
    choice:
        linear 6.0 rotate 360
    repeat

image asteroid_sm:
    "asteroid.png"
    alpha 0.9
    zoom 0.5
    subpixel True
    rotate 0
    choice:
        linear 5.0 rotate 360
    choice:
        linear 4.0 rotate 360
    choice:
        linear 3.0 rotate 360
    repeat

image asteroid cr:
    "control_room_asteroids.png"
    crop(600,400,600,400)
    alpha 0.9

image asteroids1 = SnowBlossom("asteroid", 10, xspeed=(5,300), yspeed=(10,100), start=50, horizontal=True)
image asteroids2 = SnowBlossom("asteroid_sm", 8, xspeed=(5,100), yspeed=(5,50), start=20, horizontal=True)
image asteroids cr1 = SnowBlossom("asteroid cr", 2, xspeed=(50,100), yspeed=(5,50), start=20, horizontal=True)

image asteroids = Fixed("asteroids1", "asteroids2")
image asteroids cr = Fixed("asteroids cr1")


image asteroid belt = Composite((3840,1317), (0,0), "hallway_windows_asteroids.png", (1920, 0), "hallway_windows_asteroids")
image asteroids pan:
    "asteroid belt"
    xpos 0
    ycenter 410
    linear 35.0 xpos -1920
    repeat