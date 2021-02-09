employees=[
    [100,"Tom","Developer",25000],
    [101,"Jack","Developer",18000],
    [102,"Jhon","Ba",28000],
    [104,"Dinu","Da",26000]]
sal=0
highsal=0
for emp in employees:
    if emp[2]=="Developer":
        print(emp)
    sal+=emp[3]
    if emp[3]>highsal:
        highsal=emp[3]
print("Total Salary is ",sal)
print("Highest Salary is ",highsal)
# highsal=max(map(lambda emp:emp[3],employees))




