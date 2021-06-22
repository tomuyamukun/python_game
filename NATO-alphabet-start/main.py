import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

alpha_df = {row.letter: row.code for (index, row) in df.iterrows()}


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [alpha_df[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
