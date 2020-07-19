"""
1 Functions Can Capture Local State
2. Functions that do this are called lexical closures (or just closures, for
short). A closure remembers the values from its enclosing lexical
scope even when the program flow is no longer in that scope.

3. In practical terms, this means not only can functions return behaviors
but they can also pre-configure those behaviors. Here’s another barebones example to illustrate this idea:
"""
def yell(text):
    return text.upper() + '!'
def get_speak_func(text,volume):
    def whisper():
        return text.lower() + '...'
    def yell():
        return text.upper() + '!'
    if volume > 0.5:
        return yell
    else:
        return whisper
        
print(get_speak_func('Hi',.2)())


"""Objects Can Behave Like Functions"""
"""While all functions are objects in Python, the reverse isn’t true. Objects aren’t functions. But they can be made callable, which allows
you to treat them like functions in many case"""

class Adder:
    def __init__(self, n):
        self.n = n
    def __call__(self, x):
        return self.n + x
