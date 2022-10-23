A = float (input("Введите первое число - "))
B = float (input("Введите второе число - "))
C = str (input("Введите действие с числами: "))
if C =='+':
    print(A+B)
elif C=='-':
    print(A-B)
elif C=='*':
    print(A*B)
elif C=='/' and B==0:
    print("Деление на 0!")
elif C=='/' and B!=0:
    print(A/B)
elif C=='mod' and B==0: # mod - взятие остатка от деления
    print('Деление на 0!')
elif C=='mod' and B!=0:
    print(A%B)
elif C=='pow': # pow - возведение в степень
    print(A**B)
elif C=='div' and B==0: # div - целочисленное деление
    print('Деление на 0!')
elif C=='div' and B!=0:
    print(A//B)
