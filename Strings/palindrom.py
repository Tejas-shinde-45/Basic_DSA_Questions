n='universal'
for i in range(len(n)//2):
    if n[i]!=n[len(n)-i-1]:
        print("string is not palindrome")
        break
    print("string is palindrome")
    break