"""
Python’s functions are first-class objects. You can assign them to variables, store them in data structures, pass them as arguments to other
functions, and even return them as values from other functions

"""
#defining one yell function which returns string object In UPPER CASE
def yell(text):
    return text.upper() + '!'
    
print(yell('hello'))
#Now creating one varible bark
bark = 0
bark = yell

# now calling bark varible using () operator
print(bark('hello'))

"""Notice something bark is exactly behaveing like yell functions means functions can be assigned to other varible and they are also just objects function objects and their names are two separate concerns. Need proof right see next line  """

del yell

print(bark('Bark still alive whereas yell is dead'))

"""
Python attaches a string identifier to every function at
creation time for debugging purposes. You can access this internal
identifier with the __name__ attribute:2
"""
print(bark.__name__)
# print(yell('hello')) Throw errors NameError: name 'yell' is not defined
