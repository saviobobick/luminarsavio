import Functions.demo2
addres=Functions.demo2.add(50,50)
print(addres)
from Functions.demo2 import *
addres=add(10,10)
print(addres)
import Functions.demo2 as ab
addres=ab.add(50,50)
print(addres)