employees={
    1000:{"eid":1000,"ename":"ran","desig":"developer","salary":30000},
    1001:{"eid":1001,"ename":"raj","desig":"qa","salary":25000},
    1002:{"eid":1002,"ename":"amit","desig":"ba","salary":35000}
}
eid=int(input("Enter the id: "))
property=(input("Enter the property: "))
if eid in employees:
    print("Name is:",employees[eid]["ename"])
    if property in employees[eid]:
        print(property,"is:",employees[eid][property])

