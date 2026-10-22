# # def ikram():
# #     print("my name is ikram ali.")
# # ikram()

# # def sum(a, b):
# #     result=a+b
# #     print(result)
# # sum(1,3)
# # sum(35,53)
# # def multiply(a,b):
# #     mul=a*b
# #     return mul
# # print(multiply(3,2))

# #average of three numbers

# # def average(a,b,c):
# #     avg=(a+b+c)/3
# #     print("Average of Three numbers :",avg)

# # average(2,3,2)

# # def greet_user(nae):
# #     print("Hello " + nae + "! Welcome to the training.")
# # greet_user('ikram ali')

# # def square(num):
# #     print(f"Square of {num} :",num*num)
# #     return (num*num)
# # square(6)

# # def find_MAX(a,b):
# #     if a>b:
# #         print(f"{a} is greater than {b}")
# #         return a
# #     else:
# #         print(f"{b} is greater than {a}")
# #         return b
# # find_MAX(34,5)
# # find_MAX(33,333)
# # print(find_MAX(3,-4))
# # def check_even_odd(num):
# #      if num % 2 == 0:
# #           print("The number is Even")
# #           return "Even"
# #      else:
# #          print("The number is Odd")
# #          return "Odd"
     

# # check_even_odd(3)
# # check_even_odd(30)
# # check_even_odd(3212)
# # print("The number is : ",check_even_odd(20))

# # def sum_list(numbers):
# #     total=0
# #     for num in numbers:
# #         total += num
# #     return total
# # print("The Total Sum of a List:",sum_list([3,2,3,4,5,1]))

# # def count_vowels(word):
# #     count = 0
# #     vowels='aeiouAEIOU'
# #     for char in word:
# #         if char in vowels:
# #             count +=1
# #     return count
# # print("Number of vowels in word : ",count_vowels("Ikraam ali"))
# # multiply=int(input("Enter the value :"))
# # def multiply(a,b):
# #     return a*b
# # print(multiply(2,3))

# # def count(lst):
# #     freq={}
# #     for item in lst:
# #         freq[item]= freq.get(item,0)+1
# #         return freq
# # print(count(["s","a","b","ec","a"]))
# # def eqal():
# #     print("My name is ikram ali")
# # eqal()

# # def while_f1(a):
# #     count=0
# #     while a<=20:
# #         print("My name is python! ",end="😍 ")
# #         a +=1
        
# # while_f1(1)
# # print("hi")
# # print("hello",end=" ")
# # list=['ik',34,33,'ee',33]
# # list1=['mt','tr',45]
# # def length_of_lst(list):
# #     print("Length of list :",len(list))
# #     return len(list)
# # # length_of_lst(['ikram ali' ,'parvez', 454.4,45
# # (length_of_lst(list))
# # (length_of_lst(list1))
# # tup=(1,2,3,4,5,6,7,8,9,10,4,3,3,4,55,5,3)
# # i=0
# # x=3
# # while i < len(tup):
# #     if tup[i]==x:
# #         print("Found the x :",3)
# #         break 
# #     else:
# #         print("Finding..........")    
# #     i+=1
# # print("Loop is Ended:")


# # #ques 
# # print(len(tup))
# # i=1
# # while i<= 20:
# #     if (i%2! =0):
# #         i+=1
# #         continue
# #     print(i)
# #     i+=1
# # num=[1,4,9,16,25,36,49,64,81,100,49,345,49]
# # # for i in range (len(num)+1):
# # #     print(num[i])
# # #     i+=1
# # # print("loop is terminated")
# # x=49
# # idx=0
# # for ele in num:
# #     if (ele==x):
# #         idx+=1
        
# #         print("Index of x :",idx)
        
# #     idx +=1
# # print("Loop is Ended.")  
# # for inp in range (2 ,101,2):
# #     print(inp)
# # print("loop is ended")


# # for i in range(100):
# #     print(i)

# # n=int(input("entet the Number :"))
# # for i in range(1,11):
# #     print(f"{n} * {i} = ",n*i)
# # print("loop is ended.")

# # for i in range(34):
# #     pass
# # print("er")
   
# # n=int(input("Enter the natural number : "))
# # total=0
# # while i <= n :
# #     total=total+i
# #     i +=1
# # print("Total sum : ",total)
# # # print("Loop is finish")
# # n=int(input("Enter the first n natural numbers : "))
# # a=0
# # fo
# # r facto in range(n,0,-1) :
# #     a=a+facto*(n-1)
# # print(f"Foctorial of {n} = ",a)
# '''n=5
# fact=1
# for i in range(n,0,-1):
#     fact *=i
#     print(fact)
# print("Factoraial = ", fact)

# n=int(input("Enter the any numbers : "))
# facto=1
# i=1 
# while i <= n:
#     facto *=i
#     i +=1 
#     print(facto)
# print(" ")
# print("FACTORIAL = ",facto)
# print(" ")
# '''
# # for i in range (1,11):
# #     print(i)
    
# total=0
# for i in range( 1, 101):
#     total=total+i
    
# print("total sum = ", total)
# fruits=['banana','apple','mango','grapes']
# for fruit in fruits:
#     print(fruit, end=" ")
# print("The loop is ended.")
# text='hello world !'
# vowels='aeiouAEIOU'
# count = 0
# for char in text:
#     if char in vowels:
#         count +=1
#     # else:
#     #     print(char)
        
# print("Total voweles: ", count)

# for i in range(3):
#     for j in range(2):
#         print(f"i={i},j={j}")
# print("loop is ended")
        
# matrix=[[1,2],[3,4]]
# for row in matrix:
#     for item in row:
#         print(item)
# print("Loop is ended")

# for i in range(6,1,-1):
#     for j in range(i):
#         print("*",end="")
#     print() 


# def calc_factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact *=i
#     # print("Factorial = ", fact)
#     return fact  


# print(calc_factorial(3))
# print(calc_factorial(5))

# import math
# num = int(input("Enter a number: "))
# if math.isqrt(num)**2 == num:
#  print("Perfect square")
# else:
#  print("Not a perfect square")


# print(math.isqrt(16))

# rows = int(input("Enter number of rows: "))
# for i in range(1, rows+1):
#     print("*" * i)
# def greet(name="Guest"):
#     print(F"Hello,{name}!")
# greet()
# greet("Ikram ali ")

# def sum_avg(list):

# def sum_avg(list):
#     # list=[3,4,3,2]
#     sum=0
#     for i in list:
#         sum += i
#         avg=sum/len(list)
#     print('TOTAL SUM OF LIST =',sum)
#     print("AVERAGE OF LIST =",avg)

# sum_avg([2,3,5])

# def multiply_all(*args):
#     result = 1
#     for num in args:
#         result *= num
#     return result
# print(multiply_all(2, 3, 4)) # 24

# def multiply_all(args):  # Bina star ke
#     result = 1
#     for num in args:
#         result *= num
#     return result

# # numbers = [2, 3, 4]
# print(multiply_all[1,3,4])  # Correct: 24 (list pass ki hai)
# # print(multiply_all(2, 3, 4))  # Error (kyuki bina star ke 3 arguments nahi le sakta)


# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# print_info(name="John", age=25, country="USA")


# def remove_duplicates(lst):
#     # return list(set(lst))
#     print(list(set(lst)))
# remove_duplicates([1,1,2,3,3,4,5,2])

# add two numbers

# add = lambda x,y: x+y
# print(add(3,5))

# square = lambda x: x**2
# print("square of given numbers :",square(4))

# max_two_numbers = lambda a,b: a if a>b else b
# print(max_two_numbers(20,30))
# last_cahr = lambda s:s[-1]
# print(last_cahr('pyrhon'))

# reverse= lambda s:s[::-1]
# print(reverse('ikram ali'))

# to_upper=lambda s:s.upper()
# print(to_upper('ikram ali'))
# print(to_upper('pYTHON'))

# start_with_vowel=lambda s:s[0].upper() in 'AEIOU'
# print(start_with_vowel("ikram ali"))
# print(start_with_vowel('apple'))
# print(start_with_vowel('Applra'))
# print(start_with_vowel('boy'))

# tup=(1,2,3,4,5)
# double=tuple(map(lambda x:x*2,tup))
# print(double)

# words=["apple","banana","kiwi","aayus","ali"]
# length=list(filter(lambda x:x.startswith('a'),words))
# print("length of string:",length)

# # a=[2,1,2,3,4]
# b=[1,2,3,4,5,6,7,8,9,10]
# square=list(map(lambda x:x**2,filter(lambda x:x%2 !=0,b)))
# # print(sums)


# 9. Find length of each word in list
# words = ["lambda", "function", "loop"]
# lengths = lambda ik: [len(w) for w in ik]
# print(lengths(words))  # Output: [6, 8, 4]

# nums = [1, 2, 3, 4, 5, 6]
# evens = list(filter(lambda x: x % 2 == 0, nums))
# print(evens)  # Output: [2, 4, 6]


# nums = [10, 20, 30, 40]
# multiply_index = lambda lst: [x * i for i, x in enumerate(lst)]
# print(multiply_index(nums))  # Output: [0, 20, 60, 120]

# try: 
#     n=2 
#     res=100/n
# except ZeroDivisionError:
#     print("Can't devide by zero")
# except ValueError:
#     print("value error")
# else:
#     print("result",res)
# finally:
#     print("Now completed")


# try :
#     a=10/0
# except ZeroDivisionError:
#     print("Can't divide by Zero:")
    
# try:
#     num1 = int(input("Enter numerator: "))
#     num2 = int(input("Enter denominator: "))
#     result = num1 / num2
#     print("Result :", result)
# except ZeroDivisionError:
#     print("Denominator cannot be zero!")

try:
    print("Start")
    x = int("hello")
except ValueError:
    print("ValueError occurred")
    
    
# try:
#     a = int(input("Enter a number: "))
#     b = 10 / a
#     print("result :", b)
# except (ZeroDivisionError, ValueError) as e:
#     print("An error occurred:", e)
