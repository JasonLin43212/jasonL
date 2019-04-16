import math
# Pythagorean Triples

def triple(n):
    return set(sum([ [x,y,int(math.sqrt(math.pow(x,2)+math.pow(y,2)))]\
                    if ((math.sqrt(math.pow(x,2)+math.pow(y,2))).is_integer() and math.sqrt(math.pow(x,2)+math.pow(y,2))<n)\
                    else [x,y] if math.sqrt(math.pow(x,2)+math.pow(y,2)).is_integer()\
                    else []\
                    for x in range(1,n) for y in range(1,n)\
                    ],[]))
# print(triple(100))

def quicksort(arr): return sum([[] if len(arr) == 0 else quicksort([x for x in arr if x < arr[0]]) + [x for x in arr if x == arr[0]] + quicksort([x for x in arr if x > arr[0]])],[])

print(quicksort([3,2,33,1,5,7,1,4,9,23,4,23,7]))
