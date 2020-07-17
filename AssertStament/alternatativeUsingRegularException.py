x = input("Enter x Value")

print("X value is "+x)
if x =='Yes':
    print(x)
    
elif x =='No':
    print(x)
else:
    assert False,"Something went wrong"

# Note: Never use it for  data validation always use it to check condition which never arises 
