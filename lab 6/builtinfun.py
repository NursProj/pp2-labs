import time
import math

#1
# nums = input()
# my_list = [int(x) for x in nums.split()]
# sum = sum(my_list)
# print(sum)

#2
# stri=input()
# upcount=0
# lowcount=0
# for i in stri:
#     if i.isupper():
#         upcount+=1
#     elif i.islower():
#         lowcount+=1
#     else:
#         continue   
# print(f"lowercase:{lowcount}") 
# print(f"uppercase:{upcount}")    

#3
# def is_palindrome(s):
#     s = s.lower()  
#     return s == s[::-1]

#4
# def sqrt_after_mlsc(number, milliseconds):
#     time.sleep(milliseconds / 1000)
#     return math.sqrt(number)

# num = int(input())
# milliseconds = int(input())

# result = sqrt_after_mlsc(num, milliseconds):
# print(f"Square root of {num} after {milliseconds} milliseconds is {result}")

#5
def all_true(t):
    return all(t)
#false: "false", "0", ""; true: "true", "1", "abc"
