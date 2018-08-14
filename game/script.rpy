# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define cright = Transform(xalign=0.75, yalign=1.0)

default lens2 = [16,15,14,13,12,11,10]
default seeds2 = [
    Processor("1", lens2[0], lens2),
    Processor("2", lens2[0], lens2),
    Processor("3", lens2[0], lens2),
    Processor("4", lens2[0], lens2),
    Processor("5", lens2[0], lens2),
    Processor("6", lens2[0], lens2),
    Processor("7", lens2[0], lens2)
    ]

default task2B = Task("B", 6, "#0f3")
default task2E = Task("E", 4, "#f07")
default task2F = Task("F", 6, "#cd0")
default task2H = Task("H", 6, "#f70")
default task2J = Task("J", 3, "#999")
default task2K = Task("K", 1, "#fff")
default task2L = Task("L", 5, "#ff0")
default task2M = Task("M", 4, "#0ff", [task2K, task2J])
default task2N = Task("N", 3, "#f0f", [task2H])

default tasks2 = [
    Task("A", 6, "#00f", [task2L]),
    task2B,
    Task("C", 4, "#f00", [task2B]),
    Task("D", 6, "#07f", [task2E]),
    task2E,
    task2F,
    Task("G", 1, "#70f", [task2N]),
    task2H,
    Task("I", 2, "#0f7", [task2F, task2M]),
    task2J,
    task2K,
    task2L,
    task2M,
    task2N,
    ]

define lens1 = [9,8,7,6]
define seeds1 = [
    Processor("1", lens1[0], lens1),
    Processor("2", lens1[0], lens1),
    Processor("3", lens1[0], lens1),
    Processor("4", lens1[0], lens1),
    ]

define task1A = Task("A", 2, "#00f")
define task1E = Task("E", 3, "#f0f")
define tasks1 = [
    task1A,
    Task("B", 2, "#0f0", [task1E]),
    Task("C", 3, "#f00", [task1A]),
    Task("D", 6, "#0ff"),
    task1E,
    Task("F", 4, "#ff0", [task1A]),
    ]

image bg control room = "control_room_overlay.png"
image bg hallway = "hallway_windows_overlay.png"
image bg rd room = "spaceship-1511655_1920.jpg"


image space control room = "control_room_bg.png"
image space hallway = "hallway_windows_space_bg.png"

default size = (600,800)
default cool = False

# The game starts here.

label start:
    # call setup_sublevel(dissolve)
    # $num_active = 0
    # $turn_on(seeds2[0])
    #
    # $cool = renpy.call_screen("pipeline_puzzle", seeds1, tasks1)()
    #
    # if cool:
    #     "You succeeded"
    # else:
    #     "You dun fucked up"
    #
    jump story
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene space control room:
    #     function parallax_space
    # show asteroids:
    #     function parallax_space
    # show overlay
    # show bg control room:
    #     function parallax_bg
    # with fade
    # pause
    # menu:
    #     "Choice 1":
    #         "You chose choice 1"
    #     "Choice 2":
    #         "You chose choice 2"
    #     "Choice 3":
    #         "You chose choice 3"
    # show screen Asteroid_Impact_Louder.ogg
    # pause
    # hide screen Asteroid_Impact_Louder.ogg
    # pause

    # scene space hallway at truecenter:
    #     function parallax_space
    # show asteroids pan:
    #     function parallax_space
    # show overlay

    # pause

    # call setup_environment("space hallway", "bg hallway", "asteroids pan", "overlay", fade)

    # call setup_environment("space control room", "bg control room", "asteroids", "overlay", dissolve)
    # call setup_ctrl_room(dissolve)
    # pause
    # return
