#find the largest in the array...
arr=[8,1,3,4,5,6,3,2,4]

def largest(arr):
    lar=0
    for i in range(len(arr)):
        if arr[i]>=lar:
            lar = arr[i]
    print("largest in array is :",lar)

largest(arr)
        
