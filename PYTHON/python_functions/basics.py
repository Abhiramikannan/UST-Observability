#parameter and argument
#parameter: a variable listed inside paranthesis in the function definition
#Argument: Actual value that we are passing for that variable
#creating python function
def myfun():
    print("Hello")
myfun() # calling a function

# y use python functions:
    # if u want to convert celsius to fahrenheit in many times in your code.. code will repete.. so declare function and write line of code inside it and call it whenever u need.
        #reduce time, and repetition of code.

#fahrenheit to celsius
def fahrenheit_to_celsius(fahrenheit): # parameter passed
    celsius=(fahrenheit-32)*5/9
    return celsius
print(fahrenheit_to_celsius(80)) #gave parameter value here
print(fahrenheit_to_celsius(50))

#Function with one argument
def my_fun(name): # name is parameter
    print(name + " is a student")
my_fun("abhi") #abhi is argument

#default parameter values
def country_name(name="norway"): #setting default value
    print(name)
country_name("India")
country_name() #defaultly output will be norway.. no argument given

#key word arguments
#you can also sent key = value arguments
def animal_name(name,animal):
    print("i have a "+ animal)
    print("my animal name is "+ name)
animal_name(name="leo",animal="cat") #key=value

#positional arguments
#calling function without using keyword
def animal_name1(name,animal):
    print("i have a "+ animal)
    print("my animal name is "+ name)
animal_name1("leo","cat") # no key=value

#sending list as an argument
def fruits_name(a): # only 1 parameter i. e, the list named fruits
    for x in fruits:
        print(x)
fruits=["apple","orange","banana"]
fruits_name(fruits) # passed that list here as an argument

# A function that returns a list
def fruits_func():
    return ["apple","orange"]
fruits=fruits_func()
print(fruits[0])
print(fruits[1])

#positional only arguments: Only allowed to use positional arguments
def name_fun(name,/):#/ is used to allow only positional args
    print(name)
name_fun("abhi")

#keyword only arguments: with keyword only allowed
def name_func(*,name):
    print(name)
name_func(name="abii")


#arbitrary arguments-args(*) : If u dont knw how many arguments are passed you can use * before in the parameter
def fru(*fruittss):
    print(fruittss)
fru("apple","orange","banaana")

#kwargs: if u dont know how many keyword arguments used -use **

