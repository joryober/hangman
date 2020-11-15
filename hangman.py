import random

with open("wordlist.10000.txt", "r") as word_list:
    words = word_list.read().splitlines()


def get_word():
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

    words_of_length = [word for word in words if len(word) == word_length]
    return words_of_length[random.randrange(0, len(words_of_length))]


def make_guessed_box(letters):
    if len(letters) == 0:
        return
    print("-"*(len(letters) * 2 + 3))
    print("|", end=" ")
    for letter in letters:
        print(letter, end=" ")
    print("|")
    print("-"*(len(letters) * 2 + 3))
    print("\n")


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


def stage0():
    return make_hanger()


def stage1():
    return make_hanger(head_level="|         O".rjust(18))


def stage2():
    return make_hanger(head_level="|         O".rjust(18),
                       torso_level="|         |".rjust(18))


def stage3():
    return make_hanger(head_level="|         O".rjust(18),
                       torso_level="|        \\|".rjust(18))


def stage4():
    return make_hanger(head_level="|         O".rjust(18),
                       torso_level="|        \\|/".rjust(19))


def stage5():
    return make_hanger(head_level="|         O".rjust(18),
                       torso_level="|        \\|/".rjust(19), legs_level="|        /".rjust(17))


def stage6():
    return make_hanger(head_level="|         O".rjust(18),
                       torso_level="|        \\|/".rjust(19), legs_level="|        / \\".rjust(19))


stages = [stage0, stage1, stage2, stage3, stage4, stage5, stage6]


def main():
    print("\nWelcome to Hangman!\n")

    solved = False

    word = get_word()
    hidden_word = "".join(["_" for char in word])
    stage = 0
    stages[stage]()
    incorrect_letters = []

    print("\n")
    print(" ".join(list(hidden_word)))
    print("\n")

    while not solved:
        guess = input("Guess? (type 'quit' to end game): ")

        if guess.lower() == "quit":
            return

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid guess.")
            print("Please input a single letter.")
            continue

        guess = guess.lower()

        if guess in incorrect_letters or guess in hidden_word:
            print("Already guessed this letter! Please input different letter.\n")
            continue

        if guess in word:
            hidden_word_split = list(hidden_word)
            indices = [i for i, x in enumerate(list(word)) if x == guess]
            for index in indices:
                hidden_word_split[index] = guess
            hidden_word = "".join(hidden_word_split)
        else:
            stage += 1
            incorrect_letters.append(guess)

        stages[stage]()
        print("\n")
        print(" ".join(list(hidden_word)))
        print("\n")

        make_guessed_box(incorrect_letters)

        if hidden_word.count("_") == 0:
            print("You win!\n")
            break

        if stage == 6:
            print("You lose.")
            print(f"[Word was {word}]\n")
            break


main()
