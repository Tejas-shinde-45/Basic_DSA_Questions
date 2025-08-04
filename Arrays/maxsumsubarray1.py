# max sum of subarrays using (Brute force )algorithms.
arr=[2,4,6,8,10]
maxsum=0
for i in range(len(arr)):   
    for j in range(i,len(arr)):
        arr1=[]
        currtsum=0
        for k in range(i,j+1):
            currtsum+=arr[k]
        
        if currtsum > maxsum:
            maxsum=currtsum
        print(currtsum)

print("maximum sum of the subarrya",maxsum)