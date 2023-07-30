# Question number 1---How to create a program for math table

# num = int(input("Enter the number\n"))

# for i in range(10):
#     print(f"{num}X{i+1}={num*(i+1)}")

# Question number 2 ---How to create a program For stars pattern

# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#      for j in range(n-i):
#        print(" ", end="")
#      for j in range(2*i-1):
#        print("*", end="")
#      for j in range(n-i):
#       print(" ", end="")
#       print("\n", end="")
#Questions number 3 --- How to create a program in stars pattern
 
n = 7
for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or i==n-1 or j==n-1):
            print("*", end="")
        else:
            print(" ", end="")
            print("\n", end="") 

