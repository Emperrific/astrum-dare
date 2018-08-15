# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define cright = Transform(xalign=0.75, yalign=1.0)
define cleft = Transform(xalign=0.25, yalign=1.0)

default lens3 = [16,15,14,13,13,11,10,9,8]
default seeds3 = [
    Processor("1", lens3[0], lens3),
    Processor("2", lens3[0], lens3),
    Processor("3", lens3[0], lens3),
    Processor("4", lens3[0], lens3),
    Processor("5", lens3[0], lens3),
    Processor("6", lens3[0], lens3),
    Processor("7", lens3[0], lens3)
    ]

default task3B = Task("Z", 6, "#0f3")
default task3E = Task("Y", 4, "#f07")
default task3F = Task("X", 6, "#cd0")
default task3H = Task("V", 6, "#f70")
default task3J = Task("U", 3, "#999")
default task3K = Task("T", 8, "#fff")
default task3L = Task("S", 5, "#ff0")
default task3M = Task("R", 4, "#0ff", [task3K, task3J])
default task3N = Task("Q", 3, "#f0f", [task3H])

default tasks3 = [
    Task("P", 6, "#00f", [task3L]),
    task3B,
    Task("O", 4, "#f00", [task3B]),
    Task("N", 6, "#07f", [task3E]),
    task3E,
    task3F,
    Task("M", 8, "#70f", [task3N]),
    task3H,
    Task("L", 3, "#0f7", [task3F, task3M]),
    task3J,
    task3K,
    task3L,
    task3M,
    task3N,
    ]

default lens2 = [16,15,14,13,12,11,10,9,8]
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

default lens1 = [9,8,7,6]
default seeds1 = [
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

image Patchwork = "images/patchwork princess splash.png"
image Astralore = "images/astralore splash.png"

label splashscreen:
    show Astralore with dissolve
    $ renpy.pause (2, hard=True)
    hide Astralore with dissolve
    show Patchwork with dissolve
    $ renpy.pause (2, hard=True)
    hide Patchwork with dissolve
    return

default size = (600,800)
default cool = False

label main_menu:
    stop music
    scene black
    play music config.main_menu_music fadein 1.0
    call screen main_menu
    return
# The game starts here.

label start:
    call setup_sublevel(dissolve)
    # $num_active = 0
    # $turn_on(seeds1[0])

    # $cool = renpy.call_screen("pipeline_puzzle", seeds1, tasks1)()
    #
    # if cool:
    #     "You succeeded"
    # else:
    #     "You dun fucked up"
    #
    # show screen credits
    # pause
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
