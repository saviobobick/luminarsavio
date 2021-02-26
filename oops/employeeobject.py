class employee:
    def __init__(self,id,name,desig,sal,exp):
        self.id=id
        self.name=name
        self.desig=desig
        self.sal=sal
        self.exp=int(exp)
    def __str__(self):
        return self.name
    def details(self):
        return self.id,self.name,self.desig,self.sal,self.exp
f=open("employee", "r")
employees=[]
for lines in f:
    id,name,desig,sal,exp=lines.rstrip("\n").split(",")
    employees.append(employee(id,name,desig,sal,exp))
print(list(map(lambda emp:emp.name,(list(filter(lambda emp:emp.desig=="developer",employees))))))
print(max(list(map(lambda emp:emp.sal,employees))))
print(len(list(filter(lambda emp:emp.desig=="qa",employees))))
print(list(map(lambda emp:emp.name,list(filter(lambda emp:emp.exp>1,employees)))))