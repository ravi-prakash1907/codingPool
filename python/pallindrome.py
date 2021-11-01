""" Python Program to check Pallindrome Number (as 12321)  """

def ispallindrome(num):
    sum = 0
    original = num
    while num:
        t = num % 10
        sum = sum * 10 + t
        num = num // 10
    return True if original == sum else False
    
N = int(input("Enter a number: "))
if ispallindrome(N):
    print(N,"is a pallindrome number!")
else:
    print(N,"is not a pallindrome number!")
