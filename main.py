# x = input("Enter your name: ")
# y = input("Enter your age: ")
# print('Hi' + x + "! You are " + y)
#
# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# #result = int(num1) + int(num2) # int cannot use decimal ex. 2.2
# result = float(num1) + float(num2)

# print(result)

# color = input('Enter a color: ')
# plural_noun = input("Enter a Plural Noun: ")
# celebrity = input("Enter a celebrity: ")
#
#
# print("Roses are " + color)
# print(plural_noun + " are blue")
# print("I love " + celebrity)

# lucky_numbers = [4,1,3,6,16,23,56]
# friends = ["Alex", "Sean", "Kenneth","Daniel","Ben"]
# friends.sort()
# print(friends)

# coord = (4,5) # this is a tuple() and above is a list[]. Once create tuple cannot change it, list can change. Tuple immutable and list mutable
# coord[1] = 10 # this will not work as tuple cannot change

# def sayhi(name,age):
#     print('Hello ' + name + ", you are " + str(age))
#
# sayhi('Gerard', 30)

#
# def cube(num):
#     return num*num*num
#     print('ssss') #This would not print out as return above and nothing will print after return
#
# result = cube(4)
# print(result)

# is_male = False
# is_Tall = True
#
#
# if is_male and is_Tall:
#     print("You are a Tall male")
# elif is_male and not(is_Tall):
#     print("You are a short male")
# elif is_Tall and not(is_male):
#     print("You are tall")
# else:
#     print("You are neither male or tall ")

# def max_num(num1, num2, num3):
#     if num1>= num2 and num1 >= num3:
#         return num1
#     elif num2>= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
#
# print(max_num(333,42,2152))


# num1 = float(input("Enter first number: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter second number: "))
#
# if op == '+':
#     print(num1+num2)
# elif op == '-':
#     print(num1 - num2)
# elif op == '*':
#     print (num1*num2)
# elif op == '/':
#     print(num1/num2)
# else:
#     print('Invalid operator')
#

# monthConversions = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     "Nov": "November",
#     "Dec": "December",
# }
#
#
# print(monthConversions.get("Dec"))
# print(monthConversions.get("Uis","not a valid value"))

# secret_word = "giraffe"
# guess = ""
# count = 0
# limit = 3
# out_of_guesses = False
#
# while guess != secret_word and not(out_of_guesses):
#     if count < limit:
#         guess = input("Enter guess: ")
#         count +=  1
#     else:
#         out_of_guesses = True
#
# if out_of_guesses:
#     print("Out of guesses. You lose!")
# else:
#     print('You win!')

# friends = ["Alex", "Sean", "Kenneth","Daniel","Ben"]
# # for index in range(len(friends)):
# #     print(friends[index])
#
# for index in range(5):
#     if index == 0:
#         print('First Iteration')
#     else:
#         print("Not first")

# def raise_to_power(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result = result*base_num
#     return result
#
# print(raise_to_power(2,4))
#
# number_grid = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [0]
# ]
#
# # print(number_grid[2][1]) # row first then column (index starts with 0, hence 2nd row 1st column is 8
#
# for row in number_grid:
#     for col in row:
#         print(col)

#


# Giraffe language translator, all vowels become gg
# def translate(phrase):
#     translation = ''
#     for letter in phrase:
#         if letter.lower() in "aeiou":
#             if letter.isupper():
#                 translation = translation + 'G'
#             else:
#                 translation = translation + "g"
#         else:
#             translation = translation + letter
#     return translation
#
# print(translate(input('Enter a phrase:')))


# try:
#     value = 10 / 0
#     number = int(input("Enter a number: "))
#     print(number)
# except ZeroDivisionError:
#     print("Divided by zero")
# except ZeroDivisionError as err:
#     print(err)
# except ValueError:
#     print("Invalid Input")


# employee_file = open("employees", 'r') #r is read, r+ is read and write
#
# for employee in employee_file.readlines():
#     print(employee)
#
# # print(employee_file.readlines()[1])
#
# employee_file.close()


# employee_file = open("employees", 'w') # a for append # w will overide the whole file and add what you wanted
#
# employee_file.write('\nKelly - HR')
#
# employee_file.close()


# import useful_tools
#
# print(useful_tools.me)


# import docx


# from Student import Student
#
# student1 = Student("Jim", "Business", 3.1, False ) #An object is an instance of class. An bject is an actual student with actual information
# student2 = Student("Pam", "Art", 3.3, True )
#
# print(student2.gpa)


# from Question import Question
#
# question_prompts = [
#     "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
#     "What color are bananas?\n(a) Teal\n(b) Magneta\n(c) Yellow\n\n",
#     "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
# ]
#
# questions = [
#     Question(question_prompts[0], 'a'),
#     Question(question_prompts[1], 'c'),
#     Question(question_prompts[2], 'b'),
# ]
#
# def run_test(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.prompts)
#         if answer == question.answer:
#             score += 1
#     print(f'You got {score}/{len(questions)} correct')
#
# run_test(questions)

# def run_test(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.prompts)
#         if answer == question.answer:
#             score += 1
#     print("You got " + str(score) + '/' + str(len(questions)) + ' correct')
#
# run_test(questions)
#
#


# from Student import Student #take note of 'from _____ import _______ ' format used
#
# student1 = Student("Jim", "Engineering", 3.2, None)
# student2 = Student("Mike", "Art", 3.7, None)
#
# print(student1.on_honor_roll())



from Chef import Chef
from ChineseChef import ChineseChef

myChef = Chef() #This is just making Chef() into myChef for easier call
myChef.make_salad()

myChineseChef = ChineseChef()
myChineseChef.make_special_dish()