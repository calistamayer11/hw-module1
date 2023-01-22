import string


def letter_count(file):
    alph = list(string.ascii_lowercase)
    num_of_letters = {}

    with open(file, "r") as f:
        for line in f:
            for letter in line:
                if letter.lower() in alph:
                    if num_of_letters.get(letter.lower()):
                        num_of_letters[letter.lower()] += 1
                    else:
                        num_of_letters[letter.lower()] = 1

    return num_of_letters


def letter_frequency(num_of_letters):
    sum_of_all_letters = 0
    for value in num_of_letters.values():
        sum_of_all_letters = value + sum_of_all_letters

    freq_of_letters = {}

    for key, value in num_of_letters.items():
        frequency = value / sum_of_all_letters
        freq_of_letters[key] = frequency

    return freq_of_letters


letter_count_of_frost = letter_count("frost.txt")
letter_frequency_of_frost = letter_frequency(letter_count_of_frost)


letter_count_of_hungergames = letter_count("The_Hunger_Games.txt")
letter_frequency_of_hungergames = letter_frequency(letter_count_of_hungergames)


expected_count_frost = {
    "f": 12,
    "i": 23,
    "r": 14,
    "e": 23,
    "a": 13,
    "n": 9,
    "d": 10,
    "c": 6,
    "s": 14,
    "o": 20,
    "m": 3,
    "y": 3,
    "t": 20,
    "h": 12,
    "w": 8,
    "l": 6,
    "v": 2,
    "b": 2,
    "u": 5,
    "p": 1,
    "k": 2,
    "g": 2,
}

assert expected_count_frost == letter_count_of_frost

expected_count_hungergames = {
    "t": 39325,
    "h": 24582,
    "e": 50480,
    "u": 11814,
    "n": 26676,
    "g": 9578,
    "r": 21514,
    "a": 31608,
    "m": 11800,
    "s": 26432,
    "b": 7243,
    "y": 9625,
    "z": 273,
    "c": 9847,
    "o": 29896,
    "l": 16176,
    "i": 29747,
    "p": 7231,
    "w": 8958,
    "k": 4755,
    "d": 13861,
    "f": 8840,
    "v": 3898,
    "q": 251,
    "x": 423,
    "j": 591,
}

assert expected_count_hungergames == letter_count_of_hungergames
