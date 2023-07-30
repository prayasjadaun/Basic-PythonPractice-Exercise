def greatest(num1, num2, num3):
    if(num1>num2):
        greater = num1
    else:
        greater = num2

        if(num3>greater):
            greater = num3

            return greater
        
        a = greatest(3,6,21)
        print(a)

#Question number 2 

def printpattern(n):
    for i in range(n):
        print("*"*(n-i))

printpattern(10)
        