class employee:
    def __init__(self,id,name,desig,sal,exp):
        self.id=id
        self.name=name
        self.desig=desig
        self.sal=sal
        self.exp=exp
    def __str__(self):
        return self.name
    def details(self):
        return self.id,self.name,self.desig,self.sal,self.exp
f=open("employee","r")
employees=[]
high=[]
for lines in f:
    id,name,desig,sal,exp=lines.rstrip("\n").split(",")
    employees.append(employee(id,name,desig,sal,exp))
for emp in employees:
    print(emp)
    high.append(emp.sal)
max=(max(high))
for emp in employees:
    if max==emp.sal:
        print(employee.details)
