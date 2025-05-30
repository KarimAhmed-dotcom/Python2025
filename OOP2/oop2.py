# 1- Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white. 
class Vehicle: 
    color='white'
    def __init__(self, name, max_speed, mileage): 
        self.name = name 
        self.max_speed = max_speed 
        self.mileage = mileage 
class Bus(Vehicle): 
    pass 
class Car(Vehicle): 
    pass

print(Vehicle.color)

#----------------------------------------------------------------------------

# 2- Create a Bus child class that inherits from the Vehicle class. The default fare charge of 
# any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 
# 10% on full fare as a maintenance charge. So total fare for bus instance will become the 
# final amount = total fare + 10% of the total fare. 
# Note:
#  The bus seating capacity is 50. so the final fare amount should be 5500. You need 
# to override the fare() method of a Vehicle class in Bus class. 
# Use the following code for your parent Vehicle class. We need to access the parent class 
# from inside a method of a child class. 
class Vehicle: 
    def __init__(self, name, mileage, capacity): 
        self.name = name 
        self.mileage = mileage 
        self.capacity = capacity 
        def fare(self): 
            return self.capacity * 100 
    
class Bus(Vehicle): 
    def fare(self):
        return (self.capacity * 100)+0.1*(self.capacity * 100)

# School_bus = Bus("School Volvo", 12, 50) 
# print("Total Bus fare is:", School_bus.fare())

# 3- Determine if School_bus is also an instance of the Vehicle class 
class Vehicle: 
    def __init__(self, name, mileage, capacity): 
        self.name = name 
        self.mileage = mileage 
        self.capacity = capacity 
class Bus(Vehicle): 
    pass 
School_bus = Bus("School Volvo", 12, 50)

print(isinstance(School_bus, Vehicle)) #instace is parent or inherited from other parent

# 4-Define a class named Rectangle which can be constructed by a length and width. The 
# Rectangle class has a method which can compute the area.  
# Hints: 
# Use def methodName(self) to define a method. 

class Rectangle():
    def __init__(self,length,width):
        self.lenght=length
        self.width=width
        
    def area(self):
        return self.lenght*self.width
    
rectangle=Rectangle(3,4)
print(rectangle.area())


# 5- Define a class which has at least two methods: 
# getString: to get a string from console input 
# printString: to print the string in upper case.

class PrintString():
    def __init__(self):
        self.string=""
    
    def get_string(self):
        self.string=input("Enter Your String :")
    def print_string(self):
        print(f"This is Your string : {self.string.upper()}")
        
s=PrintString()
s.get_string()
s.print_string()


# 6-Define a class Person and its two child classes: Male and Female. All classes have a 
# method "getGender" which can print "Male" for Male class and "Female" for Female 
# class.

class Person():
    def __init__(self):
        pass
    
    def gender():
        print("Not determined !")
        
class Male(Person):
    def gender():
        print("Male !")

class Female(Person):
    def gender():
        print("Female !") 
        
Person.gender() 
Male.gender() 
Female.gender()

# 7- Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. 
# These brackets must be close in the correct order, for example "()" and "()[]{}" are valid 
# but "[)", "({[)]" and "{{{" are invalid  


class CloseMe():
    def __init__(self,parenthese):
        self.parenthese=parenthese
        
    def return_parenthese(self):
        if self.parenthese == '(' :
            return '()'
        elif self.parenthese == '{':
            return '{}'
        elif self.parenthese == '[':
            return '[]'
        else:
            return 'invalid parenthese' 


close=CloseMe('[')
print(close.return_parenthese())
