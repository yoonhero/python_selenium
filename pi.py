num1 = int(input("정수 num1을 입력하라: "))
num2 = int(input("정수 num2을 입력하라: "))

prime = []

for n in range(num1, num2+1):
    condition = True
    for i in range(1, n):

        if n % i == 0:
            condition = False
            break
        else:
            continue
    if condition:
        prime.append(n)

result = 0
for primeNum in prime:
    result += primeNum
print(prime)
print(str(num1) + "부터 " + str(num2) + "까지의 소수의 합계는 " + str(result) + "입니다")
