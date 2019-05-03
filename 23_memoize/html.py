# Jason Lin
# SoftDev2 pd7
# K23 -- Memoize With Closure
# 2019-05-01
import random

def make_HTML_heading(f):
    txt = f()
    def inner():
        return '<h1>' + txt + '</h1>'
    return inner

# def greet():
#     greetings = ['hello','welcome','ayo','hola','bonjour','word up']
#     return random.choice(greetings)
#
# greet_heading = make_HTML_heading(greet)
# print(greet_heading())

#equiv to greet = make_HTML_heading(greet)
@make_HTML_heading
def greet():
    greetings = ['hello','welcome','ayo','hola','bonjour','word up']
    return random.choice(greetings)

# print(greet())

greet_heading2 = make_HTML_heading(greet)
# print(greet_heading2())

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(500))
