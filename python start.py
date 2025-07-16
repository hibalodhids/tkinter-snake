from time import altzone  #pratice set 1
# print('''Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.
#
# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.
#
# Then the traveler in the dark
# Thanks you for your tiny spark,
# How could he see where to go,
# If you did not twinkle so?
#
# In the dark blue sky you keep,
# Often through my curtains peep
# For you never shut your eye,
# Till the sun is in the sky.
#
# As your bright and tiny spark
# Lights the traveler in the dark,
# Though I know not what you are,
# Twinkle, twinkle, little star.
# ''')

                            #ch 2
#arithmetic operator +,-,/,*
# a = 3
# b = 5
# print(a+b)

#assignment operator =, +=,-=,
# a = 2-1
# print(a)
# b = 4
# b += 2 #increament the value of bby 2
# print(b)

#comparsion operator  ==, <,>=,>,<=,!=,
# a = 5<4
# print(a) #return boolean

#logical operator
# d = True and True
# print(d)
# e = True or False
# print(e)
# f = True != True
# print(f)

#TYPE()FUNCTION: is used to find the data type of a variable
# a = "sara"
# t = type(a)
# print(t)

#typecasting
# a = "34.4"
# b = float(a)
# t = type(b)
#print(t)

#input function
# a = int(input("Enter number 1: "))
# b = int(input("Enter number 2: "))
# print("Number a is: ", a)
# print("Number b is:", b)
# print("sum is:", a + b)

                      #pratice set 2

#python program to add two numbers
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# sum = num1 + num2
# print("The sum is: ", sum)

#python program to find reminder when a num divided by z
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# reminder = num1 % num2
# print("The reminder is:", reminder)

#python program to check type of variable using input function
# car = input('Enter car name: ')
# brand = type(car)
# print(brand)

#python program use comparsion operator to find out whether a given variable a is greator than b or not
# a = 34
# b = 80
# c = a > b
# print(c)

#python program to find out the average of two numbers
# a = float(input("Enter a number: "))
# b = float(input("Enter another number: "))
#
# average = (a + b)/2
# print("The average is: ", average)

#python program to calculate square of a number entered by user
# a =int(input("Enter a number: "))
# print("The square of a number is:", a ** 2)
                                   #ch 3"function"
# name = "Harry"
 #slicing
# a = "12345678"
# a = a[2:4:2]
# print(a)
#lenght function
# name = "hiba"
# print(len(name))
#  #start and end switch
# mystring = "harry"
# print(mystring.endswith("rry"))
# print(mystring.startswith("h"))
#string.count()
# string = "HAMZA"
# count = string.count("H")
# print(count)
# #string capitalized()
# s = "hello world"
# capitalized_string = s.capitalize()
# print(capitalized_string)
# #string find(word)
# h = "hello world"
# index = s.find("world")
# print(index)
# #string.replace
# h = "hello world"
# replaced_string = s.replace("world", "python" )
# print(replaced_string)
                    #prtice set 3
#python program to display a user entered a name followed by good afternoon using input function
# name = input("Enter your name: ")
# print(f"Good Afternoon {name}")

#write a program to fill in a letter template given below with name and date.
# letter = '''Dear <|Name|>,
#             you are selected!
#             <|date|>'''
# print(letter.replace("<|Name|>","HARRY").replace("<|date|>","28 september 2005"))

#write a program to detect double space in a string
# name = input("Enter your  name: ")
# print(name.find("  "))
# #replace double space with single space
# print(name.replace("  ", " "))

#write a program to a format  the following letter using space sequence characters
# letter = "Dear harry,\t\n This python course is nice.\nThanks!"
# print(letter)
                           #ch 4 [lists and tuples]
# friends = ["Apple" , "oranges", 34 , 34.6, True]
# print(friends[2])
# print(friends[0 :4: 3]) #slicing
# friends.append("Bob") #adding in list
# print(friends)

# #sort
# hamza= [1,6,9,33,23,45,78]
# # hamza.sort() #sort ascending order
# # hamza.reverse() #reverse
# # hamza.insert(4,55) #insert
# hamza.pop(4)# pop remove the element
# hamza.remove(6)#remove function
# print(hamza)






#tuple
# a = (1, 2, 2, 4)
# print(type(a))#type tuple
# a = ()
# print(a) #empty tuple
# a = (1,)#single element tuple return type
# print(type(a))
# a = (1 , 23 ,456, 23 ,33, 66)
# a[0] = 12 #tuple cannot be change
  #tuple method
# a = (1 , 23 ,456, 23 ,33, 66, "sara")
# no = a.count("sara")#count element
# print(no)
                               #pratice set
#write a python program to store seven fruits in a list entered by user
# fruit = []
# f1 = input("Enter the 1 fruits : ")
# fruit.append(f1)
# f2 = input("Enter the 2 fruits : ")
# fruit.append(f2)
# f3 = input("Enter the 3 fruits : ")
# fruit.append(f3)
# f4 = input("Enter the 4 fruits : ")
# fruit.append(f4)
# f5 = input("Enter the 5 fruits : ")
# fruit.append(f5)
# f6 = input("Enter the 6 fruits : ")
# fruit.append(f6)
# f7 = input("Enter the 7 fruits : ")
# fruit.append(f7)
# print(fruit)

# typecasting
# v = int(3.5)
# c = int("2")
# s = int(2)
# print(v)
# print(c)
# print(s)
#
# apple = float(2)
# banana = float("3")
# orange = float("4.9")
# print(apple)
# print(banana)
# print(orange)
#
# s = str("4")
# u = str(4)
# w = str(3.9)
# print(s)
# print(u)
# print(w)

#python string
# print("hello world")
# print('hello world')
#quotes inside quotes
# print("he is called 'John'")
# print("it's is alright")
# print('he is called "johnny"')
#assigning string to a variable
# a = "hello world"
# print(a)
#multi-line string
# a = """Then the traveler in the dark
#      Thanks you for your tiny spark,
#      How could he see where to go,
#      If you did not twinkle so?"""
# print(a)
#3 single quotes
# a = '''Then the traveler in the dark
#      Thanks you for your tiny spark,
#      How could he see where to go,
#      If you did not twinkle so?'''
# print(a)
#looping through strings
# for x in "banana":
#     print(x)

#slicing string
# a = "hello world"
# print(a[1:7:2])
# b = "hello world"
# print(b[:5])
# c = "hello world"
# print(c[2:])
# d = "hello world"
# print(d[-5:-2])

#modify upper case
# a = "hi!you are beautifull"
# print(a.upper())
# a = "hi!you are beautifull"
# print(a.lower())
# #replace string
# b =  "hi!you, are beautifull"
# print(b.replace("y", "n"))

#split string
# a = "jello , go away"
# print(a.split(","))

# #dictionary: are used to store data values in key:value pairs .They are unordered , changeable and donot  allow duplicate keys
# dict = {
#     "key" : "value",
#     "name" : "hiba",
#     "learning": "coding",
#     "age" :56,
#     "marks" : 34.7,
#     "adult" : True,
#     "list" : [1,2,3,4,5],
#     "tuple" : ("dict","set")
# }
# print(dict)
# print(type(dict))
# print(dict["age"])
# dict["age"] = 66
# dict["animal"] = "dog"
# print(dict)

#creating null dictionary
# s = {}
# print(s)

#nested dictionary
info = {
   " name ": "arish",
   " subject" : {
       "math" : 77,
       "urdu" : 99,
       "science" : 90
   }
}
print(info)
print(info[" subject"]["science"])
print(info.keys())
print(len(info))
print(info.values())
print(info.items())