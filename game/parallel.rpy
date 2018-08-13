init python:
    def update_mouse():
        if really_shaking:
            return
        x, y = renpy.get_mouse_pos()
        store.offsetx = x - centerx
        store.offsety = y - centery

    def update_next_shake():
        store.next_shake = renpy.random.randint(12,80)/10.0
        store.really_shaking = True
        renpy.music.set_volume(renpy.random.randint(30,100)/100.0, channel="asteroid")
        store.num_shakes = renpy.random.randint(3,8)
        store.offsetx2 += renpy.random.randint(-10,10)
        store.offsety2 += renpy.random.randint(-10,10)
        renpy.show_screen("freak_mid")

    def shake_mid():
        store.offsetx2 += renpy.random.randint(-10,10)
        store.offsety2 += renpy.random.randint(-10,10)

    def shake_last():
        store.offsetx2 += renpy.random.randint(-10,10)
        store.offsety2 += renpy.random.randint(-10,10)
        renpy.show_screen("unfreak")

    def undo_shake1():
        store.offsetx2 /= 2
        store.offsety2 /= 2

    def undo_shake2():
        store.offsetx2 = 0
        store.offsety2 = 0
        store.shaking = False
        store.really_shaking = False


    def parallax_bg(trans, st, at):
        update_mouse()
        trans.xcenter = centerx - (offsetx/10) + offsetx2
        trans.ycenter =  centery - (offsety/10) + offsety2
        return 0.01


    def parallax_char(trans, st, at):
        update_mouse()
        trans.xoffset = - (offsetx/15) + offsetx2/2
        trans.yoffset = - (offsety/15) + offsety2/2
        return 0.01

    def parallax_space(trans, st, at):
        update_mouse()
        trans.xoffset = - (offsetx/20)
        trans.yoffset = - (offsety/20)
        return 0.01

    renpy.music.register_channel("asteroid", mixer="sfx")


define centerx = config.screen_width/2
define centery = config.screen_height/2
default offsetx = 0
default offsety = 0
default offsetx2 = 0
default offsety2 = 0

screen mouse_grabber:
    timer 0.01 action Function(update_mouse) repeat True
    #text "[shaking]" at truecenter


# screen bg_parallax(bg):
#     layer "lower"
#     add bg:
#         xcenter centerx - (offsetx/10) + offsetx2
#         ycenter centery - (offsety/10) + offsety2

default next_shake = 0.1
default num_shakes = 3
default shaking = False
default really_shaking = False

screen freak_parent:
    timer 0.5 action If(not shaking, [Show("freak"),SetVariable("shaking", True)], NullAction()) repeat True

screen freak:
    timer next_shake action [Function(update_next_shake), Play("asteroid", "asteroid_impact.mp3", loop=False), Hide("freak")]

screen freak_mid:
    $ delay = 0.05
    for i in range(num_shakes):
        timer delay action Function(shake_mid)
        $ delay += renpy.random.randint(3,10)/100.0
    timer delay action [Function(shake_last), Hide("freak_mid")]

screen unfreak:
    timer 0.05 action Function(undo_shake1)
    timer 0.1 action Function(undo_shake1)
    timer 0.15 action Function(undo_shake1)
    timer 0.2 action [Function(undo_shake2), Hide("unfreak")]