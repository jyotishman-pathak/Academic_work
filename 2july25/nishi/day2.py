#dictionary
d={"tom":1234567890,"rob":9876543987,"joe":456723486}
for key in d:
    print("key:",key,"value:",d[key])
for k,v in d.items():
    print("key:",k,"value:",v)
d.clear()
print(d)
#tuple
point=(2,9)
print(point[0]*point[1])
print(point[1])
#modules
import math
x=int(input("<UNK>"))
b=math.sqrt(x)
print(b)
y=int(input("<UNK>"))
c=math.pow(x,y)
print(c)
import calendar
cal=calendar.month(x,y)
x=int(input("input a year"))
y=int(input("input a month"))
print(calendar.month(x,y))
#JSON
book= {'tom': {
    'name': 'tom',
    'age': 22,
    'phone': 987654456
}, 'rob': {
    'name': 'rob',
    'age': 21,
    'phone': 9876544975
}}
import json
s=json.dumps(book)
print(s)
#to write this into a file
# with open("c://data//book.txt","W") as f:
  #  f.write(s)
#to read
#f=open("c://data//book.txt","r")
#s=f.read
#to read as dict
#import json
#book=json.loads(s)
#exception
x=input("input a number 1")
y=input("input a number 2")
try:
     z=int(x)/int(y)
except ZeroDivisionError as e:
    print('division by zero exception')
    z=None
except TypeError as e:
    print("type error exception")
    z=None
print("division is:",z)
#Class
class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def do_something(self):
        if self.age<18:
            print(self.name,"not an adult")
        elif 18 <= self.age < 125:
            print(self.name,"is an adult")
x=input("input your name")
y=int(input("input your age"))
x=Human(x,y)
x.do_something()
#inheritence
class Vehicle:
    def general_usage(self):
        print("general usage: transportation")
class Car(Vehicle):
    def __init__(self):
        print("car class")
        self.wheels=4
        self.has_roof=True
    def special_usage(self):
        print("special usage:to go on a picnic with family")
class Motorcycle(Vehicle):
    def __init__(self):
        print("motorcycle class")
        self.wheels=2
        self.has_roof=False
    def special_usage(self):
        print("special usage:a long ride alone")
c= Car()
c.general_usage()
c.special_usage()
print(isinstance(c,Vehicle))
print(issubclass(Car,Vehicle))
#rAISE EXCEPTION
class Accident(Exception):
    def __init__(self,msg):
        self.msg=msg
    def print_exception(self):
        print('user define exception:',self.msg)
try:
    raise Accident('btw two cars')
except Accident as e:
    e.print_exception()






