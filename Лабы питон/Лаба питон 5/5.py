def prime(number):
    n = number
    c = 0
    for i in range(1, n + 1):
        if n % i == 0:
            c += 1
    return 'Простое число' if c == 2 else 'Составное число'
print(prime(132))
#Здесь мы вводим число для того чтобы он показал простое оно или составное
