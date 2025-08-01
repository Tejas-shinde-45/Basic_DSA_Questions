#finding the subarray of the array..
arr=[2,4,6,8,10]
for i in range(len(arr)):   
    for j in range(i,len(arr)):
        arr1=[]
        for k in range(i,j+1):
            arr1.append(arr[k])
        print(arr1)

        