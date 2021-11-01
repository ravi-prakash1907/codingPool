""" Python Program to check Armstrong Number (as 153)  """

def checkArmstrong(num):
    num = str(num)
    order = len(num)
    res = 0
    
    for i in num:
        res += pow(int(i),order)
    
    return True if res == int(num) else False

N = int(input("Enter the number: ")) 
if checkArmstrong(N):
    print(N,"is an armstrong number!")
else:
    print(N,"is NOT an armstrong number!")
  
