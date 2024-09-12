num = int(input("Nhap mot so N: "))
curr = 1
for i in range(0, num+1):
    for j in range(1, i+1):
        print(f"{curr:5}", end="")
        curr+= 1
    print("\n", end="")