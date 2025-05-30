# 1-The program takes a command line argument, this argument is the name of a text file. 
# the program reads all the text and split them and calulate the 20 most used workds in the 
# file 
# and then write them to a file called popular_words.t
#  xt 

def calc_freq(file):
    file=open(file)
    words=[]
    dict_words={}
    freq_words=[]
    for line in file.readlines():
        file_words=line.split(sep=" ")
        for i in file_words : 
            words.append(i)
    for i in words :
        if i in dict_words.keys() :
            dict_words[i]+=1
        else:    
            dict_words[i]=1
    
    freq_words=sorted(dict_words.items(),key=lambda item:item[1],reverse=True)[:20]
    words_file=open('./top20_frequent_words.txt','w')
    for word,len in freq_words :
        words_file.write(f"{word} : {len} \n")
    return None
    
print(calc_freq('./mockingjay.txt'))

# 2-Given two points represented as x1, y1, x2, y2, r the (float)return (float) distance 
# between 
# them considering the following distance equation. 

import math
point1=(4,0)
point2=(1,0)

def calc_distance(p1,p2):
    x2=p2[0]
    x1=p1[0]
    y2=p2[1]
    y1=p1[1]
    diffX2=(x2-x1)**2
    diffy2=(y2-y1)**2
    distance=math.sqrt(diffX2+diffy2)
    return distance
print(calc_distance(point1,point2))

#3-Create a Vehicle class without any variables and methods
class Vehicle():
    def __init__(self):
        pass
    
#4-Create a Vehicle class with max_speed and mileage instance attributes
class Vehicle():
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage

#5-Write a Python program to reverse a string word by word. 
def reverse_me(sentence):
    words=sentence.split()
    reverse_words=words[::-1]
    return ' '.join(reverse_words)

sentence = "I love Python"
reversed_sentence = reverse_me(sentence)
print(reversed_sentence)


#6-Write a Python class which has two methods get_String and print_String. get_String 
# accept a string from the user and print_String print the string in upper case 

class PrintString():
    def __init__(self):
        self.string=""
    
    def get_string(self):
        self.string=input("Enter Your String :")
    def print_string(self):
        print(f"This is Your string : {self.string}")
        
s=PrintString()
s.get_string()
s.print_string()

#7-Write a Python class named Circle constructed by a radius and two methods which will 
# compute the area and the perimeter of a circle.

class Circle():
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return 0.5*3.14*(self.radius**2)
    def perimeter(self):
        return 2*3.14*self.radius
    
c=Circle(10)
area=c.area()
perimeter=c.perimeter()
print(area)
print(perimeter)
