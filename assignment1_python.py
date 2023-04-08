# Write a program to display only those numbers from a list that satisfy the following conditions

# - The number must be divisible by five

# - If the number is greater than 150, then skip it and move to the next number

# - If the number is greater than 500, then stop the loop
# ```
# numbers = [12, 75, 150, 180, 145, 525, 50]

numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if(i > 150 and i<500):
        continue
    if(i > 500):
         break
    if(i%5==0):
        print(i)


    





#Write a code to take 3 numbers as an input from the user and display the greatest no as output.
# print ("enter three numbers")
# a= int(input())
# b= int(input())
# c= int(input())

# if a>b and a>c:
#     print("the greatest number is ", a)
# elif b>a and b>c:
#     print("the greatest number is ", b)
# elif c>a and c>b:
#     print("the greatest number is ", c)
# else:
#     print("none is the only greatest")

#calculating the sum of even numbers in the given list

# numbers = [12, 75, 150, 180, 145, 525, 50]
# sum=0
# for i in numbers:
#     if(i%2==0):
#         sum=sum+i

# print ("sum of even numbers in the list=", sum)
# age = int(input("enter your age"))
# if age >= 18:
#     print("I can Vote")
# else:
#     print("I can't vote")
# a =1 or 0           # will return 1

# b = 0 and 0         # will return 0

# c = True and False and True # will return False

# d = 1 or 0 or 0             # will return 1

# print(a)
# print(b)
# print(c)
# print(d)
# str_var = 'iNeuron'
# str_var = str_var * 4
# print(str_var)
# # a = input("enter the name")
# # b = input("enter the age")
# # print(a)
# # print(b)

# # Python program showing how to
# # multiple input using split

# # taking two inputs at a time
# x, y = input("Enter two values: ").split()
# print("Number of boys: ", x)
# print("Number of girls: ", y)

# # taking three inputs at a time
# x, y, z = input("Enter three values: ").split()
# print("Total number of students: ", x)
# print("Number of boys is : ", y)
# print("Number of girls is : ", z)

# # taking two inputs at a time
# a, b = input("Enter two values: ").split()
# print("First number is {} and second number is {}".format(a, b))

# # taking multiple inputs at a time
# # and type casting using list() function
# x = list(map(int, input("Enter multiple values: ").split()))
# print("List of students: ", x)
