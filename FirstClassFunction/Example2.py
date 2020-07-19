""" Functions Can Be Stored in Data Structures How ? see below implements
Since functions are first-class object or say varible, you can store them in data
structures just you do with other variable or object  """

#defining one yell function which returns string object In UPPER CASE
def yell(text):
    return text.upper() + '!'
    
print(yell('hello'))
bark = yell
print(bark('hello'))

funcs = [bark, str.lower, str.capitalize]# all three are functions will loop on it
print(funcs)#[<function yell at 0x00000158536671F0>, <method 'lower' of 'str' objects>, <method 'capitalize' of 'str' objects>

# funcs[0]('heyho')
for f in funcs:
    print(f,f("hi dhirendra"))
