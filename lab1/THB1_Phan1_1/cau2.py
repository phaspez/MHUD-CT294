import math

number = int(input("Nhap mot so N: "))

print("Uoc so cua N: ", end="")
for i in range(1, math.ceil(number/2.0)+1):
    if (number % i) == 0:
        print(i, end=" ")

print("\n")