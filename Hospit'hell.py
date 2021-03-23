# define each loop

'''
# "-" MEANS STORY
start_and_exit                       while true 
                                    print()
    -playgame                            
    yes                                 if 1
        -SeeHospitalWithFriends
            Checkouthospital                if 2
                -friendsdisappear
                    Run away                    if 3
                        -Doom!
                            1 something 1
                                a dead
                                b wish were dead
                            2 something else
                                a awful
                                b terrible, no good, very-bad day  

                    Go after them               elif
                                                else
                        -gate locked/stone wall to climb GATE OPEN
                            climb the wall          if 4
                                -Doom!
                            walk through gate       elif
                                                    else
                                -gate shuts/ doors open 
                                    find another way in     if 5
                                        -Doom!
                                    go in                   elif
                                                            else    
                                        -Friends in distance/Shadow turns to dragon
                                            Fight                                       if 6
                                                1 Charge recklessly "Leeroy Jenkins!"       if 7
                                                    -Doom!
                                                2 Get something to fight with               elif
                                                                                            else
                                                    -final ending                                   if 8
                                            Flight                                      elif
                                                1 Run towards weapon                        if 7b
                                                    -final ending                                   if 8
                                                2 Turn away                                 elif
                                                                                            else
                                                    -Doom!
                                            Freeze                                      elif
                                                                                        else
                                                1 Assess situation                          if 7c
                                                    -final ending                                   if 8                                                
                                                2 Stay frozen                               elif
                                                                                            else
                                                    -Doom!
                                                        1 something 1
                                                            a dead
                                                            b wish were dead
                                                        2 something else
                                                            a awful
                                                            b terrible, no good, very-bad day
            Walkaway from                   elif (2nd level)
                                            else
            -Doom!
                1 something 1
                    a dead
                    b wish were dead
                2 something else
                    a awful
                    b terrible, no good, very-bad day

    no                                     elif (1st level)
        -exit                                   
            yes                                 if
            no                                  elif
                                                else
                -sure
                    yes                             if
                    no                              elif
                                                    else
                        -reallysure
                            exit
    q!                                      elif
    "asdf"                                  else
    -exit


'''


# what will the condition be


def exit():
    quit("Goodbye for now.")  # The end.


def doom():
    input(
        "\nEverything is dark. You don't recall going to bed, but you wake up disoriented. \n Why am I on my feet? It's really cold in here, and my arms are... kinda stuck. \n Wait a sec. Something's on my wrists. Oh no...! \n My arms are manacled above me! Where am I?! \n My friends! They're lined up next to me, and chained up like Y's! \n What's going on here?! 'Hey, guys! Are you okay?' \n \n 'Yeah, we just woke up here. What is this place? \n \n 'It looks like a dirty, old operating room. You can see the table right there- \n \n *SLAM* \n \n [Your friends scream as the same shadowy being forms from the darkness.] \n [With a deep roaring call, the figure flies into your furthest friend along the wall, disappearing.] \n [After a moment, your friend starts to panic as they start to levitate away from the wall.] \n The panic turns to yells of pain as their arms pop backwards and the hands tear through the manacles.] \n [Unable to process this event, you watch in horror as your flying friend goes quiet and limp for a moment.] \n [He then screams shortly before exploding all over the room.] \n \n [You are puzzled to see Tim`s ear on your left bicep.] \n \n [Chaos erupts in the room as the operation of this shadow being repeats the same gruesome process.] \n [One by one, your friends levitate, twist, and explode coming closer to you.] \n 'This isn't happening...' you think while in the air. \n \n \n *SKPLAT* ")
    input("All is gone. This must be death. \n You then find yourself going out with your friends, with a sense of Deja Vu. \n \n ")
    start_or_exit()


def final_scene():
    print("The floor is cold and hard on your face, as you come to. \n A strong smell hits you with a mix between something coppery and way too much hand sanitizer. \n You notice the walls are covered with white pads when a shriek pierces your ear. \n To your horror, you realize you are trapped inside Albion Asylum! \n Worse, you haven't rescued your friends.")
    input()
    input("Congratulations, you survived the first part of 'Hospit'hell,' a survival story series. \n If you would like to hear the next part of this story please let the developer know about it. \n As for now, if you would like to quit the game please type EXIT. \n If you would like to play again please type PLAY. \n Thank you for playing!")
    final_choice = ""
    while final_choice != ("EXIT" or "PLAY"):  # Last choice
        pass
        final_choice = input("").upper()
        if final_choice == "EXIT":  # Goes to exit
            exit()
        elif final_choice == "PLAY":  # Goes to beginning
            start_or_exit()
        else:
            print("Please try again.")


def reception_freeze_doom():
    doom()


def reception_freeze():
    freeze_option = ""
    while freeze_option != ("ASSESS" or "STAY"):  # FREEZE
        pass
        freeze_option = input(
            "You choose to FREEZE in place to best survive the situation. \n Do you ASSESS the situation or STAY still till the problem goes away? \n \n ").upper()
        if freeze_option == "ASSESS":  # Go to end
            print("The best thing you can do is to ASSESS the situation. \n You see a candelabra in the distance. That will work as a weapon to get you through this mess. \n You get out of the way before the dragon smashes where you stood. \n You run to the light, but not before it snuffs out and the dragon materializes in front of you. \n \n The dragon lunges at you enveloping you in darkness, where you lose consciousness. \n \n ")
            final_scene()
        elif freeze_option == "STAY":  # DOOM
            print("Fear consumes you, and you are unable to move. \n \n In your paralysis, you watch in horror as the dragon lunges at you, and your world goes black. \n \n ")
            reception_freeze_doom()
        else:
            print("Please try again.")


def reception_flight_doom():
    doom()


def reception_flight():
    flight_option = ""
    while flight_option != ("DASH" or "FLEE"):  # FLIGHT
        pass
        flight_option = input(
            "It's best to take FLIGHT from this monstrous dragon before it kills you or worse. \n \n Do you DASH toward a possible weapon or FLEE from the monster? \n \n ").upper()
        if flight_option == "DASH":  # Go to end
            print("There's no way you can face this thing without some sort of help or weapon. \n You DASH away before the dragon snap you in its mighty maw. \n Perhaps you can use one of the candelabras as a spear. \n You start toward the light when the dragon materializes right in front of you. \n \n 'Oh no...' you think right before the dragon consumes you whole turning your world pitch black. ")
            final_scene()
        elif flight_option == "FLEE":  # DOOM
            print("Scared stupid, you turn around to FLEE. \n Unfortunately, you slam right into the great doors giving nothing but the sound of your cracked face. \n You rotate, aghast, seeing the dragon coming at you. \n \n The world went pitch black at that point. \n \n ")
            reception_flight_doom()
        else:
            print("Please try again.")


def reception_fight_doom():
    doom()


def reception_fight():
    fight_option = ""
    while fight_option != ("CHARGE" or "GET"):  # FIGHT
        pass
        fight_option = input(
            "Since you can't escape this dragon, it's best to fight it. \n \n Do you CHARGE the beast or GET a weapon? \n \n ").upper()
        if fight_option == "CHARGE":  # DOOM
            print("Feeling anger for the loss of your friends, you decide to CHARGE reckless. \n The dragon opens its maw impossibly wide and gobbles you up. \n ")
            reception_fight_doom()
        elif fight_option == "GET":  # Go to end
            print("Before the dragon leaps out to snap you in its jaws, you dash away to GET a weapon. \n Heading toward a tall candelabra, the monster shrieks a yell as it crashes into the doors behind you. \n You pick it up and wield it as a spear. \n The dragon snarls a hellish cry and charges after you. \n Bravery consumes you and you thrust your spear, flame first, into it's gaping maw. \n Suddenly, the shadow beast disappears like evaporating smoke. \n 'Was that it? It can't be,' you think, poised for action. \n \n Without warning, the beast materializes right above you and swallows you whole, where everything turns black. \n \n ")
            final_scene()
        else:
            print("Please try again.")


def reception_triad():
    triad = ""
    while triad != ("FIGHT" or "FLIGHT" or "FREEZE"):  # Three choices
        pass
        triad = input(
            "The light reveals a great Victorian Era mezzanine with massive staircases, Corinthian columns, and marble floors. \n That's when you see one of your friends in the distance at the top of the stairs. \n He's being pulled by the dark hand around his legs, screaming bloody murder. \n That's not all that's bloody. His fingernails are scraping the ground leaving bloody trails. \n A split second later, he's been pulled through a door at the top of the stairs that slams shut behind him, muffling his screams. \n As soon as you dart forward to save him, the incorporeal being forms in front of you from the shadows. \n It seems to recognize you for a second before changing its shape into some sort of dragon. \n The adrenaline kicks in and your heart is pounding out of your chest trying to deal with this dragon! \n \n Do you FIGHT it? \n Take FLIGHT from it? \n Or FREEZE in front of it? \n \n ").upper()
        if triad == "FIGHT":  # Go to fight
            reception_fight()
        elif triad == "FLIGHT":  # Go to flight
            reception_flight()
        elif triad == "FREEZE":  # Go to freeze
            reception_freeze()
        else:
            print("Please try again.")


def courtyard_door_doom():
    doom()


def courtyard_door():
    the_main_gate = ""
    while the_main_gate != ("GO" or "LOOK"):  # Gate or wall
        pass
        the_main_gate = input(
            "'I think this place just got creepier,' you think while summing the place up. \n It appears to be a large courtyard. I wonder if any of the patients came out here. \n As soon as you think the thought, the huge wooden doors to the asylum slowly creak and croak open. \n No sooner than the doors stop moving does a horrible scream echo from the doors. \n Taking your first step forward, the front gates quickly screech shut with a bang. \n That's bad, definitely bad. \n \n I can either GO through the doors or LOOK around for another way in. \n ").upper()
        if the_main_gate == "GO":  # Go to the reception area
            print("You choose to GO through the great, wooden doors, because why not? \n You've made it this far by going forward. \n Walking through the doors reveals a large open area with what seems to be a reception desk. \n Suddenly, blazing light emits from various torches and candelabras. \n Is this place a mansion or castle? Doesn't seem to be a hospital. \n \n ")
            reception_triad()
        elif the_main_gate == "LOOK":  # DOOM
            print("This place is literally mental! No way are you going through those 'doom doors!' \n \n You choose to LOOK for another way in. \n \n As you venture around the enormous building, you see nothing promising. \n A whistling rustle sounds behind you. You quickly turn to see nothing but leaves blowing in the wind. \n Your nerves are on total-edge. Something cracks off in the distance. \n 'What was that?!' you think, looking around quickly. \n You double back quickly, desperate to find anything of hope when you hear an awful sound that resembles yawning, moaning, and yelling altogether. \n You freeze, realizing that loud sound was close behind you. \n Slowly, you turn around when a large black shadow leaps at you, screaming that unearthly sound! \n \n ")
            courtyard_door_doom()
        else:
            print("Please try again.")


def gate_wall_doom():
    doom()


def gate_wall():
    climb_or_back = ""
    while climb_or_back != ("CLIMB" or "PASS"):  # Welcome to wall
        pass
        climb_or_back = input(
            "You could run back to town for help, but looking around shows you that the ground you are walking on is now the top of a plateau. \n What's worse is that you can't seem to see the bottom of the ground below. \n So much for getting help. This place is nuts! \n Might as well try and climb the wall to go after them. \a As soon as you start climbing the tall, stone wall the large, metal gate creaks open. \n \n 'Of course the gate opens now,' you think.\n \n Well, I can either CLIMB this wall or PASS through the gate. \n Both seem awful. \n \n ").upper()
        if climb_or_back == "CLIMB":  # DOOM
            print("\nYou decide to CLIMB the wall. \n There's no way you're going through that evil gate to save your friends. \n You make your way to the top of the wall. Suddenly, the stones on the wall shift making you lose your balance. \n Your stomach sinks as you plummet 2-stories, head first, toward the ground below. ")
            gate_wall_doom()
        elif climb_or_back == "PASS":  # To the courtyard
            print(" \nThe gate is creepy, but how else are you going to save your friends in time? \n You decide to PASS through the asylum gates. \n ")
            courtyard_door()
        else:
            print("Please try again.")


def intro_doom():
    doom()


def intro_walking_by():
    first_choice_walk = ""
    while first_choice_walk != ("FOLLOW" or "WALK"):  # And so it begins
        pass
        print(
            "\n You and your group of friends decide to visit the haunted 'Albion Asylum.' ")
        first_choice_walk = input(
            "Your friends go check out the creepy gate. \n Do you FOLLOW them or WALK away? \n ").upper()
        if first_choice_walk == "FOLLOW":  # Go to gate
            print("\n Following your friends to the gate, a dark chill flows over you. \n Ten feet in front of you, a shadowy, incorporeal being materializes. \n Stunned at this surreal moment, the dark figure emits large hands that pull your screaming friends toward the asylum. \n The gate lets them in, and you charge after them; but the gate slams shut when you get to it. ")
            gate_wall()
        elif first_choice_walk == "WALK":  # DOOM
            print('That place is way too creepy! You call out, "No thanks, guys!" and turn around to start walking away. \n After a few seconds a cold chill runs up your heels to your head. \n Suddenly, your friends` screams pierce your ears underlayed by a metallic groan. \n Shocked, you turn around to see a shadowy, incorporeal being fly toward you. \n It is moving so fast toward you that you start to scream and --... ')
            doom()
        else:
            print("Please try again.")


def second_prompt_exit():
    second_exit = ""
    while second_exit != ("YES" or "NO"):  # Second exit prompt.
        pass
        second_exit = input(
            "Are you absolutely sure you want to quit? YES or NO? ").upper()
        if second_exit == "YES":
            exit()
        elif second_exit == "NO":  # Go to the beginning.
            print("I warned you...")
            start_or_exit()
        else:
            print("Please try again.")


def first_prompt_exit():
    first_exit = ""
    while first_exit != ("YES" or "NO"):  # First exit prompt.
        pass
        first_exit = input(
            "Are you sure you want to quit? YES or NO? ").upper()
        if first_exit == "YES":
            second_prompt_exit()
        elif first_exit == "NO":
            # Go to the beginning.
            first_exit = input("You are a brave soul. Good luck. ")
            start_or_exit()
        else:
            print("Please try again.")


def start_or_exit():
    input("Welcome to the Hospit'hell. \n \n [WARNING: THIS GAMES CONTAINS DEPICTIONS OF HORROR, GORE, AND EXTREME VIOLENCE] \n [DO NOT PLAY THIS GAME IF YOU ARE SENSITIVE TO ANY OF THESE THINGS!] \n \n You have been warned. \n Viewer discretion advised. \n \n (Please press enter to make your next choice.) ")
    press_start = ""
    while press_start != ("YES" or "NO"):  # This is the introduction choice.
        pass
        press_start = input("Do you want to play? YES or NO? \n \n ").upper()
        if press_start == "YES":
            intro_walking_by()
        elif press_start == "NO":
            first_prompt_exit()
        else:
            print("Please try again.")


start_or_exit()
