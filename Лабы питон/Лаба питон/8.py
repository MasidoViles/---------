A1=int(input("Введите первое число -> "))
A2=int(input("Введите второе число -> "))
for i in range(1, A1+1): 
    for j in range(1, A2+1):
        print(i * j, end="\t")
        j += 1
    print()
    j = 1
    i += 1

        
