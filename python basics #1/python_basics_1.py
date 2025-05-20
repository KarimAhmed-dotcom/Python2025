# 1- Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

first_name=input("enter your first name :")
last_name=input("enter your last name :")
print(last_name+ " " +first_name)

#-----------------------------------------------------------------------

# 2- Write a Python program that accepts an integer (n) and computes the value of 
# n+nn+nnn.  
# Sample value of n is ​ 5 
# Expected Result : ​ 615 

#-----------------------------------------------------------------------


value=input("please enter number : ")
print(int(value*1)+int(value*2)+int(value*3))
#-----------------------------------------------------------------------
# 3- Write a Python program to print the following here document.  
# Sample string 
# : 
# a string that you "don't" have to escape 
# This 
# is a ....... multi-line 
# heredoc string --------> example 

#-----------------------------------------------------------------------

multi_line=\
"""
a string that you "don't" have to escape 
This 
is a ....... multi-line 
heredoc string    
    
# """
print(multi_line)
#-----------------------------------------------------------------------

# 4- Write a Python program to get the volume of a sphere with radius 6. 
radious=float(input("enter the radious of ball : "))
v_ball=(4/3) * (3.14) * (radious**3) 
print(f"the volume of ball is {round(v_ball,2)}")

#-----------------------------------------------------------------------

# 5- Write a Python program that will accept the base and height of a triangle and compute the area.
height=input("enter the height of trainagle : ")
base=input("enter the base of trainagle : ")
area_of_triangle=0.5*int(height)*int(base)
print(f"the area of traingle is {area_of_triangle}")

#-----------------------------------------------------------------------

# 6- Write a Python program to construct the following pattern, using a nested for loop. 
# Search about method  
# end=”” 
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

for i in range(1,6,1):
    print("* "*i)
    if i == 5:
        for i in range(4,0,-1):
            print(i*"* ")
        
        
#-----------------------------------------------------------------------

# 7- Write a Python program that accepts a word from the user and reverse it. 
word=input("input your word to reverse : ")
reverse_word=""
for j in range(len(word),0,-1):
    reverse_word+=(word[j-1])

print(reverse_word)
    
#-----------------------------------------------------------------------

# 8- Write a Python program that prints all the numbers from 0 to 6 except 3 and 6
for i in range(0,7):
    if i == 3 or i ==6 :
        continue
    print(i)

#-----------------------------------------------------------------------

# 9-Write a Python program to get the Fibonacci series between 0 to 50 
# Note : The Fibonacci Sequence is the series of numbers : 
# 0, 1, 1, 2, 3, 5, 8, 13, 21, .... 
# Every next number is found by adding up the two numbers before it. 
# Expected Output : 1 1 2 3 5 8 13 21 34

x, y = 0, 1
while y < 50:
    print(y)
    x, y = y, x + y

#-----------------------------------------------------------------------

# 10- Write a Python program that accepts a string and calculate the number of digits and letters.
letters=[]
digits=[]
word=input("enter the word to calculate the number of digits and letters : ")
for i in word :
       if i.isalpha():
           letters.append(i)
       elif i.isdigit():
           digits.append(i)

print(f"the number of digits is : {len(digits)}")
print(f"the number of letters is : {len(letters)}")
