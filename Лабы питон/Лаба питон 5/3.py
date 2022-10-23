word = "Nikita"
Glasnii = 0
Soglasnii = 0
for i in word:
    l = i.lower() # Функция lower() делает все буквы маленькими.
    if l == "a" or l == "e" or\
       l == "i" or l == "o" or\
       l == "u" or l == "y":
        Glasnii += 1
    else:
        Soglasnii += 1
print("Гласных %i\nСогласных %i" % (Glasnii, Soglasnii))
