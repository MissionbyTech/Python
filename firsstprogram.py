# this is for single line comment ctrl clash 
""" This is for nultiline comment window shift alt a and for mac shift opt a"""

name = "Mission"
age = 20
address = "home" 
#using concate method
print ("My name is " + name + "My age is " +str (age) + "My home is at " +address )
#using F-string
print(f"My name is {name } and My age is  {age} and address is {address}")
#using fofrmat old version method
print ("My name is %s and age is %d and address is %s " %(name, age, address))
# format new version method
print ("My name is {0} and age is {1} address is {2}".format (name, age, address))
#type of the data hold by variable
print (type (name))

# assigning variables 
name = input ("Enter your name" )
age = int (input("Enter the age"))
address = input ("Enter the location ")

#concate nethod 
print ("My Name is " +name + "My age is " +str(age) +"address  is " +address )


num1 = int (input( "Enter  num1 "))
num2 = int (input( "Enter  num2 "))
num3 = int (input( "Enter  num3 "))
num4 = int (input( "Enter  num4 "))

sum1 = num1 + num2 
print ("The sum of num1 and num2 numbers is " +str(sum1))

sum2 = num3 + num4
print ("The sum of num3 and num4 numbers is " +str(sum2))

# True and Fales value 
#if and is used then it return first false if both true then last true value
#if or is used then it return first true if both false then last false value

#membership and identity operators  
a = [1,2,3 ]
b = [1,2,3]
c = a
print (a is b) # false because both are different objects
print (a == b) # true because both have same value
print (a is c) # true because both are same objects
print (id(a)) # it will return the address of a
print (id(b)) # it will return the address of b
print (id(c)) # it will return the address of c

#memory comparison 
#is and in are value comparison operators
print(2**3**2)