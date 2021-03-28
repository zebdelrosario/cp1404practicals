"""Word occurrences: Enter a sentence and see how many times your word is in that sentence."""


def main():
    sentence = input("Text: ")
    words_occurrences_dict = count_occurrences(sentence)
    display_dictionary(words_occurrences_dict)


def count_occurrences(sentence):
    """Count how often a word occurs in the given sentence."""
    words = sentence.split(" ")
    words.sort()
    words_occurrences_dict = {}
    for word in words:
        if word not in words_occurrences_dict.keys():
            words_occurrences_dict[word] = words.count(word)
    return words_occurrences_dict


def display_dictionary(dictionary):
    """Display a dictionary in aligned fashion."""
    key_char_length = max([len(key) for key in dictionary.keys()])
    value_char_length = max(dictionary.values())
    for key, value in dictionary.items():
        print(f"{key:<{key_char_length}} : {value:>{value_char_length}}")


main()
