label setup_environment(space, bg, asteroids, overlays, trans):
    # $space_img = "space [space]"
    scene expression space at truecenter:
        function parallax_space
    show expression asteroids:
        function parallax_space
    show expression overlays
    show expression bg:
        function parallax_bg
    with trans

    return

label setup_hallway(trans):
    call setup_environment("space hallway", "bg hallway", "asteroids pan", "overlay", trans)
    return

label setup_sublevel(trans):
    call setup_environment("bg sublevel", "bg sublevel", "asteroids", "overlays", trans)
    return

label setup_ctrl_room(trans):
    call setup_environment("space control room", "bg control room", "asteroids", "overlay", trans)
    return

label setup_chara(chara, name, pos, trans):
    show expression chara at pos as name:
        function parallax_char
    with trans
    return
