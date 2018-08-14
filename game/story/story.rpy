# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define mus_start = "music/01_weirder_things_instrumental.mp3"
define mus_build = "music/02_illuminate_instrumental.mp3"
define mus_sad = "<to 100>music/06_the_attic_instrumental.mp3"
define mus_relax = "music/03_blue_hue_instrumental.mp3"
define mus_puzzle = "music/04_runner_instrumental.mp3"
define mus_tense = "<from 30>music/05_the_seeds_of_unrest_instrumental.mp3"
define mus_escape = "music/07_like_an_angel_instrumental.mp3"


define p = Character("[player_name]")
python:
    player_name = renpy.input("Please enter your name.")
    player_name = player_name.strip()

define c = Character("Corsi")
define ai = Character("Zentri AI")
define m = Character("[misha_name]", color ="#f7e", image="misha")
define z = Character("[zeni_name]", color="#78f", image="zeni")
define f = Character("[fera_name]", color="#f7b", image="fera")
define a = Character("[aran_name]", color="#7ff", image="aran")
default misha_name = "...?"
default zeni_name = "...?"
default fera_name = "...?"
default aran_name = "...?"
default player_name = "Kestri"

default zeni_met = False

default chat_counter = 0
default talk_zeni = False
default talk_misha = False
default talk_aran = False
default talk_fera = False

default one_death = False
default activation_success = False
default survivor = None


# The game starts here.

label story:

    #[show secure sublevel hall bg]

    stop music fadeout 2
    python:
        player_name = renpy.input("Please enter your name.")
        player_name = player_name.strip()


    if not player_name:
         $player_name = "Serin"
    #[play crackle sound]

    call setup_sublevel(dissolve)
    pause (1)

    show screen freak_parent

    c "{i}Where are you now?{/i}"
    with dissolve

    #[fade in tense music]
    $ renpy.music.set_volume(.3)
    play music mus_tense fadein 2
    p"I’m on my way. I’m on Sublevel B, Section, um..."

    "I pause and look around, hoping to regain my bearings. I’ve been running for so long that every breath hurts, and it’s hard to read the walls."

    p "Four. I’m in Section Four."

    c "{i}You’ve gotta hurry! Almost everyone has boarded already.{/i}"

    p"I know! I’m going!"

    c "{i}We have a pilot shortage as-is, so for the Light of the Six, get yourself here NOW!{/i}"

    "Easy for Corsi to say. He’s not the one sprinting all the way from the other side of the station."

    p"Huff, huff, huff..."

    "I swipe my wrist against the door panel as I approach. For some reason, it doesn’t open."

    p"What?!"

    "I’m so taken by surprise that I nearly crash head-on into the metal door."

    "This isn’t good. I know that I have clearance for the whole sublevel."

    "I swipe my wrist against the door panel again."

    "Nothing happens."

    p"Corsi?!"

    c "{i}What now?{/i}"

    p"We have a big problem!"

    c "{i}A problem? What kind of problem? Oh, hang on—{/i}"

    "He mutes me. Rude."

    c "{i}Yes, we’re waiting on two pilots and six VIPs.{/i}"

    c "{i}No, I don’t know how much longer!{/i}"

    "It’s obvious that last bit wasn’t meant for me. I can hear others shouting through his relay."

    "I almost feel bad for him. Neither of us were trained for leadership."

    "After another moment, he unmutes me and continues speaking."

    c "{i}Sorry. Problem?{/i}"

    p"The door to Section Five isn’t opening!"

    c "{i}You’ve gotta be kidding me.{/i}"

    p "Not at a time like this, I promise!"

    c "{i}Okay. Hold on. There’s gotta be another way to the hangar.{/i}"

    c "{i}Jasara! Need you over here!{/i}"

    "I don’t know who Jasara is, but I sure hope that they can help."

    c "{i}I’m working on it. Be right back.{/i}"

    "He doesn’t wait for me to reply before closing the comm relay."

    $ renpy.sound.play("Alarm_Loop.ogg")

    show alarm

    ai"Warning: Multiple asteroid impacts detected."

    ai"Immediate evacuation of all personnel is required."

    ai"Estimated time before asteroid storm reaches critical proximity: 49 minutes."

    hide alarm with dissolve

    stop sound

    "That’s comforting. Good to know that my last moments might be spent listening to the Zentri's system AI counting down the minutes until we all die."

    "Every second I spend waiting for Corsi to contact me is agonizing. I begin to pace, not knowing what else to do."

    "I still can’t believe this is happening. The sensors should have picked up the storm long before it came into collision range."

    "I can’t die here. I won’t."

    "I stand still and try to take deep breaths. I’m going to need my energy for a while longer."

    c "{i}[player_name]! Got another route for you!{/i}"

    p"Where to?"

    c "{i}If you turn around and go back through Section Three, there’s a—{/i}"

    "Corsi goes silent suddenly."

    c "{i}...We’re too late.{/i}"

    "The tone of his voice is flat and defeated. I can hear a touch of disbelief, too."

    p"Too late for what?"

    c "{i}Listen to me! Forget the main hangar! Go to the auxiliary dock! The one they use for surveillance jobs!{/i}"

    p"What do you mean? What’s going on?!"

    c "{i}Don’t you go and die! You hear me? You can’t die!{/i}"

    play sound "Asteroid_Impact_Louder.ogg"

    "An earsplitting crash sounds through Corsi’s relay."

    "After that, the feed drops... along with the pit of my stomach."

    stop music fadeout 6

    p"Corsi? Corsi?!"

    "He’s unreachable. What the...?"

    $ renpy.sound.play("Alarm_Loop.ogg")

    show alarm

    ai"Warning: Catastrophic damage to hangar bay detected."

    ai"Evacuation of all personnel is no longer possible."

    ai"Estimated time before asteroid storm reaches critical proximity: 44 minutes."

    hide alarm with dissolve

    stop sound

    p"No. No way."

    "Corsi... The hangar... All the evacuees..."

    "My body feels numb, the truth trickling slowly into my exhausted mind."

    "What little time I have left feels like it’s flowing at a quarter of the speed."

    p"Six save me… They’re all dead..."

    play music "<from 10>"+mus_build fadeout 3 fadein 2

    "And if I don’t figure something out quickly, I’ll be dead too."

    "There’s no time to mourn right now. The auxiliary dock... Corsi mentioned the auxiliary dock."

    "I need to go to the floor level. I have no idea how to navigate from here."

    "I search for the nearest set of stairs and run up them with as much speed as I can muster."

    #[show hallway bg]
    call setup_hallway(fade)

    "Finally, I see a sign. It looks like I’m at the Life Support Center."

    "Not too far ahead of me is the Research & Development section."

    "Behind me is Maintenance."

    "The one thing I can’t find is a map. I have no clue where the auxiliary dock is in relation to where I am."

    "No other options. I need to start looking for directions, and fast."

    "But where should I start?"

    menu:
        with dissolve
        "Life Support Center":
                p"Might as well go with the closest."

                "I hurry over to the door of the Life Support Center."

                p"Good thing everything’s fine here."

                p"...I just jinxed it, didn’t I?"

                "My accidental prophecy comes true. When I scan my wrist on the panel, I see a message flash across it: Insufficient Clearance Level. Level A Required."

                "I guess it's not really a surprise that I don't have clearance for this. One screwup in there could suffocate everyone on board."

                "There’s no way I’m getting in here. Time to try somewhere else."

                menu:
                    with dissolve
                    "Maintenance Center":
                        jump maintenence_center

                    "Research & Development Hub":
                        jump r_and_d

        "Maintenance Center":
            jump maintenence_center

        "Research & Development Hub":
            jump r_and_d



label maintenence_center:

    $zeni_met = True

    p"Maintenance seems like a safe bet."

    "Turning around, I walk towards the door for the Maintenance Center."

    "Before I reach it, though, I notice something slumped against the wall."

    "Wait... That’s not a some{i}thing{/i}. That’s a some{i}one!{/i}"

    "I dash to the person’s side. It’s a man in a security uniform. He’s not dead... I think."

    p"Hey! You okay?!"
    show zeni eyes_rest concern neutral at leftish_zeni, parallaxed_z
    with dissolve

    show zeni eyes_rest concern neutral
    "Sure enough, the man stirs to life at the sound of my voice. He clutches his head and replies groggily."
    show zeni eyes_squint raised part_neutral
    z"I’m... I’m fine... what?"
    show zeni scared neutral
    "He looks around, confused."

    p"Are you completely insane?! Why are you here?"
    show zeni part_neutral
    z"Where is... here?"
    show zeni neutral
    "Great. This guy appears to be short a few bolts."

    p"We’re near the Maintenance Center. But we don’t have time for pleasantries!"

    "Perhaps the sounds of the asteroids bombarding the station finally snap him out of his stupor, because he stands up and stares at me, wide-eyed."
    show zeni eyes_wide raised open_neutral
    z"I was... Oh, no. It’s gotten worse. How long was I out?"
    show zeni neutral concern eyes_open
    p"Like I have any clue?! Come on. We have to go!"

    "I grab his arm and start pulling him in the direction of the door, but he resists me with very little effort. He points in the opposite direction."
    show zeni scared eyes_narrow part_frown
    z"The hangar is the other way."
    show zeni frown
    "I stifle a sigh. I was trying to block that out of my mind."

    p"There is no more hangar."
    show zeni eyes_wide raised part_neutral
    z"...Oh."
    show zeni part_frown eyes_rest angry
    "He doubles over, holding his head again. Maybe he’s injured? Even if he is, there’s nothing I can do to help him."

    z"I must have gotten knocked out somehow..."
    show zeni eyes_squint scared look_away
    z"Anyway... um... if there’s no more hangar, aren’t we...?"
    show zeni frown
    "He doesn’t actually say the word ‘doomed’, but I can infer it from his tone."
    show zeni look_at
    p"Not yet. I’m heading for the auxiliary dock. There should be some small ships there."
    show zeni eyes_open raised part_neutral
    z"Good idea. Smart. Where do we go?"
    show zeni neutral
    p"Well, um, I don’t actually... know where it is..."
    show zeni look_away scared eyes_narrow
    z"...Oh."

    p"I’m hoping there’s a directory in Maintenance."
    show zeni eyes_open frown concern
    z"Yeah... you uh, you don’t wanna go in there."

    p"What do you mean?"
    show zeni look_at scared
    z"I was in there. Earlier. Bad electrical accident."

    "His tone becomes serious and thoughtful."
    show zeni eyes_rest
    z"Someone accidentally severed the energy coil to the sensor system. Sparks everywhere."
    show zeni eyes_narrow look_away neutral
    "Well, that means Maintenance is out of the question."

    "But anyway, what is with this guy? How is he so calm? I envy his composure, but at the same time, I’m also wondering if he truly realizes how much danger we’re in."

    p"Okay. Then we need to go somewhere else."
    show zeni look_at concern part_neutral eyes_open
    z"R&D should have a directory. Yeah."
    show zeni neutral
    "He nods sagely. I guess he’s pretty confident about that assertion."

    p"Good enough for me."
    show zeni eyes_narrow raised
    z"I’m coming with you."

    p"I assume you weren’t planning on staying!"
    show zeni scared look_away eyes_squint smile
    z"Sorry. Still getting my bearings. Let’s go. My name is Zeni, by the way."
    $zeni_name = "Zeni"

    p"[player_name]. We should hurry."

    "We walk briskly down the hall towards the Research & Development Hub."

    jump argument

label r_and_d:

    p"I’ll just go with the Research & Development Hub, then." with dissolve

    "Continuing down the hall, I arrive quickly in front of the door to the R&D Hub."

    jump argument

label argument:

    "To my surprise, I hear what sounds like arguing."

    f "I don’t think you’re taking this even remotely seriously enough."

    m "I heard your opinion the first time. Perhaps you think you can do better?"

    m "It’s not my fault I’m stuck with imbeciles for staff. Do you really think I designed the infernal thing? No! Of course not!"

    a "Ladies! Ladies! We need to calm down. Time is of the essence. Let’s put this aside and work together."

    f "Shut up!{nw}"

    m "Shut up!"

    "There are definitely people still alive in there. And from the sound of it, they’re stuck."

    if zeni_met == False:

        "I look at the door panel. Sure enough, it says Emergency Lockdown."

        "Someone must have triggered it by accident..."

        "This is bad. Lockdown means no one can go in or out. They’ll die in there if I don’t do something."

        "But what can I do? I certainly don’t know of a way to lift the lockdown..."

        "All of a sudden, a voice calls out to me."

        z"Hey! You over there!"
        show zeni at leftish_zeni, parallaxed_z with moveinleft
        "A man in a security uniform runs up to me."
        show zeni angry frown
        z"What are you doing? You should be evacuating."

        p"Didn’t you hear? The hangar was destroyed."

        "He stops dead in his tracks."
        show zeni eyes_wide raised
        z"Wait, what?"

        p"How did you not hear the…? Nevermind. There’s no time for questions. I need your help."

        "That security uniform means he might have the ability to override this door. I hope."

        z"Help?"

        p"Yes, help. There are people trapped in this room. It’s on lockdown, and I can’t open it."

        show zeni eyes_narrow original neutral

        "He stops for a minute to think."

        show zeni eyes_wide relax

        z"...Oh. Oh!"

        z"I can fix that. Let me see."

        p"Please. We don’t have much time."

        "The security guy gently nudges me out of the way to mess with the panel. After a moment, the door opens. Both of us hurry into the room."

    else:

        "I look at the door panel. Sure enough, it says Emergency Lockdown."

        "Someone must have triggered it by accident..."

        "This is bad. Lockdown means no one can go in or out. They’ll die in there if I don’t do something."

        p"Zeni! There are people in here!"

        show zeni eyes_wide frown look_at

        z"What? Why didn’t they evacuate?"

        "Zeni walks up beside me to investigate the door."

        p"The door’s on lockdown. I can’t open it."

        show zeni eyes_wide concern

        z"Lockdown? Why?... Doesn’t matter. Let me see."

        "I step aside so Zeni can mess with the panel. After a moment, the door opens."

        show zeni eyes_open smile relax

        z"Tada!"

        p"Nice work."

        "I dash into the room, Zeni on my heels."



    #[fade in chill theme]
    call setup_rd_room(dissolve)

    show fera eyes_wide raised open_neutral at center,flipped, parallaxed_f
    show aran eyes_wide raised open_neutral at mid_right, flipped, parallaxed_a
    show misha eyes_wide concern open_neutral at rightish, flipped, parallaxed_m
    with dissolve

    pause 0.7

    show fera eyes_open relax part_smirk
    show aran eyes_open relax smile
    show misha eyes_open relax smile
    with dissolve

    "Three shocked faces stare back at us before their expressions melt into relief."

    a"Look! We’re saved, see?"

    "The friendly-looking man strides forward to greet us. He seems familiar, but I don’t know where I’ve seen him before."

    a"Thank you so much for opening that door. We were in quite some trouble."

    show aran part_smile
    a"Ah, my manners! My name is Aran. Aran Ceani, governor-elect of the Saru Territories."
    $aran_name = "Aran"

    "A governor? That explains the familiar face."

    show aran eyes_rest original
    "He gives a dignified bow. I feel flattered but also a bit awkward."
    show aran eyes_open

    p"My name is [player_name] Kestri. You’re welcome, but we need to hurry."

    a"Oh, yes. Ah..."

    show misha look_away angry frown
    "As Aran looks around nervously, the tall woman in the lab coat taps her foot angrily and speaks."

    show misha one_raised
    m"Hurry for what reason? Should we not have an extravagant dinner while we wait patiently for our end?"

    show fera one_raised frown eyes_narrow
    f"Not a single plan to get us out of here, but you’re cracking jokes?"

    show fera angry
    show misha angry look_at
    "The two women scowl at each other. I do not want any part of that."

    p"Okay, okay. Look. I don’t know what happened here, but it doesn’t matter. As you know, the hangar is done for."

    p"The only ships left on the station are at the auxiliary dock. Anyone know where that is?"

    show fera look_away concern neutral
    "The short woman’s face becomes thoughtful."

    f"So you’re thinking we can still get out of here after all?"

    p"Yes. If we can get there in time."
    show fera part_smile original look_at
    f"Well, then. I can show us to the docks if you have a plan."

    show misha eyes_narrow
    "The woman in the lab coat snorts derisively."

    m"Aren’t you gregarious all of a sudden?"

    "The short woman pays no heed to the insult, thoughtfully curling a strand of her voluminous ponytail between her fingertips instead."

    show zeni concern frown look_away at leftish_zeni, parallaxed_z with dissolve
    z"Uh, everyone?"

    show misha eyes_squint
    m"Who’s this... peon?"

    show zeni one_raised
    z"Misha, we’ve met at least 4 times..."

    "I’ll take that to mean that the woman in the lab coat’s name is Misha."
    $misha_name = "Misha"

    show misha eyes_open frown original
    m"Is that so? Hmm."

    show fera smile look_away raised
    f"Ah, I recognize you. Zeni Taro, right? Vice President of Security?"
    $zeni_name = "Zeni"

    show zeni neutral
    z"That’s me. Although I don’t think I know you."

    show fera neutral
    f"Fera Mycia. Charmed, I’m sure, though you’ll forgive me if we forgo the rest."
    $fera_name = "Fera"

    p"Wait. Mycia as in the colony?"

    show fera smirk
    f"Very good. Yes. My... organization... is the proprietor of Mycia Beta’s colonization efforts."

    "Wow. This is kind of terrifying. A governor is one thing, but... this woman is one of the richest people in our solar system."

    show zeni concern frown look_at
    z"Anyway, now that we’re all friends, I have bad news."

    m"What could possibly be worse news at this stage?"

    show zeni part_frown
    z"Um... before this happened, I was overseeing Maintenance."

    show fera eyes_narrow one_raised neutral
    f"And...?"

    show zeni eyes_squint
    z"They were removing the power cores from the ships in the auxiliary dock. For refueling."

    #[fade out music to silence]
    stop music fadeout 3.0

    show aran eyes_wide
    show fera eyes_wide part_neutral
    show misha eyes_wide part_neutral

    "Everyone falls silent."

    show zeni look_away
    z"After that, there was an accident in Maintenance. There’s no way they had time to finish the refueling."

    show zeni frown one_raised
    z"Maintenance also happens to be very, um, electrifying right now."

    p"So... you’re saying the ships have no power."

    "He slumps his shoulders and leans against a nearby wall."

    show zeni concern eyes_narrow
    z"None."

    p"No... That’s..."

    show fera eyes_narrow angry part_frown
    show misha eyes_wide frown look_away
    show aran eyes_narrow concern part_frown
    f"Unbelievable... Of all the Six-forsaken hellholes to die on...!"

    "Fera is livid. She lashes out at the nearest object—which happens to be a steel table leg. My foot throbs just from watching her, but Fera just gives the table a look of furious disgust."

    "Aran is pacing nervously, but Misha is standing perfectly still, brows furrowed and arms crossed."

    "Pausing with a deep breath, Aran tries his best to comfort the group."

    show aran eyes_open neutral concern
    a"Surely there is something we can do. We must not give up."

    z"Wish I shared your optimism, Governor."

    show aran smile original
    a"Please call me Aran. There is no need for formalities in a situation so dire."

    f"As if it matters what he calls you? We’re all going to be dead soon anyway."

    "A depressing hush falls over the group."

    "Misha, who has been quiet for some time, suddenly breaks the silence."

    play music "<from 10>"+mus_build fadeout 3 fadein 2

    show misha eyes_open original part_neutral look_at
    m"Maybe we won’t be."

    f"Oh, {i}now{/i} you have an idea?"

    show misha angry eyes_narrow
    m"Be silent, you vile woman. I’m sorry that all that money can’t buy you a personality."

    show fera part_smirk
    f"It sure can buy you, though."

    "Fera’s purring voice seems to intimidate Misha, because she drops her nasty attitude somewhat."

    show misha eyes_open neutral original
    m"Ahem. I provided a client with a new fuel cell schematic about two weeks ago."

    show fera eyes_wide part_neutral original
    show aran eyes_wide smile
    show zeni eyes_wide relax smile look_at

    "Eyes light up cautiously around the room."

    m"I am quite sure that the demonstration prototype remains somewhere in this hub. That being said..."

    "She pauses and starts tapping her foot again in anger."

    show misha angry
    m"No one ever thinks to ask my leave before moving my masterpieces. So you’ll need to look for it."

    show zeni smile original
    z"You don’t have to tell me twice!"

    hide zeni with dissolve

    "Zeni begins digging through shelves and containers with fervor, his previous lackadaisical attitude fading away in the face of hope for survival."

    show fera one_raised part_neutral
    f"This isn’t exactly what I had on my agenda for today, but oh well..."

    hide fera with dissolve

    p"Well, that settles it. We need that power cell. Everyone, split up."

    show aran angry neutral eyes_narrow
    "Misha leans against a table while everyone else gets to work, but a commanding glare from Aran motivates her to join in."

    hide aran with dissolve
    hide misha with dissolve

    "Just as we begin, a familiar yet unwelcome sound graces our ears."

    $ renpy.sound.play("Alarm_Loop.ogg")

    show alarm

    ai"Warning: Catastrophic damage to multiple sectors detected."

    ai"Estimated time before asteroid storm reaches critical proximity: 30 minutes."

    "As it stands, there is one person for each corner of the room. I find myself milling around, not sure where to go."

    hide alarm with dissolve

    stop sound

    "I should just go help someone with their share. Who should I talk to?"

    play music "<from 15>"+mus_relax fadeout 3 fadein 5

    jump choices

    #Choice:
    #Help Zeni
    #Help Misha
    #Help Aran
    #Help Fera



    return
