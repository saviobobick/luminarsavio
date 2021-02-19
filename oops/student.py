class student:
    def set_student(self,roll,name,total):
        self.roll=roll
        self.name=name
        self.total=total
    def print_student(self):
        print(self.roll,"\n",self.name,"\n",self.total)
obj=student()
obj.set_student(13,"deepak",62)
obj.print_student()
