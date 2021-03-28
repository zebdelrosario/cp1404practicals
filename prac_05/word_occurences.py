"""Word occurrences: Enter a sentence and see how many times your word is in that sentence."""


def main():
    # sentence = input("Text: ")
    sentence = "this is the sentence provided the sentence is this"
    words_occurrences_dict = count_occurrences(sentence)


def count_occurrences(sentence):
    """Count how often a word occurs in the given sentence."""
    words = sentence.split(" ")
    words_occurrences_dict = {}
    for word in words:
        if word not in words_occurrences_dict.keys():
            words_occurrences_dict[word] = words.count(word)
    return words_occurrences_dict


main()
