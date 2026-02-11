name = input("Enter your name: ") #input is a in built function
age = int(input("Enter your age: ")) #type casting , as python takes input as string data type so we need to change the data type manually 
print("Your age is", age)
print(type(age)) #because of type casting , it will print (int) as the data type
#if i remove thr type casting , it will print data type as <class 'str'>