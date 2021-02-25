# class parent:
#     def phone(self):
#         print("have nokia phone")
# class child(parent):
#     def phone(self):
#         print("have iphone")
# ch=child()
# ch.phone()

class person:
    def __init__(self,age,name):
        self.age=age
        self.name=name
    def __str__(self):
        return self.name+str(self.age)
p=person(22,"ajay")
print(p)