screen credits:
    add "#090909"
    vbox at scrolly, delayed_fall_in:
        fixed:
            xysize(1280,720)
            use astra_credits
        fixed:
            xysize(1280,720)
            use patchwork_credits
        fixed:
            xysize(1280,720)
            use emp_credits
        fixed:
            xysize(1280,720)
            use credits_bye

screen astra_credits:

    add "astralore logo.png" zoom 0.5 xalign 0.9 yalign 0.5
    vbox:
        xalign 0.1
        yalign 0.5
        spacing 20
        label "Astralore Games" text_size 60
        text "Vale Magri (valeatory)" size 40
        text "Character Art and Programming" xoffset 20
        text "Puzzle Design" xoffset 20
        text "Renee Archbold (Archaeren)" size 40
        text "Writing" xoffset 20
        text "Directing" xoffset 20
        text "Music Sourcing" xoffset 20

screen patchwork_credits:

    add "patchwork princess splash.png" zoom 0.5 xalign 1.0 yalign 0.5
    vbox:
        xalign 0.1
        yalign 0.5
        spacing 20
        label "Patchwork Princess" text_size 60
        text "Vanessa Parker (Azura)" size 40
        text "Writing" xoffset 20
        text "GUI Design and Art" xoffset 20
        text "BG Art Sourcing and Prep" xoffset 20

image credits emp = im.MatrixColor("emp_icons.png", im.matrix.desaturate())

screen emp_credits:

    add "credits emp" xalign 0.95 yalign 0.5
    vbox:
        xalign 0.1
        yalign 0.5
        spacing 20
        label "From Nowhere in Particular" text_size 60
        text "Elaine M. Podosek (Empish)" size 40
        text "Puzzle Programming" xoffset 20
        text "Effects Programming" xoffset 20
        text "GUI Programming" xoffset 20
        text "There was a lot of programming okay?" xoffset 20

screen credits_bye:
    text "Thanks for playing!" at truecenter:
        size 120

transform scrolly:
    ypos 320
    linear 25 ypos -1280
    linear 20 ypos -2560
    linear 20 ypos -3840
