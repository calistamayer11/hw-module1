import string


def letter_count(file):
    alph = list(string.ascii_lowercase)
    num_of_letters = {letter: occurences}
    for i in alph:
        num_of_letters[i] = None
    occurences = 0
    f = open(file, "r")
    for key in num_of_letters:
        for line in f:
            for letter in range(len(line)):
                if key == letter:
                    occurences += 1
            num_of_letters[key] = occurences
            occurences = 0
            f.seek(0)
    f.close()
    return num_of_letters


print(letter_count(file="frost.txt"))
# print(num_of_letters)


# def letter_frequency(num_of_letters):
#     counts = letter_count("frost.txt")
#     print(counts)
#     freqs = letter_frequency(counts)
#     dict_letters = {}
#     frequency = num_of_letters[key] / 26
