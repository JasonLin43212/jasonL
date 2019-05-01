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
        def incr():
            nonlocal x
            # nonlocal y # After this, it becomes closure
            x += 1
        incr()
        return x
    return inner

# accessor method of counter
def access_value(counter):
    return counter.__closure__[0].cell_contents


ctr1 = make_counter()
print("ctr1",ctr1())
print("ctr1",ctr1())
print("accessing ctr1", access_value(ctr1))
print("ctr1",ctr1())
ctr2 = make_counter()
print("ctr2",ctr2())
print("ctr2",ctr2())
print("ctr2",ctr2())
print("accessing ctr2", access_value(ctr2))
print("ctr1",ctr1())
print("ctr1",ctr1())
print("accessing ctr1", access_value(ctr1))
print("ctr2",ctr2())
print("accessing ctr2", access_value(ctr2))
