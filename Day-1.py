name ="Edbin Khanal"
age =17

print(f"Name: {name} and Age: {age} ")           #Ways for printing the output
print("Name: " +name + " and Age: "+ str(age))
print("Name: %s and Age: %d" %(name, age))
print("Name: {0} and Age: {1}" .format(name, age))

name1= input("Enter your name: \n")         #Ways to take input from user
age1= int(input("Enter your age: \n"))

print(f"Name: {name1} and Age: {age1} ")

print(type(name1))   #Ways to check the data type of a variable
print(type(age1))
