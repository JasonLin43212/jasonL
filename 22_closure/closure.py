# Jason Lin
# SoftDev2 pd7
# K22 -- Closure
# 2019-04-30

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
    # y = 2 #Declaring it here is not closure
    def inner():
        nonlocal x
        # nonlocal y # After this, it becomes closure
        x += 1
        return x
    def access():
        return x
    return inner,access

# accessor method of counter
def access_value(counter):
    return counter.__closure__[0].cell_contents


ctr1,acc1 = make_counter()
print("ctr1",ctr1())
print("ctr1",ctr1())
print("accessing ctr1", acc1())
print("ctr1",ctr1())
ctr2,acc2 = make_counter()
print("ctr2",ctr2())
print("ctr2",ctr2())
print("ctr2",ctr2())
print("accessing ctr2", acc2())
print("ctr1",ctr1())
print("ctr1",ctr1())
print("accessing ctr1", acc1())
print("ctr2",ctr2())
print("accessing ctr2", acc2())
