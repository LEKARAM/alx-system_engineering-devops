#!/usr/bin/python3

def count_words(sentence, words_to_count):
    word_count = {}

    for word in words_to_count:
        if word.lower() in sentence.lower():
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    return word_count
