# making the pair of the arrays.....
arr=[2,3,4,5,6]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        print((arr[i],arr[j]),end="")
    print()