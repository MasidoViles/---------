a = int(input("Введите первое число - ")) #Вводим наши 3 числа
b = int(input("Введите второе число - "))
c = int(input("Введите третье число - "))
s = a + b + c; #Проводим их сложения для будущего вычисления ост.числа
print("Расчет чисел:")
print("Максимальное число - ", max(a,b,c)) #max возвращает наибольшее значение
print("Минимальное число - ", min(a,b,c)) #min возвращает наименьшее значение
print("Остаточное число - ", s - max(a,b,c) - min(a,b,c))
#Остаточное число мы нашли благодаря сумме всех чисел, и отниманию максимального
#и минимального числа
