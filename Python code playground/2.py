# 2. Sum of Digits Until Single Digit
#example: 9875 -> 9+8+7+5 = 29 -> 2+9 = 11 -> 1+1 = 2

n = 9875

while n > 9:
    s = 0
    while n:
        s += n % 10  #concept :- n%10 means to get the last digit of the number 
        n //= 10     #// :-floor division means to remove last digit 
    n = s

print(n)
