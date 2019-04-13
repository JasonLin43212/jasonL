import math
# 1a
output1a = []
for num in range(10):
    if num % 2 == 0:
        output1a.append(str(num)*2)
# print(output1a)

#1b
output1b = [str(x)*2 for x in range(10) if x % 2 == 0]
# print(output1b)

#2a
output2a = []
for multiplier in range(5):
    output2a.append(7+multiplier*10)
# print(output2a)

#2b
output2b = [7+x*10 for x in range(5)]
# print(output2b)

#3a
output3a = []
for x in range(25):
    if x % 12 == 0:
        output3a.append(x//100)
        output3a.append(x//10)
        output3a.append(x%10)
# print(output3a)

#3b
output3b = sum([ [x//100,x//10,x%10] for x in range(25) if x % 12 == 0],[])
# print(output3b)

#4a
output4a = []
for x in range(101):
    if x <= 3:
        continue

    i = 2
    while i*i <= x:
        if x % i == 0:
            output4a.append(x)
            break
        i += 1
# print(output4a)

#4b
output4b = list(set([x for x in range(101) for i in range(2,math.ceil(math.sqrt(x))+1) if x > 3 and x % i == 0]))
# print(output4b)

# 5a
output5a = []
for x in range(101):
    if x not in output4a and x > 1:
        output5a.append(x)
# print(output5a)

# 5b
output5b = [x for x in range(101) if x not in output4a and x > 1]
# print(output5b)

#6a
def divisors_a(num):
    output = []
    for x in range(1,num):
        if num % x == 0:
            output.append(x)
    output.append(num)
    return output
# print(divisors_a(57))

#6b
def divisors_b(num):
    return [x for x in range(1,num+1) if num % x == 0]
# print(divisors_b(1024))

#7a
def transpose_a(arr):
    new_arr = []
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if row == 0:
                new_arr.append([arr[row][col]])
            else:
                new_arr[col] += [arr[row][col]]
    return new_arr

test =[\
[2,5,6,7],\
[4,2,8,9],\
]

# print(transpose_a(test))

#7b
def transpose_b(arr):
    return [[arr[row][col] for row in range(len(arr))] for col in range(len(arr[0]))]
# print(transpose_b(test))
