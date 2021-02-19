# class
# objects
# reference
class person:
    def set_person(self,age,name):
        self.name=name
        self.age=age
    def print_person(self):
        print(self.name,self.age)
obj=person()
obj.set_person(25,"ram")
obj.print_person()
obj1=person()
obj1.set_person(27,"deepak")
obj1.print_person()