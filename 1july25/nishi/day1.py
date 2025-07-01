#List on pythons
items=["bread","pasta","fruits","veggies"]
items.append("apple")
print(items)
items.insert(2,"butter")
print(items)
items.remove("pasta")
print(items)
bathroom=["shampoo","soap"]
total_items=items+bathroom
print(total_items,len(total_items))
#if else functions
num=int(input("enter the number"))
if num%2==0:
    print(num,"is even")
else:
    print(num,"is odd")
#asking if a item is in the items list or not
item=(input("enter the item"))
if item in items:
    print("Yes")
else:
    print("No")
#if loops
expense=[1200,2000,1400,4000]
total=0
for i in range(len(expense)):
    print("month:",(i+1),"Expense:",expense[i])
    total=total+expense[i]
print("total expense:",total)
for i in range(1,11):
    if i%2==0:
        continue
    print(i*i)
#while loops
i=1
while i<=10:
    print(i)
    i=i+1
#user define function
def calculate_total(exp):
    total=0
    for item in exp:
        total=total+item
    return total
my_expense=[2100,222,1200,5000]
not_my_expense=[1200,2000,6000,800]
print("my expense",calculate_total(my_expense))
print("not my expense",calculate_total(not_my_expense))