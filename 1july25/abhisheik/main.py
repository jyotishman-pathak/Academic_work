


print("Using for loop:")
for i in range(5):
    print(f"Value: {i}")


print("\nUsing while loop:")
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1


print("\nWorking with Tuples:")
my_tuple = ("apple", "banana", "cherry")
for item in my_tuple:
    print(f"Fruit: {item}")


print("\nMatrix Manipulation (2D List):")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("Original Matrix:", matrix)
print("Transposed Matrix:", transpose)
