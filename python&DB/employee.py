import psycopg2 

conn=psycopg2.connect(
    dbname='',
    user='',
    password='',
    host='',
    port='' 
)

cur=conn.cursor()
print(conn.status)

# cur.execute("""
#             create table if not exists employee(
#                 id serial primary key ,
#                 first_name varchar(20),
#                 last_name varchar(20),
#                 age integer ,
#                 department varchar(20),
#                 salary integer 
#             )
#             """)
conn.commit()
class Employee():
    all_employees=[]
    def __init__(self,first_name,last_name,age,department,salary):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.department=department
        self.salary=salary
        type(self).all_employees.append(self)
        self.add_employee()
        
    @staticmethod
    def get_all_employees():
        return Employee.all_employees
    
    def __str__(self):
        return f"first_name: {self.first_name} , last_name: {self.last_name} , age: {self.age} , department :{self.department} , salary: {self.salary} , "


    def add_employee(self):
        cur.execute("""
                    insert into employee(first_name,last_name,age,department,salary)
                    values (%s, %s, %s, %s, %s)
                    returning id
                    """,(self.first_name, self.last_name, self.age, self.department, self.salary))
        self.id=cur.fetchone()[0]
        conn.commit()
        
    def transfer(self,new_department):
        self.department=new_department
        cur.execute("""
                    update employee 
                    set department=%s 
                    where id=%s
                    """,(new_department,self.id))
        conn.commit()
        
    def fire(self):
        if self in Employee.all_employees :
            Employee.all_employees.remove(self)
        
        cur.execute("""
                    delete from employee
                    where id=%s
                    """,(self.id,))
        conn.commit()
        
    def show(self):
        cur.execute("""
                    select * from employee
                    where id=%s
                    """,(self.id,))
        employee=cur.fetchone()
        if employee :
            print(employee)
        else:
            print('employee not found !')
    
    def list_employees(self):
        cur.execute("""
                    
                    select * from employee
                    
                    """)
        employees=cur.fetchall()
        for emp in employees : 
            print(emp)
            



    
    
# e6=Employee('noha','shreif',40,'backend',15000)

# e6.add_employee()
# e6.show()
# e6.transfer('front end')
# e6.show()
# # e5.fire()
# e6.list_employees()
