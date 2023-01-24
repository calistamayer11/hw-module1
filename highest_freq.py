from letters import letter_frequency, letter_count


def highest_freq(file):
    """
    Uses file name as input to create a dictionary of letter:frequencies.
    Function scrolls through each letter:frequency in dictionary and finds the highest frequency.
    Returns letter and max frequency as a tuple.
    """
    frequency_dict = letter_frequency(letter_count(file))
    max_value = 0
    max_key = ""

    for key, value in frequency_dict.items():
        if max_value < value:
            max_value = value
            max_key = key

    return (max_key, max_value)


if __name__ == "__main__":
    ltr, freq = highest_freq("frost.txt")
    expected_highest_freq_frost = ("i", 0.10952380952380952)
    assert expected_highest_freq_frost == (ltr, freq)

    hunger_games_tuple = highest_freq("The_Hunger_Games.txt")
    expected_highest_freq_hunger_games = ("e", 0.12451162240025257)
    assert expected_highest_freq_hunger_games == hunger_games_tuple
