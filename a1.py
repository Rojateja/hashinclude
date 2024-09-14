#5.string method exploration
string = "hashinclude"
vowels = "aeiouAEIOU"
count = sum(string.count(vowel) for vowel in vowels)
print(count)
#reverse a string
a="apple "[::-1]
print(a)
#check string is palindrome or not
string=input("enter string")
revstr=""
for i in string:
    revstr=i+revstr
    print('reversed string:',revstr)
    if(string == revstr):
          print("the string is palindrome")
    else:
              print("the string is not a palindrome")



