
label vessel_activated:

    "The security screen clicks, changing to show the words Vessel Activated."
    show aran eyes_open look_at raised part_smile
    show misha eyes_open look_at raised part_smile
    a "Yes! You did it! Amazing!"

    "Aran and Misha are practically cheering."

    p "Yeaaaaah!"
    show aran eyes_open smile relax
    show misha eyes_open neutral
    "There isn’t too much time to celebrate."

    p "Okay, we have to go to the ship, right away."

    #[play alarm sound]

    #[display red light fade]
    show aran look_away eyes_wide raised part_frown
    show misha look_away eyes_narrow angry part_frown
    ai "Warning: Catastrophic damage to multiple sectors detected."

    ai "Warning: Life support systems are offline."

    ai "Oxygen levels at: 98\%. Time until depletion: 6 minutes."

    "The life support?! Oh, no. We {i}really{/i} have to go now."
    show misha eyes_rest frown
    m "At least suffocating might be a better death than being crushed by debris."
    show misha eyes_narrow look_at
    show aran look_at eyes_open scared frown
    "Misha makes a quiet and cold point as I open the gate between the control room and launch dock."
    show zeni  part_smile eyes_open raised at leftish_zeni, parallaxed with easeinleft
    show fera neutral raised
    "As soon as the doors open, I see Zeni jump down from the back panel of the ship. He flashes me a double thumbs up."

    z "It’s in! We need to board, right now!"

    if one_death == False:
        f "Isn’t this ship a little small...?"

    p "Wait."
    show fera angry eyes_narrow frown
    show zeni one_raised neutral
    "My voice is pained, and everyone looks my way."

    "Misha and Aran know the score, but Zeni and Fera don’t. I don’t have time to phrase it gently..."

    play music mus_tense fadeout 3 fadein 3

    p "Before we go, I..."

    p "The ship won’t fly unless I’m in it. So until we’re out of here, I’m in charge, got it?"
    show zeni frown concern
    z "Sure, but can’t this wait?"

    p "No. Because..."

    if one_death == True:
        jump one_left
    else:
        jump three_left


label one_left:
    menu:
        "...Zeni has to stay behind.":
            jump zeni_lost
        "...Misha has to stay behind.":
            jump misha_lost
        "...Aran has to stay behind.":
            jump aran_lost
        "...Fera has to stay behind.":
            jump fera_lost

    label zeni_lost:

        show zeni scared part_frown eyes_wide
        z "What...? No. No! What do you mean, stay behind?!"

        z "I’ll die!"

        show black with fade

        "I close my eyes bitterly. I can’t bring myself to tell him why. The truth is, I’m being pragmatic. Zeni is the only person here who doesn’t serve an irreplaceable purpose."

        "It’s not like knowing my reason might be justified makes this any easier."

        hide black with fade

        p "Zeni... I’m sorry. The ship I activated can only fit a pilot and 3 passengers..."

        z "But why me?!"
        show zeni eyes_narrow angry frown
        z "...I get it."
        show zeni eyes_squint
        z "My life’s not worth as much as these guys, is that right?"

        "Zeni spits on the ground."

        z "I misjudged you. You’re much more cold-hearted than you look."

        "He crosses his arms and starts to yell."

        z "And when pirates come to loot the colony while comms are down, who’s going to protect you?!"

        z "{i}Huh?{/i} These spoiled brats?!"

        "I wish I could talk to him and make him okay with this. But we have less than 3 minutes left."

        p "Zeni... I’m sorry. I won’t ask you to forgive me."

        "Zeni points a finger at Fera."

        z "If you care at all about atoning for this, you will {i}take care of my daughter.{/i}"

        z "Racia Taro. I was all she had. Protect her, or I swear I’ll come back from the dead."

        "We board the ship without another word. Zeni sits down on the ground, looking numb and confused. As the ship closes, he breaks down into sobbing."
        jump final_escape

    label misha_lost:
        m "Absolutely not! How dare you even suggest that?!"

        m "You need me. The colony needs me."

        "I close my eyes bitterly. I can’t bring myself to tell her why. The truth is, I’m being pragmatic. Misha is a genius, but there is little use for yet another scientist on the surface."

        "It’s not like knowing my reason might be justified makes this any easier."

        p "Misha... I’m sorry. The ship I activated can only fit a pilot and 3 passengers..."

        m "Are you an imbecile? Why not leave someone else?"

        m "You would truly take this meat-for-brains over me?"

        "Zeni glares daggers at her."

        m "I can’t believe this. You don’t get the right to do this."

        "She stomps her foot and starts to yell."

        m "All of my tech was destroyed! Do you think colonies run without power?! They don’t. Good luck solving the energy crisis with these morons."

        "I wish I could talk to her and make her okay with this. But we have less than 3 minutes left."

        p "Misha... I’m sorry. I won’t ask you to forgive me."

        "Misha points a finger at me."

        m "I’ll haunt you until the day you die, you monster."

        "We board the ship without another word. Misha paces back and forth on the ground, looking shocked and betrayed. As the ship closes, she screams, falling to her knees in despair."
        jump final_escape

    label aran_lost:

        a "Is that how it is...?"

        "Aran crosses his arms quietly, resigning himself to the end."

        "I close my eyes bitterly. I can’t bring myself to tell him why. The truth is, I’m being pragmatic. Aran might be essential in his jurisdiction, but here..."

        "It’s not like knowing my reason might be justified makes this any easier."

        p "Aran... I’m sorry. The ship I activated can only fit a pilot and 3 passengers..."

        a "So it was to be me after all. I will admit that I expected this to happen..."

        "The fact that Aran is taking this so well makes it even more painful."

        "He uncrosses his arms and starts to mumble to himself."

        a "Someone like me is not as valuable as a scientist... or a quadrillionaire. I understand... I simply hope you have what it takes to maintain order once the colonists realize they’re all alone..."

        "I wish I could talk to him and make him okay with this. But we have less than 3 minutes left."

        p "Aran... I’m sorry. I won’t ask you to forgive me."

        a "But I do forgive you. Now go."

        "We board the ship without another word. Aran stands straight up, looking resigned and resolute. As the ship closes, he only watches silently, his hand to his chest in a farewell prayer."
        jump final_escape

    label fera_lost:

        f "Are you out of your mind?!"

        "Fera spits venom at me as soon as the words leave my mouth."

        f "Did you forget {i}who I am?!{/i}"

        "I close my eyes bitterly. I can’t bring myself to tell her why. The truth is, I’m being pragmatic. Fera’s organization may be funding the colony, but they will choose another executive if she dies."

        "It’s not like knowing my reason might be justified makes this any easier."

        p "Fera... I’m sorry. The ship I activated can only fit a pilot and 3 passengers..."

        f "No! You can’t leave me behind! This is {i}my station{/i}! My {i}colony{/i}!"

        if talk_fera == False:

            "Fera's eyes narrow, a cruel smile breaking over her face."

            "Seconds later, she whips out a laser cutter."

            a "Where did you get that?!"

            f "If I don’t leave? {i}No one does.{/i}"

            "She points the laser cutter straight at my chest and squeezes the trigger."

            "I close my eyes and brace myself reflexively, but I feel no pain."

            a "Arrgh!"

            "Instead, Aran jumps out in front of me, crying out in agony as the smell of seared flesh fills the room."

            "He saved me. Aran just saved my life."

            "With the last of his strength, Aran tackles Fera to the ground."

            f "Get off me, you disgusting do-gooder! {i}Get off!{/i}"

            a "Go. Go now!"

            "His voice is weak. I can see his life force fading away as he begs us to leave."

            "We board the ship without another word. Aran holds Fera to the ground, his grip slackening as the ship door closes. Fera shoves his limp form aside and screams her hatred at us until we’re out of sight."

        else:
            "A realization dawns across Fera’s face, and she points accusingly at me."

            f "Was this your intention all along? I can’t believe this! I {i}trusted{/i} you!"

            f "{i}Don’t take the gun, Fera! You’ll be just fine, Fera!{/i}"

            f "You made me defenseless on purpose. You thorny little viper."

            "I wish I could talk to her and make her okay with this. But we have less than 3 minutes left."

            p "Fera... I’m sorry. I didn’t know this would happen."

            p "I won’t ask you to forgive me."

            f "{i}Forgive you?!{/i} I hope you get impaled by shrapnel and die a slow... agonizing... death."

            "Her bitter words are like dripping acid."

            "We board the ship without another word. Fera screams her hatred at us until we’re out of sight."
        jump final_escape

label three_left:

    menu:
        "...Only Zeni can come with me.":
            jump zeni_lives
        "...Only Misha can come with me.":
            jump misha_lives
        "...Only Aran can come with me.":
            jump aran_lives
        "...Only Fera can come with me.":
            jump fera_lives

label zeni_lives:

    $survivor = "Zeni"

    f "What do you mean, only Zeni?!"

    "Everyone is confused and dismayed. Even Zeni looks surprised beneath his relief."

    a "The ship is... too small..."

    m "But why would you pick Zeni?!"

    f "Clearly you’ve gone nuts. You’re really gonna leave us all here and take that nobody?"

    z "Okay, that’s enough."

    "Misha laughs mockingly at Fera."

    m "Maybe this is your karma for being such an evil bitch."

    "Aran is the only one who remains quiet. He drops to his knee in prayer, then addresses me softly."

    a "If this is the only way, then so be it..."

    "I close my eyes bitterly. I can’t bring myself to say anything to everyone."

    "How can I possibly explain to three people why I’m leaving them to die?"

    "How do I tell them that this is my fault? That my incompetence doomed two more people to certain death...? If only I could do this over again..."

    p "Everyone... I’m sorry. The ship I activated can only fit a pilot and 1 passenger..."

    "I wish I could talk to them and make them okay with this. But we have less than 3 minutes left."

    p "This is my fault... I’m so sorry. I won’t ask any of you to forgive me."

    "Zeni softly taps my shoulder as the three others begin to accept their fate with a combination of reflection, weeping, and fury."

    z "We should go."

    jump final_escape


label misha_lives:

    $survivor = "Misha"

    f "What do you mean, only Misha?!"

    "Everyone is confused and dismayed. Misha smiles arrogantly, but her shoulders slump in relief."

    a "The ship is... too small..."

    z "But my little girl... No! Please no!"

    f "Clearly you’ve gone nuts. You’re really gonna leave us all here and take *her*?"

    "Misha laughs mockingly at Fera, crossing her arms triumphantly."

    m "Maybe this is your karma for being such an evil bitch."

    "Aran is the only one who remains quiet. He drops to his knee in prayer, then addresses me softly."

    a "If this is the only way, then so be it..."

    "I close my eyes bitterly. I can’t bring myself to say anything to everyone."

    "How can I possibly explain to three people why I’m leaving them to die?"

    "How do I tell them that this is my fault? That my incompetence doomed two more people to certain death...? If only I could do this over again..."

    p "Everyone... I’m sorry. The ship I activated can only fit a pilot and 1 passenger..."

    "I wish I could talk to them and make them okay with this. But we have less than 3 minutes left."

    p "This is my fault... I’m so sorry. I won’t ask any of you to forgive me."

    "Misha walks briskly towards the ship as the three others begin to accept their fate with a combination of reflection, weeping, and fury."

    m "We haven’t time to waste."

    jump final_escape

label aran_lives:

    $survivor = "Aran"

    f "What do you mean, only Aran?!"

    "Everyone is confused and dismayed. Aran looks extremely shocked at the sound of his name. Perhaps he was already resigned to death..."

    a "Are you sure about this?"

    z "But my little girl... No! Please no!"

    f "Clearly you’ve gone nuts. You’re really gonna leave us all here and take that worthless figurehead?"

    "Misha laughs mockingly at Fera."

    m "Maybe this is your karma for being such an evil bitch."

    "Aran is the only one who remains quiet. He drops to his knee in prayer, then addresses me softly."

    a "If this is what you want, then I am in no position to say no."

    "I close my eyes bitterly. I can’t bring myself to say anything to everyone."

    "How can I possibly explain to three people why I’m leaving them to die?"

    "How do I tell them that this is my fault? That my incompetence doomed two more people to certain death...? If only I could do this over again..."

    p "Everyone... I’m sorry. The ship I activated can only fit a pilot and 1 passenger..."

    "I wish I could talk to them and make them okay with this. But we have less than 3 minutes left."

    p "This is my fault... I’m so sorry. I won’t ask any of you to forgive me."

    "Aran bows apologetically as the three others begin to accept their fate with a combination of reflection, weeping, and fury."

    a "We must go."

    jump final_escape

label fera_lives:

    $survivor = "Fera"

    f "Hah! At least someone here has a bit of sense."

    "Aran’s face darkens, and he turns away. It appears he is very unhappy with my decision."

    "Everyone is confused and dismayed. Fera immediately begins walking towards the ship, but Zeni grabs her arm."

    z "Fera!"

    f "What now? Let go of me!"

    "Zeni holds onto her arm tightly, his voice pleading."

    z "Please. I have a daughter. Racia Taro. She’s only a child."

    f "What...?"

    z "I’m begging you. For someone like you, it would be nothing. Help her."

    "Fera stands still for a moment, looking surprisingly thoughtful."

    f "No promises."

    "She shakes him off and walks away onto the ship."

    "Misha scowls darkly at me and taps her foot furiously."

    m "So you’ve shown your true colors. I can’t believe you let her get her claws in you."

    "I close my eyes bitterly. I can’t bring myself to say anything to everyone."

    "How can I possibly explain to three people why I’m leaving them to die?"

    "How do I tell them that this is my fault? That my incompetence doomed two more people to certain death...? If only I could do this over again..."

    p "Everyone... I’m sorry. The ship I activated can only fit a pilot and 1 passenger..."

    "I wish I could talk to them and make them okay with this. But we have less than 3 minutes left."

    p "This is my fault... I’m so sorry. I won’t ask any of you to forgive me."

    jump final_escape

label final_escape:
    hide screen freak_parent

    call setup_escape(fade)

    play music mus_escape fadeout 5 fadein 5

    if one_death == False:
        "I board the ship without another word. Three faces watch on as the ship closes. Three faces I’ll never forget."

    "There was no other way..."

    if one_death == False:
        "There was no other way, right? I did the best that I could..."
        if survivor == "Zeni":
            z "Thank you."
        elif survivor == "Misha":
            m "I suppose I should be thanking you."
        elif survivor == "Aran":
            a "You have my thanks. I won’t make you regret this decision."
        else:
            f "I was right about you. You chose wisely."

    "I strap myself into the pilot’s chair and prepare to take off."

    play sound "Asteroid_Impact_Louder.ogg"

    "No sooner do we launch the ship than another asteroid strikes close by."

    "We made it. Somehow."

    "I lean back in the chair as we speed towards the surface of Mycia Beta."

    "It’s over."

    jump end_credits

label ultra_fail:

    "No way. I..."

    "The last ship goes into emergency lockdown."

    m "{i}What have you done?!!{/i}"

    "Misha lunges forward, shoving me aside to look at the console."

    m "You’ve killed us. You complete and total imbecile... you’ve killed us all!"

    "Aran’s gaze is focused on the view of Mycia Beta."

    m "Why did we put our lives in your hands? I should have just done this myself, I should have..."

    "This is the end. Everything we’ve done is for naught. And it’s all my fault."

    "Time slows, and we find ourselves standing separately in different parts of the room."

    "Zeni and Fara must slowly be coming to understand what’s gone wrong on the other side of the divider."

    "Each of us is trying to make peace in their own way, all hope lost."

    ai "Warning: Life support systems are offline."

    ai "Oxygen levels at: 22\%. All personnel, please use auxiliary oxygen sources..."

    "I’m sorry, Corsi... but it appears I’ll be joining you after all."

    jump end_credits


label end_credits:

    "Game over, suckaaa"
