def inc(x):
    return x+1

f = inc
# Prints the address of the function
# print(f)
# print(inc)
# print(inc(10))
# print(f(10)) # 11

def adder(a,b):
    return a+b

def caller(c):
    print(c(2,4)) # 6
    print(c(3,5)) # 8

# A function that takes in a function and calls it within it.
# caller(adder)
# print(caller)

# A closure
def outer(x):
    def contains(l):
        return x in l
    return contains

# print(outer(42))
contains_15 = outer(15)
print(contains_15([1,2,3,4,5]))
print(contains_15([13,14,15,16,17]))
print(contains_15(range(1,20)))

del outer
# print(outer(42))
print(contains_15(range(14,20)))

# Global scope vs local scope

# def outer():
#     x = "foo"
#     def inner():
#         x = "bar"
#     inner()
#     return x
#
# print(outer())

def outer():
    x = "foo"
    def inner():
        nonlocal x
        x = "bar"
    inner()
    return x

print(outer())
