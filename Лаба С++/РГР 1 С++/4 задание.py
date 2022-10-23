X = int(input("Введите любое число -> "))
if X<=12 and X>-15:
    print('True')
elif X>14 and X<17: #elif-если не выполнено предыдущее условие, но выполнено текущее
    print('True')
elif X>=19:
    print('True')
else:
    print('False')
