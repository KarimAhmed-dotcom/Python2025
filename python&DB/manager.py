import psycopg2 

conn=psycopg2.connect(
    dbname='',
    user='',
    password='',
    host='',
    port=''
    
)

cur=conn.cursor()

# cur.execute("""
#             create table if not exists manager(
#                 id serial primary key,
#                 employee_id integer references employee(id),
#                 managed_department varchar(20)  
#             )
#             """)

# conn.commit()

from employee import *

class Manager(Employee):
    def __init__(self,first_name,last_name,age,department,salary,managed_department):
        super().__init__(first_name,last_name,age,department,salary)
        self.managed_department=managed_department
        self.add_manager()
        
        
    def show(self):
        return f"first_name : {self.first_name} , last_name: {self.last_name} , age: {self.age} , department :{self.department} , salary: confidential"
    
    def add_manager(self):
        cur.execute("""
                    insert into manager (employee_id,managed_department)
                    values(%s ,%s) 
                    """,(self.id,self.managed_department))
        conn.commit()
        
    def fire(self):
        cur.execute("""
                    delete from manager
                    where employee_id=%s
                    """,(self.id,))
        conn.commit()
        super().fire()
