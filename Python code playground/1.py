# 1. Print Reverse Number Pyramid
# 54321
# 5432
# 543
# 54
# 5

n = int(input("Enter a number: "))
num=n

for i in range(n):
    for j in range(n - i):

        print(n - j, end='')
        num-=1

    print()
