
print("Even numbers using while loop:")
num = 1
while num <= 10:
    if num % 2 == 0:
        print(num)
    num += 1


print("\nCounting down using for loop:")
for i in range(10, 0, -2):
    print(i)


print("\nTuple unpacking example:")
student = ("Ravi", 21, "CSE")
name, age, branch = student
print(f"Name: {name}, Age: {age}, Branch: {branch}")


print("\nMatrix Addition:")

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

result = [
    [A[i][j] + B[i][j] for j in range(len(A[0]))]
    for i in range(len(A))
]

print("Matrix A:", A)
print("Matrix B:", B)
print("Result (A + B):", result)
