#a
for i in range(0, 101, 10):
    print(i, end=" ")
print()

#b
for i in range(20, 0, -1):
    print(i, end=" ")
print()

#c
number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars):
    print("*", end="")
print()

#d
number_of_line = int(input("Number of line: "))
for i in range(1, number_of_line + 1):
    print("*" * i)