#while loop
i=1 #initialize
while i<10:  #condition
    print(i)
    i=i+1 #increment
#break
#exit the loop when i=3
i=1 #initialize
while i<10:  #condition
    print(i)
    if i==3:
        break  #1,2,3 will be output
    i=i+1 #increment


#continue : skip the current iterationa and continue with next
i=0
while(i<10):
    i=i+1
    if(i==3):
        continue
    else:
        print(i)


#forloop
#1. print each fruit in the fruit list
fruits=["apple","orange","mango"]
for a in fruits:
    print(a)

#2. iterating through string
for x in "banana":
    print(x)

#3. break statement
for x in fruits:
    if x=="orange":
        break
    else:
        print(x)

#4. continue statement : dont print orange
for x in fruits:
    if x=="orange":
        continue
    else:
        print(x)

#5. range() function
for x in range(6):
    print(x) # 0 to 5

for x in range(2,6):
    print(x) # 2 to 5

for x in range(1,10,2):
    print(x) # 1 to 9 which skips 1 value b/w  (1+2=3+2=5+2=7+2=9)


#6. pass statement = for loop actually cannot be empty,but if u have no content then put pass to neglect the error in python.
for x in [0,1,2]: # list of numbers
    pass # will pass the statement(skip)
    
   
   




   
