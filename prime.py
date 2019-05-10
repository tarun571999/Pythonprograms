#problem statement : To check whether a number is prime or not 

num = int(input("Enter the number\n"))
for i in range(2, (num // 2) + 1):
    if num % i == 0:
        print('the number is not prime\n')
        break
else:
    print('the number is prime\n')

