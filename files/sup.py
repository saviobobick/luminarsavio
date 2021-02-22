class person:
    def __init__(self,age,name):
        self.age=age
        self.name=name
employee=[]
p=person(27,"Ram")
p1=person(26,"Varun")
p2=person(24,"Nikhil")
employee.append(p)
employee.append(p1)
employee.append(p2)
lst=[]
for emp in employee:
    lst.append(emp.age)
    if emp.age>25:
        print(emp.name)
print(max(lst))