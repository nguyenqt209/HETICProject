import random

def word_generator(length):
    letters = "abcdefghijklmnopqrstuvwxyz"
    word = ""
    for i in range(length):
        word += random.choice(letters)
    return word

print(word_generator(5))