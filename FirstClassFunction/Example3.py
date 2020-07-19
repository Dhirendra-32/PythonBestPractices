"""
Functions Can Be Passed to Other Functions
Because functions are objects, you can pass them as arguments to
other functions. Here’s a greet function that formats a greeting string
using the function object passed to it and then prints it:
"""
def yell(text):
    return text.capitalize() + '!'
print(yell('hello'))
bark = yell
print(bark('hello'))
funcs = [bark, str.lower, str.capitalize]

def greet(func):
    greeting = func('Hi, I am a Python program')
    print(greeting)
greet(bark)

# defining new functions to change the flvaour
def whisper(text):
    return text.upper() + '...'
greet(whisper)
"""
The ability to pass function objects as arguments to other functions is
powerful. It allows you to abstract away and pass around behavior in
your programs. In this example, the greet function stays the same but
you can influence its output by passing in different greeting behaviors.
Functions that can accept other functions as arguments are also called
higher-order functions. They are a necessity for the functional programming style.
The classical example for higher-order functions in Python is the builtin map function. It takes a function object and an iterable, and then
calls the function on each element in the iterable, yielding the results
as it goes along.
Here’s how you might format a sequence of greetings all at once by
mapping the bark function to them:
"""
print(list(map(bark, ['hello', 'hey', 'hi'])))
