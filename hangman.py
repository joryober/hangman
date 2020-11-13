import random

with open("wordlist.10000.txt", "r") as word_list:
    words = word_list.read().splitlines()

while(True):
    try:
        word_length = int(input("Please input length of word to guess: "))
        while not (3 < word_length < 16):
            print("Invalid entry. Please enter an integer between 3 and 16.\n")
            word_length = int(
                input("Please input length of word to guess: "))
        break
    except ValueError:
        print("Invalid entry. Please enter an integer between 3 and 16.\n")


def get_word(word_length):
    words_of_length = [word for word in words if len(word) == word_length]
    return words_of_length[random.randrange(0, len(words_of_length) - 1)]


def make_hanger(
    head_level="|".center(15), torso_level="|".center(15), legs_level="|".center(15)
):
    base = "---------------"
    stem = "|".center(15)
    bends = "/         \\".rjust(18)
    top = "_________".rjust(17)
    print(top)
    print(bends)
    print(head_level)
    print(torso_level)
    print(legs_level)
    for _ in range(4):
        print(stem)
    print(base)


make_hanger()
print(get_word(word_length))
