import math

def palindrome():
    word = input("Insert a word: ")
    i = len(word)
    while i >= math.floor((len(word)) / 2):
        i -= 1
        if word[i] == word[len(word)-i-1]:
            continue
        else:
            return False

    return True


print(palindrome())