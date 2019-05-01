import random

def make_HTML_heading(f):
    txt = f()
    def inner():
        return '<h1>' + txt + '</h1>'
    return inner

def greet():
    greetings = ['hello','welcome','ayo','hola','bonjour','word up']
    return random.choice(greetings)

greet_heading = make_HTML_heading(greet)
print(greet_heading())
