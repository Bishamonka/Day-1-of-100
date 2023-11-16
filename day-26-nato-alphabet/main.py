import pandas

data_as_df = pandas.read_csv("nato_phonetic_alphabet.csv")
data_as_dict = {row.letter: row.code for (index, row) in data_as_df.iterrows()}

ui_word = input("Type a word: ").upper()

result = [data_as_dict[letter] for letter in ui_word]
print(result)
