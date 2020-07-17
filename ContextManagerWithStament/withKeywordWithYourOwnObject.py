'''
Now, there’s nothing special or magical about the open() function the fact that they can be used with a
with statement. You can provide the same functionality in your own
classes and functions by implementing so-called context managers


What’s a context manager? It’s a simple “protocol” (or interface) that
your object needs to follow in order to support the with statement.
Basically, all you need to do is add __enter__ and __exit__ methods
to an object if you want it to function as a context manager. Python
will call these two methods at the appropriate times in the resource
management cycle.

'''

class ManagedFiles:
    
    def __init__(self,file):
        self.file= file
        
    def __enter__(self):
        self.file = open(self.file,'w')
        return self.file
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

#__enter__ get called             
with ManagedFiles('hello.txt') as f:
    f.write("Hi Dhirendra whats up ?")
    f.write("Bye for Now")

"""
Python calls __enter__ when execution enters the context of the
with statement and it’s time to acquire the resource. When execution leaves the context again, Python calls __exit__ to free up the
resource
"""
