
image zeni_mouth open_smile = renpy.easy_displayable("zeni_mouth open_neutral")
image zeni_mouth open_smirk = renpy.easy_displayable("zeni_mouth open_neutral")
image zeni_mouth open_frown = renpy.easy_displayable("zeni_mouth open_neutral")

define config.all_character_callbacks = [speaker_callback]

transform blinking_anim(norm_d, closing_d, blink_d):
    norm_d
    choice:#random pause
        0.1
    choice:
        1
    choice:
        2
    choice:
        3
    choice:
        4
    closing_d
    pause .1
    blink_d
    pause .2
    closing_d
    pause .15
    repeat

transform anim_talk_once(norm_d, speak_d, open_d, anim_time):
    choice 2:
        speak_d
        pause anim_time
        norm_d
        pause anim_time*3/4
    choice:
        open_d
        pause anim_time *3/4
        speak_d
        pause anim_time /2
        norm_d
        pause anim_time
    choice:
        open_d
        pause anim_time
        norm_d
        pause anim_time*3/4

transform talking_anim(speak_d, open_d, close_d):
    choice:
        anim_talk_once(close_d, speak_d, open_d, .25)
    choice:
        anim_talk_once(close_d, speak_d, open_d, .15)
    repeat

default current_speaker = None

#Callbacks for lip flap and dialogue color

#composite image stuff, not relevant to the ATL
init -1 python:

    def img_or_default(d, dflt=None):
        if isinstance(d, DynamicDisplayable) \
            or isinstance(d, ImageReference) \
            or renpy.has_image(d):
            return d
        return dflt

    def speaker_callback(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "begin":
            store.current_speaker = _last_say_who
        elif event in ("slow_done", "end"):
            store.current_speaker = None


    def is_speaking(img_name):
        if current_speaker:
            return globals()[current_speaker].image_tag in img_name.split()
        return False

    def generate_speaking_transform_e(img_name, option, word, dflt_option, image_format):
        get_disp = lambda w, o: image_format(img_name+"_mouth "+w+"_"+o)
        return WhileSpeaking(img_name,
                talking_anim(
                    img_or_default(get_disp("part", option), get_disp("part", dflt_option)),
                    img_or_default(get_disp("open", option), get_disp("open", dflt_option)),
                    img_or_default(get_disp("closed", option), get_disp("closed", dflt_option))),
                get_disp(word, option))
    # This returns speak_d/not_d based on if the character is speaking,
    def while_speaking(name, speak_d, not_d, st, at):
        if is_speaking(name):
            return speak_d, .1
        else:
            return not_d, None

    # Curried form of the above.
    curried_while_speaking = renpy.curry(while_speaking)

    # Displays d when the named character is speaking, and Null otherwise.
    def WhileSpeaking(name, speak_d, not_d):
        return DynamicDisplayable(curried_while_speaking(name, speak_d, not_d))


    attr_imgs = {}
    def setup_layered_anims(img_name, image_format=None, default_mouth="neutral"):
        if not image_format: image_format = renpy.easy_displayable

        for attrs in renpy.get_available_image_attributes(img_name+"_eyes"):
            attr = attrs[0]
            renpy.image(
                img_name+"_eyes_eyes_"+attr, #put this in the format layeredimage expects
                #closed eyes don't blink
                (
                    image_format(img_name+"_eyes "+attr) if attr in ("closed", "rest")
                    else blinking_anim(
                        image_format(img_name+"_eyes "+attr),
                        #blinking frame is dependent on how open the eyes are
                        image_format(img_name+"_eyes narrow") if attr not in ("narrow", "squint")
                                                          else image_format(img_name+"_eyes squint"),
                        image_format(img_name+"_eyes rest")
                    )
                )
            )
        for attrs in renpy.get_available_image_attributes(img_name+"_mouth"):
            attr = attrs[0]
            word, option = attr.split('_')
            print(img_name+"_mouth_"+ (option if word=="closed" else attr))
            renpy.image(
                #put this in the format layeredimage expects
                img_name+"_mouth_"+ (option if word=="closed" else attr), #only closed doesn't use the word
                generate_speaking_transform_e(img_name, option, word, default_mouth, image_format), #the displayable

            )
