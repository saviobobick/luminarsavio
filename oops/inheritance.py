class parent:
    def n1(self):
        print("inside n1")
class subchild(parent):
    def n2(self):
        print("inside n2")
class child(subchild):
    def n3(self):
        print("inside n3")
ch=child()
ch.n1()
