age = int(input("Enter your age "))
if(age>=10):
    print("Yes")

else:
    print("No")


a = 234
b = 54
c = 43
d = 23
if (a > b):
    maxNum1 = a
else:
    maxNum1 = b
    if (c > d):
        maxNum2 = c
    else:
        maxNum2 = d
        if (maxNum2 > maxNum1):
            maxNum = maxNum2
        else:
            maxNum = maxNum1
            print("Maximum number out of these four numbers is", maxNum)


m1 = int(input("Enter the marks for subject 1:"))
m2 = int(input("Enter the marks for subject 2:"))
m3 = int(input("Enter the marks for subject 3:"))
overAll = ((m1+m2+m3)*100)/3
if (overAll >= 40):
    if (m1 >= 33 and m2 >= 33 and m3 >= 33):
        print("You have passed th exam")
else:
        print("You have not passed the exam due to one of the subjects")

