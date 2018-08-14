label choices:

    menu:
        with dissolve
        "Help Zeni." if talk_zeni == False:
            jump help_zeni
        "Help Misha." if talk_misha == False:
            jump help_misha
        "Help Aran." if talk_aran == False:
            jump help_aran
        "Help Fera." if talk_fera == False:
            jump help_fera

    # After 3 are chosen, go to Power Cell Found

    # If Fera is ignored, triggers Fera finding and stashing a weapon.
    #This leads to a bad ending if you ignore Fera and then leave her behind. She will attempt to kill you out of spite and Aran will die after jumping in front, leaving you to only escape with Zeni and/or Misha.



label help_zeni:
    $talk_zeni = True
    $chat_counter += 1

    show zeni look_at at middle, parallaxed_z with dissolve

    "I decide to give Zeni a hand."

    "From the looks of it, he’s in charge of the heaviest stuff."

    "I give him a little wave as I approach.  He looks baffled, as if he surprised that I would help him."

    show zeni smile eyes_open relax

    "Despite his surprise, he smiles when I grab one side of a particularly large storage container that he’s taking apart."

    z "You don't have to do that. I'm stuck with this kind of work every day."

    p "But I thought you were the Vice President of Security?"

    show zeni frown one_raised

    z "Also known as glorified manager slash scapegoat, basically."

    show zeni neutral original

    z "I mean, I'm not really complaining. You do what you have to do."

    p "That’s true."

    z "What is it that you do on the station?"

    p  "I'm a pilot. A fairly new graduate actually. Only been here about 3 weeks."

    show zeni eyes_rest

    z "That would explain why I don't recognize your name."

    show zeni eyes_open

    p "Yeah, I haven't really met most of the personnel yet."

    show zeni look_away sad frown

    "Zeni's eyes slide to the floor, and he goes uncomfortably quiet. Probably because all of the personnel that I just mentioned are very, very dead."

    "Surely some of them must have been his friends. His men."

    "I wish there were something I could say to change the topic, but it's hard to think about anything except for what's happened right now."

    "Let’s try a more positive question."

    menu:
        with dissolve
        "Ask him about his family.":
            p "So, um, do you have a family?"

            show zeni look_at eyes_wide original neutral

            z "A daughter. She’s 6."

            "But no mention of a mother... Probably best I if didn’t pry."

            p "Do you mind if I ask her name?"

            "Zeni sets down a steel crate and digs through it as he answers my question."

            z "Racia."

            show zeni eyes_open smile relax

            z "She’s a little songstress, just like her mother was."

            "With a sigh, Zeni leans against his box and gazes at me."

            show zeni neutral original

            z "What about you?"

            p "Oh... I was raised in a communal domicile on Jenri Alpha."

            show zeni eyes_wide raised frown

            z "So you were an orphan, then. I’m sorry."

            p "Don’t be. I never knew my parents."

            "Zeni balls his fists and grimaces."

            show zeni look_away angry

            z "The war?"

            p "Pirates."

            z "That’s even worse. I sure hope they did right by you on Jenri Alpha."

            p "It wasn’t a luxurious life, but it wasn’t a miserable one."

            "Melancholy washes over me as a memory from my early teens comes flooding back."

            "A young Corsi, wide-eyed, excitable, and without nearly as many piercings, is helping me dig through a junkyard. Eventually, he says, we’ll find enough parts to build us a ship. Then we can go wherever we want."

            "But then I blink, and the moment of bittersweet nostalgia is gone."

            "Zeni must notice my upset, because he nods quietly and goes back to searching."

            z "I’m almost done here. You should check in with the others. Thanks for the chat."


        "Ask him why he joined security.":

            p "So, um, what made you go into a career in station security?"

            z "The pay. Plus I’m told I have an aptitude. Supposedly."

            "Zeni winks at me and flexes his arm."

            z "What do you think?"

            p "I think you’re full of yourself."

            z "Just a little."

            p "So you didn’t aspire to protect the innocent or something like that?"

            z "Maybe you have me confused with Governor Ceani."

            "He lets out a warm, deep laugh that’s soft on the ears."

            z "There {i}is{/i} someone I need to protect. But the only way I can protect her is by being here."

            p "What do you mean?"

            z "It’s complicated. What about you? Did you dream of flying transports back and forth?"

            p "Actually... yes. This guy I grew up with got me into scrappers and we..."

            "A few tears slide down my face without warning. I wipe them away quickly."

            z "...Oh."

            "Zeni seems to understand and accept my sudden wave of emotion, closing his eyes and giving a solemn nod."

            "For a moment, neither of us know what to say. The heavy weight of lost life bears down on our mundane conversation."

            z "Let’s focus on keeping ourselves alive for now. There will be time for everything else later."

            "Zeni points out a particularly large crate."

            z "Just this last one and I’m done. Can you help me drag it over?"

            "We heave both ends and finally get it open."

            z "Alright. Got it from here. You should check in with the others. Thanks for the chat."

    if chat_counter == 3:
        jump power_up
    else:
        jump choices



    # Return to choices, Zeni removed from options.



label help_misha:
    $talk_misha = True
    $chat_counter += 1

    "Of all the people in this room, the most likely one to find that power cell is probably the woman who made it."

    "I walk over to Misha’s corner of the room cautiously. She pays no attention to me as I approach."

    "On second thought... perhaps it’s more realistic to say that she doesn’t notice me because she’s too focused on her search."

    p "Hey, Misha...?"

    "Misha whips around and looks me up and down with slight confusion."

    m "What do you want? Did you find it?"

    p "No, I just wanted to ask you—"

    m "Waste someone else’s time if you don’t know what a fuel cell looks like."

    "If she would just let me talk..."

    p "I know what a fuel cell looks like. I’m a pilot."

    "That gets her attention. Misha stops, regarding me with interest."

    m "You’re a pilot? I suppose that explains why you’ve no fear of the auxiliary ships."

    p "Yes. And all I wanted to ask you was if you could use some help."

    "For some reason, Misha seems shocked that I would offer."

    m "Could you not find anywhere else to look, or are you simply frittering our final minutes away?"

    p "I don’t want to die any more than you do."

    m "Fine, then. I’m sure I could delegate the more... cumbersome items to you. Have at it."

    "She strides over and opens up a large set of lockers on the wall."

    m "My infuriating aides are very insistent that I store things in here."

    m "It’s very frustrating to find they’ve made a feeble attempt to categorize things without telling me."

    m "{i}The new guidelines say to organize by commission date instead of creation date, Dr. Ventai!{/i}"

    m "{i}You put a grismetal compound in the section for steel hybrids, Dr. Ventai!{/i}"

    "The tone she uses to imitate her research aides is whiny and mocking. I’d hate to be those guys."

    m "{i}Dr. Ventai! Dr. Ventai!{/i} I swear just hearing that makes me livid."

    "I’m not even quite sure what to say. I get the feeling I should just let her talk it out."

    "Misha walks along the wall, shining her light into each locker quickly in search of the precious prototype."

    m "Why can these bureaucrats not comprehend that these regulations only make my life exponentially more difficult?"

    m "And now, this organizational garbage is probably going to get me killed. Oh, the irony!"

    "Perhaps I’m misreading it, but I sense a lot of fear and tension bubbling below the surface of  Misha’s sarcastic rampage."

    "Maybe she just needs some help calming down."

    menu:
        with dissolve
        "Explain that organization would have solved this problem.":
            p "Misha, if you’d be willing to consider an idea..."

            m "Out with it, then. The seconds are drifting away."

            p "Maybe the organizational techniques might end up benefiting you if you didn’t fight back against your aides’ work."

            "Misha scowls at me, refusing to acknowledge my statement with more than a scoff. She closes her current locker with extra force, and it clangs shut."

            p "No, really; think about it. If you stepped back, let them organize the whole place, and adhered to the structure, you’d know where everything was all the time."

            m "I know where everything is when {i}I{/i} am the last to have handled it."

            p "But you can’t make everything alone, right?"

            "What was that word she used?"

            p "You need your... peons... to get everything done."

            p "And so letting them organize things might keep you both sane."

            "Misha crosses her arms, deep in thought. I must have passed some sort of test in her eyes, because her tone becomes warmer."

            m "You’re leagues wiser than I originally believed you would be. I respect that."

            m "That being said, hypothetical musings will not save our lives."

            "She closes the last locker gently, tucking her pen light into her bun."

            m "I am finished here. You may leave."

            "Misha doesn’t say another word, but her slight smile is good enough for me."
        "Offer to check the lockers while she takes a short break.":
            p "Misha, do you want to trade?"

            m "Trade?"

            p "Yes. I’ll search the lockers, and you can go through this storage unit I found."

            "Misha looks as though she’s trying to discern my ulterior motives. Finding nothing concrete, she merely pauses and holds out her pen light in my direction."

            m "Very well. I’d much prefer to be off my feet."

            "I stand up and start searching the lockers for the power cell."

            "Misha seems quite pleased to have escaped this task. She catches me eyeing her and quickly smiles before looking away again."

            "I close the last locker a few moments later. No luck."

            m "Thank you... [player_name], was it?"

            p "Yes. You’re welcome."

            "Misha doesn’t say another word, but her thanks is good enough for me."
    if chat_counter == 3:
        jump power_up
    else:
        jump choices



label help_aran:
    $talk_aran = True
    $chat_counter += 1

    "Aran seems to be the most pleasant of the bunch. I’ll go help him."

    "As I expected, Aran greets me graciously when I walk over to his part of the room."

    a "[player_name]. What can I do for you?"

    "His movements are graceful and effortless, and his smile radiates positive energy. Somehow or another, I find myself instinctively smiling in return."

    "Maybe it’s the inner cynic in me, but he’s just so sunny that I find myself wondering if he’s for real."

    "Either way, I have no particular reason to distrust him."

    p "Need some help? I’ve looked through all there was in the central island."

    a "Oh, of course, of course! Actually, if you’ll come over here..."

    "He subtly draws me forward with a little wave."

    a "Please forgive me for the facade. I’m afraid I must ask you for more than a little help."

    a "You see... I haven’t actually a clue what this device Misha speaks of looks like."

    "Wow. He’s serious. He’s been pretending to look all this time without even knowing what to look for? Why?!"

    "I stifle a giggle, and he looks very embarrassed."

    a "I am well aware of how foolish this may seem to you. Unfortunately, neither of those two ladies will so much as acknowledge my question."

    "Ah, that’s right. If I recall, Misha and Fera were yelling at Aran when I walked in."

    a "Those two are near impossible to placate. I know time is running out, and I fear doing anything that might set them at each other’s throats again."

    "I get it now. He had everyone split up into corners to stop the bickering. It’s quite wise in its own way."

    p "Why didn’t you just ask me?"

    "Aran scratches his head sheepishly."

    a "By the look on your face, I thought you were most likely in the same boat."

    "Is he saying I look stupid? No way. Right?"

    p "I’ll have you know, {i}Governor{/i}, I’m a pilot. And I do know what a power cell for a ship looks like. They’ve been standardized for 2 centuries."

    a "I’m sorry... I assure you I have no ill intent. Perhaps we could look together?"

    p "In the interest of time, let’s just do it this way. Grab me containers off that shelf over there and bring them over so I can look."

    a "If you’re certain that’s faster, then I can oblige."

    p "Trust me. It’s faster than explaining the fine details to you, and someone was going to have to carry the boxes anyway."

    "Aran smiles and does his dignified little bow again before walking over to the shelf."

    "Although I do question his motives (and in some cases, his intellect), he is extremely friendly and easy to be around."

    "I suppose it’s no small wonder he’s a politician."

    "Together we go through box after box and have a lively conversation."

    a "Where are you from, [player_name]?"

    p "Jenri Alpha."

    a "Ahhh, a beautiful colony. Shame about the pirate operations there."

    "Yep. That’s what Jenri is famous for. Beautiful landscapes and murderous pirates."

    "Back in the day, when were just kids in the dirt, we loved the pirates. They represented freedom. Dominion over sky and space."

    "Unfortunately, like most childhood idols, they weren’t all we imagined them to be. Just a fancy breed of violent criminal."

    p "Some day they’ll be driven out. Once people actually care enough."

    a "You’re a bit harsh with your words, but I agree. The law is unethically lenient towards career pirates."

    "Aran’s voice lowers to a strong whisper."

    a "If you want my opinion, off the record, I would say that {i}certain parties{/i} have a vested interest in the continued existence of pirates. And that needs to change."

    "Aran frowns before grabbing a particularly large box off the shelf. He staggers for a moment, shaking precariously."

    p "You alright?"

    a "Yes! I’ve... I’ve got it!"

    "After a few nerve-wracking moments, he sets the box down and sits across from me."

    a "This is the last one. While it’s not a good sign that we didn’t find it, I can’t thank you enough."

    p "You’re welcome."

    a "I hope you make it through this unharmed. I hope we all do."

    "He gives me a little wave as I get up and leave."

    if chat_counter == 3:
        jump power_up
    else:
        jump choices

label help_fera:
    $talk_fera = True
    $chat_counter += 1

    "Fera seems like she’s having trouble reaching the cabinets on her corner of the room."

    "While I have enough sense not to comment on that, it might be good to help her out."

    "She notices me before I call out to her."

    f "[player_name]. Hello."

    f "Do you need something? You must understand that I’m a bit busy."

    p "Actually, I thought I’d offer you an extra pair of hands."

    f "Well, far be it from me to turn down free labor."

    "Fera sits me down at a table covered with many small boxes and containers. Just how much crap does R&D have lying around? This is insane."

    f "While you make your way through that, humor me."

    p "Alright."

    f "You’re one of the new pilots, are you not?"

    "I’m quite surprised that she knows that."

    p "Yes. How do you...?"

    f "Every hiring decision on this station must pass my desk for approval."

    "Oh, yeah. That little fine detail about her basically owning this entire space station."

    f "Surely you do not see me as the negligent sort who would stamp them without reading."

    p "I have no opinions about you either way. I’ve just met you."

    p "Although I guess I should be thanking you for the opportunity."

    "An awkward silence descends before Fera laughs out loud."

    f "Thank you? For the opportunity?! What a fine thing to say, under such circumstances!"

    "She’s right. I might have lived a long life if I hadn’t been hired as a pilot on this station. Now... the future looks pretty dubious."

    p "Something’s bothering me, though."

    f "Hm? What would that be?"

    p "Why were you not evacuated immediately? I would think that would be a top priority."

    "For a moment, I sense a crackling wave of hostile intent coming from Fera’s direction. She did not like that question."

    "She leans in close, setting down the box she was searching for a quick moment."

    f "Someone in my position is ever a target. Do you believe for a second that the sensors conveniently failed by accident, and I was trapped in a lockdown room via pure bad luck?"

    p "Wait. You’re saying you think someone would destroy the space station... just to kill you?"

    "That’s insane."

    "Well... Maybe to a quadrillionaire, it’s not so insane."

    f "I only tell you this because I know you’re much too open-handed to be involved."

    f "But I firmly believe I was never intended to leave this space station alive."

    f "I need your help. There is no Zentri without me. No Mycia Beta. Remember that."

    "Fera plops one more box in front of me, but nearly as soon as she does, she grabs it again."

    "After a moment, she pulls out something bizarre and sets it on the table."

    "It’s a laser cutter gun. The kind used to open hulls for maintenance."

    p "What’s that doing in there?"

    f "I have no idea. But..."

    "It seems like Fera’s mind is running at warp speed."

    f "I’m.... going to hold onto this."

    "Oh, no. No. A weapon is the {i}last{/i} thing we need in this scenario."

    p "Fera. No. You don’t need that."

    f "Did you listen to anything I just told you? Yes, I do."

    p "None of us still in this room want to do anything but leave."

    p "If anyone sees that you have a weapon, there will be panic. Danger."

    p "Bad, bad idea."

    "Fera is not convinced."

    f "I believe it is I who decides what is acceptable and not acceptable here."

    "Fine. I have no choice then. I quickly reach forward and pull the charges out of the cutter, tossing them into a junk pile."

    f "H-How dare you?!"

    "She snarls quietly at me, trying not to attract attention."

    "After a moment, she sighs."

    f "You may be right. I guess it doesn’t matter now."

    p "Sorry I had to do that."

    f "Never apologize. It’s a sign of weakness."

    "Fera considers me quietly."

    f "You’re not as cowardly as the others. Very few would dare even call me by my first name."

    p "Thank you. I think."

    "Fera leans back in her chair, her voice purring and catlike."

    f "I find that foolhardy courage refreshing."

    f "If we do somehow live through this mess, I’m certain I could have a number of... uses for you."

    f "But we’ve wasted enough time. The power cell is not here. We need to move on."

    if chat_counter == 3:
        jump power_up
    else:
        jump choices





label power_up:

    "No one’s having any luck, and the mood in the room has started to get desperate."

    "Before, we were trying not to break things, but perhaps the ticking clock has given us some clarity."

    "All this stuff will be reduced to debris soon, anyway. At this point we’re all throwing things and ripping open boxes."

    $ renpy.sound.play("Alarm_Loop.ogg")

    show alarm

    ai "Warning: Catastrophic damage to multiple sectors detected."

    ai "Estimated time before asteroid storm reaches critical proximity: 23 minutes."

    hide alarm with dissolve

    stop sound

    "Just as the voice starts to fade, I hear a shout of triumph."

    m "Hah! I {i}knew{/i} it!"

    "Everyone scrambles to Misha’s side of the room."

    p "The fuel cell. We need to go, now."

    "There’s no time to celebrate. We have to install the core into a ship and board it immediately if we want to have any chance of survival."

    "For a brief moment, no one knows what to do next. Perhaps inspired by the crisis, Aran speaks up."

    a "What is the best plan of action from here?"

    z "We need to get to the auxiliary deck and install that core into a ship. But we also need to have someone deactivate the ship’s security from the next door command room."

    z "The ships all lock down after a failed attempt to prevent theft."

    z "Any volunteers?"

    "Everyone is silent. Even Misha and Fera aren’t volunteering."

    "I know the gist of how the security features work... but my job was to fly the ship. Not activate it."

    "I don’t know if I can do this. But it’s not like they’re leaving me any other options."

    p "Alright, fine. Listen to me. Fera, you told me you know the way to the auxiliary docks?"

    f "Correct."

    p "Take Zeni with you and get ready to power up the biggest ship you find in there."

    f "But how will we know where to put the core?"

    p "That’s why you’re taking Zeni. Between the two of you... figure it out, I guess."

    p "I’m going with Misha and Aran to the command room to take care of the security."

    p "Since I’m guessing no one else feels confident in their knowledge of fleet technology."

    "The room is filled with shaking heads. Guess that’s that."

    a "Alright. You heard what [player_name] said. Let’s all live through this. Go!"

    "Aran’s command is like a firecracker; everyone sprints in their respective directions."

    "I quickly dart over to the directory to confirm the command center’s location first."

    m "I sure hope they don’t mess this up."

    a "Misha, we have to believe in each other. Let’s focus on doing our part."

    "Misha rolls her eyes at Aran’s saccharine words, but she doesn’t argue as we head out the door."

    #[change bg hallway with asteroids]

    "We make our way into the hallway, running down it as fast as our legs can carry us."

    "The ship shakes and groans from damage. Emergency lights are on in multiple places. This is life or death. I steel myself to run even faster."

    "We close in on the command room and dart through the door."

    "Looking out onto the vastness of Mycia Beta, I feel a renewed will to survive."

    "Maybe we can do this."

    "There are no comms at this point anymore. We just have to hope they figure it out."

    "I suppose it’s at least a small comfort to know that they can’t just decide to leave without us. The ships won’t activate without a biochipped pilot in the seat."

    m "Over here! This is the console."

    "All three of us huddle around the console."

    "There are three workable ships: a 10-person transport ship, a 4-person escort ship, and a 2-seater reconnaissance ship."

    a "Perfect! The transport ship can take everyone!"
    "This is the best possible outcome. All I need to do is remove the security."

    "Then the locks on the ship will release, the deployment alert will sound, and Zeni and Fera will know which ship to power up."

    "Alright. No time like the present."

    #[downer puzzle that you can’t win]

    hide zeni
    hide misha
    hide fera
    hide aran
    window hide
    with dissolve

    $ num_active = 0
    $turn_on(seeds3[0])

    $timedout = renpy.call_screen("pipeline_puzzle", seeds3, tasks3, 180)
    if timedout != "timeout":
        "...Nothing happens."

    play music mus_puzzle fadeout 3 fadein 3

    show misha frown at right, parallaxed_m
    show aran frown sad at cright, parallaxed_a
    m "There’s no way we can get through this in time."

    "She’s right. Damn it! I pound my fist against the side of the console."

    m "We have to try the escort ship."

    a "No! We’re not leaving people to die!"

    m "We don’t have a choice, you imbecile!"

    p "Shut up, both of you!"

    "I need to think. I have to focus on what I remember about this..."


    #Puzzle for 4 person ship

    hide zeni
    hide misha
    hide fera
    hide aran
    window hide
    with dissolve

    $num_active = 0
    $turn_on(seeds2[0])

    $activation_success = renpy.call_screen("pipeline_puzzle", seeds2, tasks2)()


    if activation_success == True:
        $one_death = True
        jump vessel_activated

    else:
        pass

    #[puzzle for 4 man ship]

    #If success 🡆 1 PERSON LEFT BEHIND ENDINGS

    #If fail
        show misha angry open_neutral eyes_wide at left, parallaxed_m with moveinleft

        m "What happened?! What did you just do?!"

        show aran scared at right, parallaxed_a

        with moveinright

        "No. No, no, no, no."

        p "The... The anti-theft lockdown engaged. It’s over. We’re not getting on that ship."

        "This is bad. This is really bad. How could I screw up like this?"

        "Six save me. All that’s left is the reconnaissance ship."

        "I no longer have the luxury of failure if I want to live. Let alone save anyone else."

        "This is my last chance."

        hide zeni
        hide misha
        hide fera
        hide aran
        with dissolve

        $num_active = 0
        $turn_on(seeds1[0])

        $activation_success = renpy.call_screen("pipeline_puzzle", seeds1, tasks1)()



        if activation_success == True:
            jump vessel_activated

        else:

            jump ultra_fail

    #[puzzle for 2 man ship]

    #If success 🡆 3 PEOPLE LEFT BEHIND ENDINGS

    #If fail 🡆 BAD ENDING
