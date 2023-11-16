# Welcome Section

print("Welcome to 'WHERE IS MY LOVELY SOCK?'")
print("[Your mission is to find the second sock of your favorite pair.] \n \n")

#Cover Image

print('''

     .    !__________!    .    _______
    /_\   |____  ____|   /_\   |__*__|
   __|__  {____}{____}  __|__  |__*__|
 __|_*_|__%%%%%%%%%%%%__|_*_|__|__*__|__
   |   | %%%%%%%%%%%%%% |   |  |/   \|
        %%%%%%%%%%%%%%%%
       %%%%%%%%%%%%%%%%%%
      %%%%%%%%%%%%%%%%%%%%
      ||||||||||||||||||||
      
''')

# Player's path begins here with 3 Options

print(
    "You find yourself laying on the bed. Seems like its pretty late already. You see only one sock on your foot, gotta find the seccond one..."
)

choice_1 = input(
    "Where could it be? You can search under the 'bed', 'stand up' for a better view or maybe 'think' a bit. \n\nYou choose: "
)
choice_1 = choice_1.lower()

# First Option Branch

if choice_1 == "bed":
    print(
        "\nYou bend over to the edge of the bed, lying on your stomach trying to look under the bed. You still feel preety sleepy though... \nThen suddenly you think you might see it in the dark."
    )
    choice_1_1 = input(
        "You can try to 'grab' it though it's preety far away. Or you can 'leave it' and change your mind, so no socks for today! \n\nYou choose: "
    )
    choice_1_1 = choice_1_1.lower()
    if choice_1_1 == "grab":
        print(
            "\nYou've decided to reach and grab something you thought was your sock in a dark. \nLying on your stomach on the bed, with your head down you suddenly felt weakness in your sleepy body. One imprudent move and you hear some of your cervical vertebrae cracking. You are paralizes now. \n\n»» GAME OVER ««\n"
        )
    elif choice_1_1 == "leave it":
        print(
            "\nWho knows if it was the best choice for today. Even though you are ready to begin your day, you feel that you'll be missing youur favorite pair of socks the whole day. \n\n»» GAME OVER ««\n"
        )
    else:
        print("\n»ERROR«\nInvalid input. Restart the game.\n»ERROR«\n")

    # Second Option Branch

elif choice_1 == "stand up":
    print(
        "\nYou've decided to stand up for a better view, maybe from this height you'll finaly be able to see it. Room is not big, you still don't see it on the floor."
    )
    choice_2 = input(
        "But think you might find it in the 'closet' or change your mind and look inder the 'bed'.\n\nYou choose: "
    )
    choice_2 = choice_2.lower()
    if choice_2 == "closet":

        print(
            "\nIt was already couple of days since you remember yourself opening it last time. Previously the inner shelf almost killed you. But you were lucky enough to avoid it then. Unfortunately seems like not this time. You hear how your skull makes cracking noizes. Some warm liquid flows from your head, covering your eyes. Suddenly. It's dark and quiet. You are dead. \n\n»» GAME OVER ««\n"
        )
    elif choice_2 == "bed":
        print(
            "\nYou decide to look under the bed. You still feel preety sleepy though... There's no light under your bed. You kepp skimming with your eyes and suddenly you think you might see it in the dark. You reach your hand towards it. Oh the bed... if only you`d fixed it. One imprudent move and you hear your skull cracks. Should've bought better bed. It's dark and quiet now. You are dead. \n\n»» GAME OVER ««\n"
        )
    else:
        print("\n»ERROR«\nInvalid input. Restart the game.\n»ERROR«\n")

    # Third Option Branch

elif choice_1 == "think":
    print("\nBefore you think, you think how long do you need to think.")
    choice_3 = input(
        "So you think you can think a 'few minutes' or a 'couple of hours'.\n\nYou choose: "
    )
    choice_3 = choice_3.lower()
    if choice_3 == "few minutes":
        print(
            "\nEven though you still feel preety sleepy, you've decided to think a few minutes where could it be but you seemlesly fall asleep. Seems like you won't find your sock today, but 'hey' maybe it's better for your health? \n\n»» GAME OVER ««\n"
        )
    elif choice_3 == "couple of hours":
        print(
            "\nYou start to think... and then fall asleep. Waking up, falling asleep then back... but you had a goal. And all that time you were recalling where the sock could be... \nFinaly, after a couple of hours you see a dream: \n—'I`m here! Under! Look! Pssssst! Under the pillow!' \nSuddenly you wake up in sweat, you grab your pillow. OMG! It's here! It was here the whole time! You've achieved your goal... but weird thoughts started to filling your mind... What would happen if you chose the wrong tactics? Guess you'll never know. \n\n»» CONGRATULATION! ««\n"
        )
    else:
        print("\n»ERROR«\nInvalid input. Restart the game.\n»ERROR«\n")
else:
    print("\n»ERROR«\nInvalid input. Restart the game.\n»ERROR«\n")
