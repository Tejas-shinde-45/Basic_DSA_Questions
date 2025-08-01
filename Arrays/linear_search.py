# linear_search in python..
arr=[2,4,6,1,7,8]
t=13
index=-1
def l_s(arr,t):
    for i in range(len(arr)):
        if arr[i]==t:
            global index 
            index = i+1
            break
    


l_s(arr,t)
if index<0:
    print("index is not found")
else:
    print("index is found at",index)