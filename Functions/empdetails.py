def emp(**data):
    employees = {
        1000: {"eid": 1000, "ename": "ram", "desig": "developer", "salary": 30000},
        1001: {"eid": 1001, "ename": "raj", "desig": "qa", "salary": 25000},
        1002: {"eid": 1002, "ename": "amit", "desig": "ba", "salary": 35000}
    }
    id=data["eid"]
    prop=data["property"]
    if id in employees:
        print("Name :",employees[id]["ename"])
        if prop in employees[id]:
            print(prop,":",employees[id][prop])
        else:
            print(prop,"doesnt exist")
    else:
        print("id doesnt exist")
eid=int(input("Enter the id: "))
property=input("Enter the property: ")
emp(eid=eid,property=property)
