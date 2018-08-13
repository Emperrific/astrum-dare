

define default_zoom = 0.33

image zeni_mouth open_smile = renpy.easy_displayable("zeni_mouth open_neutral")
image zeni_mouth open_smirk = renpy.easy_displayable("zeni_mouth open_neutral")
image zeni_mouth open_frown = renpy.easy_displayable("zeni_mouth open_neutral")
image misha_mouth open_smile = renpy.easy_displayable("misha_mouth open_neutral")
image misha_mouth open_smirk = renpy.easy_displayable("misha_mouth open_neutral")
image misha_mouth open_frown = renpy.easy_displayable("misha_mouth open_neutral")

init python:
    setup_layered_anims("misha")
    setup_layered_anims("zeni")

layeredimage misha:
    always "misha_base":
        zoom default_zoom
    group iris auto:
        zoom default_zoom
        attribute look_at default

    group eyes auto:
        zoom default_zoom
        attribute eyes_open default

    group brow auto:
        zoom default_zoom
        attribute original default

    group mouth auto:
        zoom default_zoom
        attribute neutral default


layeredimage zeni:
    always "zeni_base":
        zoom default_zoom
    group iris auto:
        zoom default_zoom
        attribute look_at default

    group eyes auto:
        zoom default_zoom
        attribute eyes_open default

    group brow auto:
        zoom default_zoom
        attribute original default

    group mouth auto:
        zoom default_zoom
        attribute neutral default
