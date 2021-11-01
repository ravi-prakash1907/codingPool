""" Maximum of two numbers in Python """

def maxNum(a,b):
  if a > b:
    return True,a
  elif b > a:
    return True,b
  else:
    print("Both are equal!")
    return False,b

num1 = int(input("Num 1: "))
num2 = int(input("Num 2: "))
flag,res = maxNum(num1,num2)

if flag:
  print(res,"is greater!")
