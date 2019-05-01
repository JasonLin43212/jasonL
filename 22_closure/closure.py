def repeat(word):
    def output(num):
        return word*num
    return output

r1 = repeat('hello')
r2 = repeat('goodbye')
# print(r1(2))
# print(r2(2))
# print(repeat('cool')(3))

def make_counter():
    x = 0
    def inner():
        def incr():
            nonlocal x
            x += 1
        incr()
        return x
    return inner

# accessor method of counter
ctr1 = make_counter()
print("ctr1",ctr1())
print("ctr1",ctr1())
print("ctr1",ctr1())
ctr2 = make_counter()
print("ctr2",ctr2())
print("ctr2",ctr2())
print("ctr2",ctr2())
print("ctr1",ctr1())
print("ctr1",ctr1())
print("ctr2",ctr2())

def accessor(ctr):
    nonlocal x
    return x

print(accessor(ctr1))
