
#reversing the array...
arr=[12,33,22,4,3,10]
def reverse(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        # Swap the elements at the start and end positions
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp

        # Move the pointers towards the center
        start += 1
        end -= 1

    print(arr)

# Example usage:
reverse(arr)
