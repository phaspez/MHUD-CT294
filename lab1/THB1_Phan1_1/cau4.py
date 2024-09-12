import math

number = int(input("Nhap mot so N: "))
divisors = []

for i in range(1, math.ceil(number/2.0)+1):
    if (number % i) == 0:
        divisors.append(i)

if (sum(divisors) == number):
    print(str(number)+" is a perfect number!")
    for i in range(len(divisors)):
        print(str(divisors[i])+" + " if i != len(divisors)-1 else str(divisors[i]), end="")
    print(" = "+str(number))
else:
    print(str(number)+" is NOT a perfect number.")