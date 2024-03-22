"""1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line."""
  
# for i in range(2000, 3201):
#     if i%7==0 and i%5 !=0:
#         print(i, end=",")

"""2. With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}"""
# n=8
# new=dict()
# for i in range(n):
#     if i==0:
#         continue
#     else:
#         new[i]=i*i
# print(new)

"""
3. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')"""

# n=input()
# num=tuple(n.split(","))
# tum=list(n.split(","))
# print(num,"\n",tum)

"""
4. Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods."""

# class Newclass:
    
#     def getString(self):
#         string = input("> ")
#         return string
    
#     def printString(self, string):
#         print(string.upper())
        
# def testClassMethods():
#     obj = Newclass()
#     input_string = obj.getString()
#     obj.printString(input_string)

# testClassMethods()


"""5. Write a program that accepts a comma separated sequence of words as input and
prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world"""

# words = input(">")
# word_list = words.split(",")
# sorted_words = sorted(word_list)
# sorted_seq = ",".join(sorted_words)
# print(sorted_seq)  

"""6. Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world"""

# words = input(">")
# word_list = words.split()
# unique_words = list(set(word_list))
# sorted_words = sorted(unique_words)
# sorted_sequence = " ".join(sorted_words)
# print(sorted_sequence)


"""7. Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input."""

# even_numbers = []
# for num in range(1000, 3001):
#     all_even = True
#     for digit in str(num):
#         if int(digit) % 2 != 0:
#             all_even = False
#             break
#     if all_even:
#         even_numbers.append(str(num))
# print(", ".join(even_numbers))

"""8. Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9"""

# sentence = input("> ")
# upper_count = 0
# lower_count = 0
# for char in sentence:
#     if char.isupper():
#         upper_count += 1
#     elif char.islower():
#         lower_count += 1
# print("UPPER CASE", upper_count)
# print("LOWER CASE", lower_count)

"""9. A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1"""

# import re
# def check_password(password):
#     if len(password) < 6 or len(password) > 12:
#         return False
#     if not re.search(r"[a-z]", password):
#         return False
#     if not re.search(r"[0-9]", password):
#         return False
#     if not re.search(r"[A-Z]", password):
#         return False
#     if not re.search(r"[$#@]", password):
#         return False
#     return True

# passwords = input("> ")
# valid_passwords = []
# for password in passwords.split(","):
#     if check_password(password):
#         valid_passwords.append(password)
# print(",".join(valid_passwords))
