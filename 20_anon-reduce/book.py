# Team Reduce Reuse Recycle -- Simon Tsui and Jason Lin
# SoftDev2 pd7
# K20 -- Reductio ad Absurdum
# 2019-04-17

from functools import reduce
import string

f = open("tom.txt",'r')
words = f.read()
for c in string.punctuation+"“”":
    words = words.replace(c," ")
words = words.split()
f.close()
# print(words)

# Adds one to the current count if the word is the same as the input
def word_freq(word):
    return reduce((lambda x,y : x+1 if y.lower() == word else x),words,0)
# print(word_freq("entirely"))

# Use list comprehension to create a sliding window that adds a 1 if it finds the
# phrase and 0 if it doesn't match. Then use reduce to add up all the 1s.
def phrase_freq(phrase):
    phrase = phrase.split()
    return reduce((lambda x,y: x+y),[1 if words[i:i+len(phrase)] == phrase\
                                       else 0\
                                       for i in range(len(words)-len(phrase)+1)],0)
print(phrase_freq("in the"))

# Goes through the entire book once and counts the occurance of each word.
# We were unable to find a reduce/listcomp way to do this
def get_most_frequent():
    word_dict = {}
    for word in words[1:]:
        word = word.lower()
        if word in word_dict.keys():
            word_dict[word] = word_dict[word] + 1
        else:
            word_dict[word] = 1
    most_word = ''
    high_freq = 0
    for key in word_dict:
        if word_dict[key] > high_freq:
            most_word = key
            high_freq = word_dict[key]
    return most_word,high_freq
    # return reduce((lambda x,y: ))
    # return reduce((lambda x,y: [y,word_freq(y)] if word_freq(y) > x[1] else x),[["",0]] + list(set(words[1:])))
# print(get_most_frequent())
