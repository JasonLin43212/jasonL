# Jason Lin
# SoftDev2 pd7
# K22 -- Closure
# 2019-04-30
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
        nonlocal memo
        if x in memo:
            return memo[x]
        if len(memo.keys()) < 2:
            memo[len(memo.keys())] = f(len(memo.keys()))
            memo[len(memo.keys())] = f(len(memo.keys()))
        memo_len = len(memo.keys())
        if memo_len < x+1:
            memo[memo_len] = memo[memo_len-1] + memo[memo_len-2]
        return helper(x)
    return helper

@memoize
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(800))
