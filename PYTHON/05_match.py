#match:
        #match checks a value against different patterns and runs the matching block.

#pass
age=78
if age<18:
    pass 
else:
    print("grant access")

#match
grade = "B"

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Average")
    case _:
        print("Invalid grade")


#Match with multiple options
day = "Saturday"

match day:
    case "Saturday" | "Sunday":
        print("Weekend")
    case _:
        print("Weekday")
        
#with if condition       
num = 15

match num:
    case n if n > 0:
        print("Positive")
    case n if n < 0:
        print("Negative")
    case _:
        print("Zero")


#Match with sequence (lists / tuples)
values = [10, 20]

match values:
    case [x, y]:
        print("Two numbers:", x, y)
    case _:
        print("Different pattern")

#dictionary
person = {"name": "Ammu", "age": 40}
match person:
    case{"name":a,"age":b}:
     print(a,b)
    case _:
        print("pattern mismatch")
