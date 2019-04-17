# Team Reduce Reuse Recycle -- Simon Tsui and Jason Lin
# SoftDev2 pd7
# K20 --
# 2019-04-17

from functools import reduce

f = open("tom.txt",'r')
words = f.read().split()
f.close()
words = [0] + words
# print(words)
the = [x for x in words if x == "the"]
# print(len(the))
the2 = reduce((lambda x,y : x+1 if y =="the" else x),words)
# print(the2)

search = ["by","the",""]
