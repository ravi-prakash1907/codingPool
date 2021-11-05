'''
Format strings in zigzag pattern and later read it row-wise.
eg.:

I/P:  
"PAYPALISHIRING"

ZigZag form:
P   A   H   N
A P L S I I G
Y   I   R

O/P:
"PAHNAPLSIIGYIR"

'''

##############  ZigZag Converter  ##############

def convert(s,numRows):
    zigzag = [[] for i in range(numRows)]
    
    size = len(s)
    setCount, currLoc = 0,0
    flag = True

    while flag:
        setCount += 1
        if (2*numRows-2)*setCount >= size:
            uptoLoc = size
            flag = False
        else:
            uptoLoc = (2*numRows-2)*setCount
        strSet = s[currLoc:uptoLoc]

        # processing 'strSet'
        #print(strSet)
        revTrack = numRows-1

        for i in range(numRows): #0,1,2
            if i < len(strSet):
                zigzag[i].append(strSet[i])
                if i not in [0,numRows-1]:
                    if revTrack+i < len(strSet):
                        zigzag[i].append(strSet[revTrack+i])
                        revTrack -= 2
        
        ## updating for the loop
        currLoc = uptoLoc
    
    # result builder
    res = ""
    for rows in zigzag:
        for char in rows:
            res += char
    
    return  res



############## TESTING ##############

#plainStr,rows = "PAYPALISHIRING",3
plainStr = input("Enter the string: ") 
rows = int(input("Enter the number of rows: "))

Z = convert(plainStr, rows)

print("ZigZag output: ",Z)