from employee import *
from manager import *

process=input("for adding new employee enter “add”' ")

option=input("If manager press “m”/ if employee press “e” ")

print("Please insert data ")

if process =='add' and option == 'e':
    first_name=input("enter your first name : ")
    last_name=input("enter your last name : ")
    age=int(input("enter your age : "))
    department=input("enter your department : ")
    salary=int(input("enter your salary : "))
    
    e=Employee(first_name,last_name,age,department,salary)
    print("Employee added successfully.")
elif process =='add' and option == 'm' :
    first_name=input("enter your first name : ")
    last_name=input("enter your last name : ")
    age=int(input("enter your age : "))
    department=input("enter your department : ")
    salary=int(input("enter your salary : "))
    managed_department=input("enter your managed department : ")
    
    m=Manager(first_name,last_name,age,department,salary,managed_department)
