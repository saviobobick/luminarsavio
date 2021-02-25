class book:
    def __init__(self,pages):
        self.pages=pages
    def __str__(self):
        return str(self.pages)
    def __add__(self, other):
        return book(self.pages+other.pages)
    def __sub__(self, other):
        return self.pages-other.pages
    def __truediv__(self, other):
        return self.pages/other.pages
obj1=book(200)
obj2=book(100)
obj3=book(50)
print(obj1+obj2+obj3)
print(obj1-obj2)
print(obj1/obj2)
