#instance method

class Student:

    #step 3: Defining a global/Class variable
    School="dominics"

    #step 1
    def __init__(self,m1,m2,m3): #pass values from user
        self.m1=m1 #m1,m2,m3 are instance variables
        self.m2=m2
        self.m3=m3
    
    #step 4: calculate avg of marks
    def avg_marks(self): #instance method which works with the object
        return(self.m1+self.m2+self.m3)/3
    
    #step 6: To get m1 value(Accessors/Getters)
    def get_M1(self):
        return self.m1
    
    #step 7: To set the value of m1(Mutators/setters)
    def set_M1(self,value):
        self.m1=value
    



#step 2: lets create object for this
s1=Student(34,44,32) #passing values here
s2=Student(43,54,33)


#step 5 : printing
print(s1.avg_marks())
print(s2.avg_marks())


#instance method: Because we are passing self..so this belongs to a particular object.
#in instance method u have 2 methods
        # Accessor methods: to fetch the instance variables use accessors
        # Mutator methods: To modify the value of instance variable use mutators.


# Getters(Accessors) and setters(Mutators):
#     Getters get the Value 
#     Setters sets the Value
