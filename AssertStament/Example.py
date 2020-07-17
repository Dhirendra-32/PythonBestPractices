# Syntax assert_stmt ::= "assert" expression1 ["," expression2]
# function to show assert behaviour
def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    print(price)
    return price
    
# product Information
shoes = {'name': 'Fancy Shoes', 'price': 14900}

# it will work
"""discounted prices calculated by this function cannot be lower than 0 and they cannot be higher than the original price of the product"""

apply_discount(shoes,.25)

# Throw error exception
"""You can also see how the exception stacktrace points out the exact line
of code containing the failed assertion. If you (or another developer
on your team) ever encounter one of these errors while testing the
online store, it will be easy to find out what happened just by looking
at the exception traceback."""
apply_discount(shoes,2)



"""Equivalent code How python internally check this assert statement:

if __debug__:
    if not expression1:
        raise AssertionError(expression2)


"""
