from letters import letter_frequency, letter_count


def highest_freq(file):
    frequency_dict = letter_frequency(letter_count(file))
    max_value = 0
    max_key = ""

    for key, value in frequency_dict.items():
        if max_value < value:
            max_value = value
            max_key = key

    return (max_key, max_value)


print(highest_freq("frost.txt"))
(ltr, freq) = highest_freq("frost.txt")

expected_highest_freq = ("i", 0.10952380952380952)
assert expected_highest_freq == (ltr, freq)
