#one dimension array
# import numpy as np
# fruit = np.array([1 , 2, 3])
# print(fruit)

# two dimension array
# import numpy as np
# fruit = np.array([[1,2,3],
#                  [4,5,6],#matrics
#                  [7,8,9]])
# print(fruit)

#multi dimension array
# import numpy as np
# fruit = np.array([[2,4,6],
#                   [1,4,7]])
# print(fruit)

#creating array from python lists
#np.array([ ele 1 , elem 2, elem 3, elem 4])
# import numpy as np
# arr = np.array([1,2,3,4,5])
# print(arr)

#with default values
# #np.zeros(shape)
# import numpy as np
# zeroes_array = np.zeros(5)
# print(zeroes_array)

#ones(shape)
# import numpy as np
# ones_array = np.ones((3,4))
# print(ones_array)

#full(shape)
# import numpy as np
# full_array = np.full((3,4),4)
# print(full_array)

#arrange(start,stop,step)
# import numpy as np
# arr = np.arange(1,15,3)
# print(arr)

#creating identity matrix
# import numpy as np
# identity_matrix = np.eye(4)
# print(identity_matrix)
                        #ch 2
#shape of array
# import numpy as np
# arr = np.array([[1,2,4,6,8],
#                 [1,2,4,7,8]])
# print(arr.shape)

#reshape of array
# import numpy as np
# hiba = np.array([98, 70, 60, 72, 40, 67])
# new_array = hiba.reshape(3,2)
# print(new_array)

#size of array
# import numpy as np
# hamza = np.array(([2, 5, 7, 7],[2,4,7,89]))
# new_hamza = hamza.size
# print(new_hamza)

#ndim dimension check
# import numpy as np
# arr1 = np.array([1,2,3,4,5])
# arr2 = np.array([[1,2,3,4,5],[1,2,3,4,5]])
# arr3 = np.array([[[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]])
#
# print(arr1.ndim)
# print(arr2.ndim)
# print(arr3.ndim)

#dtype
# import numpy as np
# arr = np.array(["33.7, 11.0 ,33.7, 22.4" ])
# print(arr.dtype)

# import numpy as np
# arr = np.array([1,2,3,4])
# new_arr = arr.astype(float)
# print(new_arr)
# print(new_arr.dtype)

#operation on array
# import numpy as np
# arr = np.array([1,2,3,4,5])
# print(arr+5)
# print(arr-5)
# print(arr*5)
# print(arr/5)
# print(arr%5)
# print(arr**5)

#aggregation function
# import numpy as np
# var = np.array([1,2,3,4,5])
# print(np.sum(var))
# print(np.max(var))
# print(np.min(var))
# print(np.mean(var))
# print(np.median(var))
# print(np.std(var))
# print(np.var(var))

#indexing
# import numpy as np
# arr = np.array([12,32,56,87,90])
# print(arr[1])
# print(arr[-1])
# print(arr[4])

#slicing
#arr = (start:end:step)
# import numpy as np
# arr = np.array([10,20,30,40,50])
# print(arr[1:5:2])
# print(arr[:2])
# print(arr[1:5])
# print(arr[::-2])
# print(arr[::2])

#fancy indexing
# import numpy as np
# arr = np.array([10,20,30,40,50])
# print(arr[[0,3,4]])

#filtering data boolean masking
# import numpy as np
# arr = np.array([10,20,30,40,50])
# print(arr[arr<20])
# print(arr[arr>=30])

#.ravel() - views modification in original array
#.flatten()-copy no modification in original array
# import numpy as np
# arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(arr.view())
# print(arr.copy())

#inserting()
# import numpy as np
# arr = np.array([1, 2, 3])
# print(arr)
# new_arr = np.insert(arr, 3,46,axis=0)
# print(new_arr)
# arr2 = np.array([[1,2],[4,5]])
# new_arr2 = np.insert(arr2, 1,[8,9],axis=0)
# print(new_arr2)

#concatenate
# import numpy as np
# arr = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# new_arr = np.concatenate((arr,arr2))
# print(new_arr)
#
# #append()
# import numpy as np
# arr = np.array([1,2,3])
# new_arr = np.append(arr,[45,67,98])
# print(new_arr)

#np.delete(array, index, axis = none)
# import numpy as np
# arr = np.array([1,2,3,4,5])
# print(arr)
# new_arr = np.delete(arr, 2)
# print(new_arr)
# arr2 = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
# new_arr2 = np.delete(arr2, 1,axis=0)
# print(new_arr2)

# from numpy import random
# a = random.randint(3) #int
#
# print(a)
# from numpy import random
# d = random.rand() #float
# print(d)
# from numpy import random
# rand = random.randint(10,size=(5))
# print(rand)
# from numpy import random
# s = random.randint(10,size=(3,4)) #2 dimension array
# print(s)
# from numpy import random
# a = random.rand(5)
# print(a)

# from numpy import random
# a = random.rand(3,5)
# print(a)
#choices
# from numpy import random
# a = random.choice([2,3,4,5])
# print(a)
# from numpy import random
# x = random.choice([3, 5, 7, 9], size=(3, 5))
# print(x)
#random distribution
# from numpy import random
# a = random.choice([2,3,4,5], p=[0.1, 0.2, 0.3, 0.4], size=20)
# print(a)
# from numpy import random
# a = random.choice([2,3,4,5], p=[0.1, 0.2, 0.3, 0.4], size=(4,4))
# print(a)

#random shuffle
# from numpy import random
# import numpy as np
# arr = np.array([1,2,3,4,5])
# random.shuffle(arr)
# print(arr)

#permutation
# from numpy import random
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# print(random.permutation(arr))


                               #project 1
# import numpy as np
# sec_num = np.random.randint(1,20)
# # print(sec_num)
#
# while True:
#     try:
#         guess = int(input("Enter your guess: "))
#         if guess < 1 or guess > 20:
#             print("please enter a number between 1 and 100")
#         elif guess < sec_num:
#             print("you guessed too low")
#         elif guess > sec_num:
#             print("you guessed too high")
#         else:
#             print(f"you guessed correctly{sec_num}")
#             break
#     except ValueError:
#         print("invaild input")


              #python project 2
# import numpy as np
# #
# nouns = ["sana" , "car" , "lion" , "house" , "star" , "chair"]
# verbs = ["dance" , "move" , "watch" , "sleep" , "eat" , "play"]
# adjectives = ["beautiful" , "co]orful", "full" , "handsome" , "rude" ," circle"]
#
# for i in range(6):
#    noun = np.random.choice(nouns)
#    verb = np.random.choice(verbs)
#    adjective = np.random.choice(adjectives)
#
#    print(f"The {adjective} {noun} {verb}.")


                        #project1
# import numpy as np
# hidden_num = np.random.randint(1,10)
# print(hidden_num)
#
# while True:
#     try:
#         choice = int(input("Enter your choice: "))
#         if choice >= 1 and choice <= 10:
#             print("plz enter a number between 1 and 10")
#         elif choice < hidden_num:
#             print("you guessed too low")
#         elif choice > hidden_num:
#             print("you guessed too high")
#     else:
#     print(f"you guessed correctly{hidden_num}")
#     break
# except ValueError:
# print("invalid input")


                       #rock, paper ,secsisor
# import numpy as np
#
# opt = ["Rock", "Paper", "Scissor"]
# print('Welcome to my game (Rock, Paper, Scissor)!')
#
# while True:
#     try:
#         user_choice = input("Enter your guess: ").capitalize()
#
#         if user_choice not in opt:
#             print("Invalid choice, try again!")
#             continue  # This was misplaced in your code
#
#         comp_choice = np.random.choice(opt)
#
#         print(f"Computer 💻 chooses: {comp_choice}")
#         print(f"Hiba chooses: {user_choice}")
#
#         if comp_choice == user_choice:
#             print("It's a tie!")
#         elif (user_choice == "Rock" and comp_choice == "Scissor") or \
#                 (user_choice == "Paper" and comp_choice == "Rock") or \
#                 (user_choice == "Scissor" and comp_choice == "Paper"):
#             print("You win! 🎉")
#         else:
#             print("You lose 😢")
#
#     except Exception as e:
#         print("An error occurred:", e)


# import numpy as np

# options = ["Rock", "Paper", "Scissor"]
# user_score = 0
# comp_score = 0

# print("🎮 Welcome to Rock, Paper, Scissor Game 🎮")

# while True:
#     user_input = input("\nEnter your choice (Rock, Paper, Scissor or Q to quit): ").capitalize()

#     if user_input == "Q":
#         print("\nGame Over!")
#         print(f"Final Score → 👤 You: {user_score} | 💻 Computer: {comp_score}")
#         break

#     if user_input not in options:
#         print("❌ Invalid choice. Please choose Rock, Paper, or Scissor.")
#         continue

#     comp_choice = np.random.choice(options)
#     print(f"💻 Computer chose: {comp_choice}")
#     print(f"👤 You chose: {user_input}")

#     if comp_choice == user_input:
#         print("🤝 It's a tie!")
#     elif (user_input == "Rock" and comp_choice == "Scissor") or \
#          (user_input == "Paper" and comp_choice == "Rock") or \
#          (user_input == "Scissor" and comp_choice == "Paper"):
#         print("🎉 You win this round!")
#         user_score += 1
#     else:
#         print("😢 You lose this round.")
#         comp_score += 1

#     print(f"📊 Current Score → You: {user_score} | Computer: {comp_score}")


#math operation



import numpy as np
score = 0
total_question = 5

for i in range(total_question):
   num1 = np.random.randint(1,10)
   num2 = np.random.randint(1,10)
   operation = np.random.choice(['+', '-', '*', '/'])

   if operation == '+':
      sol = num1 + num2
   elif operation == '-':
      sol = num1 - num2
   elif operation == '*':
      sol = num1 * num2
   elif operation == '/':
      sol = num1 / num2

   try:
      user = input(f"Q{i+1}:What is {num1} {operation} {num2}?")

      if user == sol:
         print("Correct!")
         score += 1
      else:
         print("Wrong!")
   except ValueError:
      print("Invalid input! Please enter a number.")
      print(f"ypor total score:{score} out of total question:{total_question}")

# from numpy import random
# import numpy as np

# arr = np.array([1, 2, 3, 4, 5])

# print(random.permutation(arr))
# import seaborn as sns
# import matplotlib.pyplot as plt
# x = [1, 2, 3, 4]
# y = [10, 20, 25, 30]

# # plt.plot(x,y) line chart
# # plt.bar(x, y) bar chart
# plt.scatter(x, y) 


# 


# data = [55, 60, 65, 70, 70, 72, 75, 78, 80, 82, 85, 90, 95]
# data = [1,2,2,3,4,5,6,7,8,9,10]
# plt.hist(data, bins=5,color='skyblue',edgecolor='black')  # 5 bars (bins)
# plt.title("scatter chart")
# plt.xlabel("x value")
# plt.ylabel("y value")
# plt.show()




# import seaborn as sns
# import matplotlib.pyplot as plt

# cake = ["chocalate cake" ,"vanilla cake" , "cofee cake","pinapple cake"]
# sales = [120,400, 500,300]
# plt.figure(figsize=(7,7))
# plt.pie(sales,labels=cake,autopct='%1.1f%%')
# plt.title("cake sales - pie charts")
# plt.show()



# import seaborn as sns
# import matplotlib.pyplot as plt

# x = ["orange juice","mango juice","strawberry juice"]
# y = [120 ,140,170]
# plt.figure(figsize=(7,7))
# plt.line(x, y)
# # plt.xlabel(juices)
# # plt.ylabel(sales)
# plt.show()



# import seaborn as sns
# import matplotlib.pyplot as plt

# subjects = ['math' ,'urdu','science']
# marks  = [34,56,78]

# sns.barplot(x=subjects, y=marks)

# plt.xlabel("subjects")
# plt.ylabel("marks")









