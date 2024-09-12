mydict = {}

num = int(input("Enter a number: "))
for i in range(1, num+1):
    mydict[i] = i**2

print("mydict = ", mydict)