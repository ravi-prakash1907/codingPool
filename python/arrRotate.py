""" Python Program for array rotation """

def rotateArr(arr,n):
    if n == 0 or len(arr) <= 1:
        return arr
    else:
        size = len(arr)
        last = arr[size-1]
        
        i = size-2
        while i >= 0:
            arr[i+1] = arr[i]
            i -= 1
        arr[0] = last

        return rotateArr(arr,n-1)


#############

inp = [1,2,3,4,5,6,7]
dist = 4

result = rotateArr(inp,dist)
print(result)