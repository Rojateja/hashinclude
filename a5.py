#palindrome checker
s=input("enter the value of string=")
rev=s[::-1]
if(rev==s):
    print("is palindrome")
else:
    print("not a palindrome")
