print("Nhap danh sach cac so, nhap $ de ket thuc")

floats = []
userinput = ""
while userinput != "$":
    try:
        userinput = input("Nhap phan tu thu "+str(len(floats)+1)+": ")
        if userinput == "$":
            break
        f = float(userinput)
        floats.append(f)
    except:
        print("You did't type a float or a '$', try again")

if (len(floats) > 0):
    print("Average: ", sum(floats)/len(floats))
else:
    print("You didn't type any numbers")