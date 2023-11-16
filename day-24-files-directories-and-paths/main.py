with open("./Input/Names/invited_names.txt") as names_file:
    for name in names_file.readlines():
        new_name = name.strip()
        with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", mode="w") as letters_file:
            with open("./Input/Letters/starting_letter.txt") as starting_letter:
                txt = starting_letter.read().replace("[name]", new_name)
