# Find the Largest Digit in a Number
num = int(input("Enter a number: "))
largest = 0

while num:
    digit = num % 10
    if digit > largest:
        largest = digit
    num = num // 10

print("Largest digit is:", largest)
