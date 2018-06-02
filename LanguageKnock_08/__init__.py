def makeCode():
    target=[]
    tempResultArray=[]
    x=input("x= ")
    for i in range(len(x)):
        target.append(x[i])
    for j in range(len(target)):
        if target[j].islower():
            tempResultArray.append(str(ord(target[j])))
        else:
            tempResultArray.append(str(target[j]))
    result=''.join(tempResultArray)
    print(result,end="")
    return tempResultArray

makeCode()