first_name = "testing"
last_name = "name"
full_name = (first_name +" "+ last_name)

print ("hello "+full_name)

age = 99
age += 1
print ("The age of this object is "+ str(age))
print(type(age))

height = 21.6
print ("The height of this object is: "+str(height)+"cm")
print (type(height))

connected = False
print("Are these wires connected? "+str(connected))


name = "frank"
age = 100
ugly = True

name, age, ugly = "frank", 100, True

print (name)
print(age)
print(ugly)




Patrick = Spongebob = Squidward = MrKrabs = 30

print (Spongebob)
print (Squidward)
print (Patrick)
print (MrKrabs)

#string methods
name = "PeTer"

print(len)name)
print (name.find("t"))
print(name.capitalize())
print (name.upper())
print (name.lower())
print (name.isdigit())
print (name.isalpha())
print (name.count("r"))
print (name.replace("e","o"))
print (name*11)

#type casting - convert the data type of a value to another data type


x = 6
y = 2.1
z = "10"

int(y)
x = float(x)
y = float(y)
z = float(z)
print(x)
print(y)
print(z*3)
print ("x is "+str(x))
print ("y is "+str(y))
print ("z is "+str(z))



name = input("What is your name? ")
age = int(input("What is your age? "))

height = float(input("What is your height?"))

print("Hello there, "+name)
print("Your age is "+ str(age) + " years old")
print ("You are "+str(height) + " centimeters tall.")


#Math functions
import math

pi = 3.14
x = 1
y = 2
z = 3
print (round(pi)) #This rounds the number.
print (math.ceil(pi)) #This will round UP to the nearest full integer.
print (math.floor(pi)) #This will round DOWN to the nearest full integer.
print (abs(pi)) #Absolute value.
print (pow(pi, 2)) #Raises a number to a power.
print (math.sqrt(pi)) #Finds the square root.
print(max(x,y,z)) #Finds the highest number of each number.
print (min(x,y,z)) #Finds the lowest number of each number.

#slicing - creating a substring by extracting elements from another string.
#                   indexing [] or slice ()
#                   [start:stop:step]

name = "Test Name"
last_name = name[5:9]
first_name = name[0:3]
weird_name = name[0:9:2] #if step is at 1 then it displays each character. If it's at 2 it displays every 2nd character and so on.
reverse_weirdname = name[::-1]

print (first_name)
print (reverse_weirdname)

website = "http://facebook.com"
slice = slice(7,-4)
print (website[slice])
print (website)



# if statements - a block of code that will only execute if its condition is met

age = int(input("How old are you? "))


if age == 1000:
    print("You are extremely old!")

elif age >= 100:
    print("You are old")
elif age < 0:
    print ("You haven't been born yet!")
else:
    print("You are not old")








