# Team Reduce Reuse Recycle -- Simon Tsui and Jason Lin
# SoftDev2 pd7
# K20 --
# 2019-04-17

from functools import reduce
import string

f = open("tom.txt",'r')
words = f.read()
for c in string.punctuation:
    words = words.replace(c,"")
words = words.split()
f.close()
words = [0] + words
# print(words)
# the = [x for x in words if x == "the"]
# print(len(the))
def word_freq(word):
    return reduce((lambda x,y : x+1 if y.lower() == word else x),words)

# print(word_freq("entirely"))

phrase = "in the".split()
group = reduce((lambda x,y: x+y),[1 if words[i:i+len(phrase)] == phrase else 0 for i in range(len(words)-len(phrase)+1) ])
# group = reduce((lamda x,y : [x[0]+1,x[1]+y] if y == phrase[x[0]] else [0,'']), words)
# print(group)
