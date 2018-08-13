# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


default seeds1 = [
    Processor("1", 6, [6,5,4]),
    Processor("2", 6, [6,5,4]),
    Processor("3", 6, [6,5,4])
    ]

default task1 = Task("A", 2, "#abc")
default tasks1 = [
    task1,
    Task("B", 3, "#fed", [task1]),
    Task("C", 4, "#f12")
    ]

image bg control room = "control_room_overlay.png"
image bg hallway = "hallway_windows_overlay.png"


image space control room = "control_room_bg.png"
image space hallway = "hallway_windows_space_bg.png"

default size = (600,800)
default cool = False

# The game starts here.

label start:
    # call setup_sublevel(dissolve)
    # $num_active = 0
    # $turn_on(seeds1[0])
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
