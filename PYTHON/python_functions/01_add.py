#adding 2 numbers using functions

def add(a,b):
    c=a+b
    print(c)

add(4,4)

#return is used to store the value into variable outside function =return returns/fetches the result
def add1(a,b):
    c=a+b
    return c #returns the value and we can do whatever we want
    
result=add1(5,6) #storing the c value returned into result
print("The result is ", result)
