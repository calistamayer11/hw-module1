import string


def letter_count(file):
    """
    Returns a dictionary of each letter and the number of occurrences the letter had in the file.
    """
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
    """
    Takes the dictionary of num_of_letters as input and calculates the frequency of occurrence for each letter in the file.
    """
    sum_of_all_letters = 0
    for value in num_of_letters.values():
        sum_of_all_letters = value + sum_of_all_letters

    freq_of_letters = {}

    for key, value in num_of_letters.items():
        frequency = value / sum_of_all_letters
        freq_of_letters[key] = frequency

    return freq_of_letters


if __name__ == "__main__":

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

    expected_frequency_hungergames = {
        "t": 0.09699721772761356,
        "h": 0.060632818974703025,
        "e": 0.12451162240025257,
        "u": 0.029139863451596353,
        "n": 0.06579778207506216,
        "g": 0.023624649749398163,
        "r": 0.053065432732152015,
        "a": 0.07796282410513437,
        "m": 0.029105331702119264,
        "s": 0.06519594301274714,
        "b": 0.017865247247326257,
        "y": 0.023740577765499822,
        "z": 0.0006733691148032676,
        "c": 0.024288152650065117,
        "o": 0.073740084454793,
        "l": 0.039898969967244166,
        "i": 0.0733725679782154,
        "p": 0.01783564860491732,
        "w": 0.02209538655826986,
        "k": 0.011728462054540431,
        "d": 0.03418889853585382,
        "f": 0.02180433324124867,
        "v": 0.009614625675835669,
        "q": 0.0006191049370535538,
        "x": 0.0010433521449149533,
        "j": 0.001457733138640041,
    }

    assert expected_frequency_hungergames == letter_frequency_of_hungergames

    assert letter_frequency(letter_count(file="assert.txt")) == {
        "a": 0.25,
        "b": 0.4,
        "c": 0.2,
        "d": 0.15,
    }
