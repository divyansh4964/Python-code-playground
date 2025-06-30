#Palindrome Number Checker

n = int(input("Enter a number:"))
m = n
reverse = 0

while m :
    reverse = reverse * 10 + m % 10
    m //= 10

if reverse == n:
    print("Palindrome")
else:
    print("Not Palindrome")
