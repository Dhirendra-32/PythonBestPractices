# Question is how withKeyWord is attached to open function and how you can use it with your own function

# will simply create file
'''
with open('hello.txt', 'w') as f:
    f.write('hello, world!')

'''
# Intenally treated by python is
'''
f = open('hello.txt', 'w')
try:
    f.write('hello, world')
finally:
    f.close()
'''
