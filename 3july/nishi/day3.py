#iterators
class RemoteControl:
    def __init__(self):
        self.channels=["hbo","cnn","avc","expn"]
        self.index=-1

    def __iter__(self):
        return self
    def __next__(self):
        self.index+=1
        if self.index>=len(self.channels):
            raise StopIteration
        return self.channels[self.index]
r=RemoteControl()
itr=iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
#generators
def fibo():
    aa,b=1,2
    while True:
        yield aa
        aa,b=b, aa + b
for f in fibo():
    if f>100:
        break
    print(f)
#list set dict comprehensions
number=[1,2,3,4,5,6,7,8,9]
even=[]
for i in number:
    if i%2==0:
        even.append(i)
print(even)
even=[i for i in number if i%2==0]
print(even)
sqr_numbers=[i**2 for i in number]
print(sqr_numbers)
s= {1, 2, 3, 3, 8, 9, 3, 4, 5, 6, 7, 8, 9}
print(s)
even={i for i in number if i%2==0}
print(even)
cities=["mumbai","new york","paris"]
countries=["India","United States","France"]
z=zip(cities,countries)
print(z)
for a in z:
    print(a)
d={city:country for city,country in zip(cities,countries)}
print(d)
#set a frozen set
set1={"123","244","456","789","244"}
type(set1)
print(set1)
a=set()
a.add(1)
a.add(2)
print(a)
number=[1,2,3,4,5,6,7,8,9,7,3,2,4,]
unique_number=set(number)
print(unique_number)
unique_number.add(200)
print(unique_number)
fs=frozenset(number)
print(fs)
#command line arguments
import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--num1", type=int, help="first number")
    parser.add_argument("--num2", type=int, help="second number")
    parser.add_argument("--operation", help="operation: sum, product, or min")

    args = parser.parse_args()
    if args.num1 is None:
        args.num1 = int(input("Enter first number: "))
    if args.num2 is None:
        args.num2 = int(input("Enter second number: "))
    if args.operation is None:
        args.operation = input("Enter operation (sum/product/min): ").strip()
    result = None
    if args.operation == "sum":
        result = args.num1 + args.num2
    elif args.operation == "product":
        result = args.num1 * args.num2
    elif args.operation == "min":
        result = min(args.num1, args.num2)
    else:
        print("unknown operation")
        exit()

    print(f'result: {result}')
#Decorators
import time
def time_it(func):
    def wrapper(*arg, **kwargs):
        start = time.time()
        results = func(*arg, **kwargs)
        end = time.time()
        print(func.__name__ +"took" +str((end - start)*1000) +"milliseconds")
        return results
    return wrapper
# to find time of operation of different functions
#add @time_it before the def line
