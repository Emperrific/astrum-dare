# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

default seed1 = Processor("1", 6, [6,5,4])
default seed2 = Processor("2", 6, [6,5,4])
default seed3 = Processor("3", 6, [6,5,4])

default task1 = Task("A", 2, "#abc")
default task2 = Task("B", 3, "#fed", [task1])
default task3 = Task("C", 4, "#f12")

image bg control room = "control_room_overlay.png"
image bg hallway = "hallway_windows_overlay.png"

image space control room = "control_room_bg.png"
image space hallway = "hallway_windows_space_bg.png"

image security = "security.png"
default size = (600,800)

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    # $num_active = 0
    # $turn_on(seed1)

    # $cool = renpy.call_screen("pipeline_puzzle", [seed1, seed2, seed3], [task1, task2, task3])

    # if cool:
    #     "You succeeded"
    # else:
    #     "You dun fucked up"
    # scene space control room:
    #     function parallax_space
    # show asteroids:
    #     function parallax_space
    # show overlay
    # show bg control room:
    #     function parallax_bg
    # with fade
    # pause
    # show security at leftish:
    #     function parallax_char
    # with easeinright
    # e "hiya"
    # menu:
    #     "Choice 1":
    #         "You chose choice 1"
    #     "Choice 2":
    #         "You chose choice 2"
    #     "Choice 3":
    #         "You chose choice 3"
    # show screen freak_parent
    # pause
    # hide screen freak_parent
    # pause

    # scene space hallway at truecenter:
    #     function parallax_space
    # show asteroids pan:
    #     function parallax_space
    # show overlay

    # pause

    # call setup_environment("space hallway", "bg hallway", "asteroids pan", "overlay", fade)
    call setup_hallway(fade)
    call setup_chara("security", leftish, easeinright)
    pause

    # call setup_environment("space control room", "bg control room", "asteroids", "overlay", dissolve)
    call setup_ctrl_room(dissolve)
    pause
    return
