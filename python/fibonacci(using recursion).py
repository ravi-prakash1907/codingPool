""" Python program to print a Fibonacci series using recursion """
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

N = int(input("Enter a number: "))
print("The fibonacci series upto",N,"is:")
for i in range(N): 
    print(fibo(i))
