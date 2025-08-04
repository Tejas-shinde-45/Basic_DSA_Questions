# search the element in the array using the birary search algorithms...
ar=[2,3,4,5,6,7,7,9]
key=4

def b_s(arr,k):
    lb=0
    up=len(arr)-1

    while lb<=up:
        mid=(lb+up)//2
        if arr[mid]==k:
            print("found here...",mid)
            break
        else:
            if arr[mid]<k:
                lb=mid
            else:
                up=key

b_s(ar,key)

    

        