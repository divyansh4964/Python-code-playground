# 4. Count the Number of Even Digits and Odd Digits
#Input: 456123

n = 456123
# even = 0
# odd = 0
even=odd=0

while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        even += 1
    else:
        odd += 1
    n //= 10

print("Even:", even)
print("Odd:", odd)
