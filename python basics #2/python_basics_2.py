# 1- Given a list of numbers, create a function that returns a list where all similar adjacent  
# elements have been reduced to a single element, so [1,2,3,3] returns [1,2,3] 
# Note:  
# You may create a new list or modify the passed in list.

List=[1,2,3,3]
newRedList=[]
def reduced(collection):
    return list(set(collection))
                
newRedList=reduced(List)
print(newRedList)



#another method 
mylist=[1,2,3,3]
def check_diff(sequence):
    seq=sequence
    gen_seq=[]
    for i in seq:
        if i in gen_seq:
            continue
        else:
            gen_seq.append(i)
    return gen_seq
print(check_diff(mylist))
#------------------------------------------------------------------------------------------------

# 2 Consider dividing a string into two halves  
# Case1:  
# The length is even, the front and back halves are the same length. 
# Case2: 
# The length is odd, we’ll say that the extra char goes in the front half. 
# E.g. ‘abced’, the front half is ‘abc’, the back half’de. 
# Given 2 strings, a and b, return a string of the form: 
# (a-front + b-front) + (a-back +b-back) 

import math
def strCalc(string):
    str_lenght=len(string)
    if str_lenght %2 ==0:
        return [string[0:int(str_lenght/2)],string[int(str_lenght/2):str_lenght]]
    else:
        return [string[0:math.ceil(str_lenght/2)],string[math.ceil(str_lenght/2):str_lenght]]
    
    
print(strCalc("kemo"))
print(strCalc("kemos"))
#------------------------------------------------------------------------------------------------

# 3- Write a Python function that takes a sequence of numbers and determines  
# whether all the numbers are different from each other. 
# E.X. [1,5,7,9] -> True 
# [2,4,5,5,7,9] -> False


mylist=[1,2,3]
def check_diff(sequence):
    seq=sequence
    gen_seq=[]
    for i in seq:
        if i in gen_seq:
            continue
        else:
            gen_seq.append(i)
    if len(seq) == len(gen_seq):
        return "there are the same"
    else:
        return "there are differnce"


print(check_diff(mylist))

#----------------------------------------------------------------------------------------------

# Given unordered list, sort it using algorithm bubble sort 
# ( read about  bubble sort and try to implement it) 

mylist=[5,6,1,3,4,5,36,8,79]
def orderme(unord_list):
    for i in range(len(unord_list)):
        for j in range((len(unord_list)-1)):
            if unord_list[j] <= unord_list[j+1]:
                continue
            else:
                current=unord_list[j]
                next=unord_list[j+1]
                unord_list[j]=next
                unord_list[j+1]=current    
    return  unord_list
        
print(orderme(mylist))

#---------------------------------------------------------------------------------------------
# 5- Gusses game 
# ● Your game generates a random number and gives only 10 tries for the user to 
# guess that number. 
# ● Get a user input and compare it with the random number 
# ● Display a hit message to the user in case the use number is smaller or bigger of 
# the random number 
# ● If the user type number is out of range(100), display a message that is not allowed 
# and don’t count this as try. 
# ● If user type a number that has been entered before, display a hint message and 
# don’t count this as try 
# ● In case the user entered a correct number within the 10 tries, display a 
# congratulations message and let your application guess another random number 
# with the remain number of tries 
# ● If the user finishes all his tries, display a message to ask him if he wants to play 
# again or not.


import random
def guess_game():
    usr_guesses = []
    app_number = random.randint(0, 100)
    print(app_number)
    while len(usr_guesses) < 10:
        try:
            usr_guess = int(input("Guess a number from [0..100]: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if usr_guess < 0 or usr_guess > 100:
            print("Your number is out of range!")
            continue

        usr_guesses.append(usr_guess)

        if usr_guess == app_number:
            print(f" Congratulations! You guessed correctly: {app_number}")
            complete=input("click (y) to continue (n) to exit")
            if complete=="y":
                return guess_game()
            else:
                break
        else:
            print(" Try again!")
            
    return f"Game over! The correct number was {app_number}"


print(guess_game())
