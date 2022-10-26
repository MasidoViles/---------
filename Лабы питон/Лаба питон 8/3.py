words = ['гидроэлектростанция', 'блинчик', 'олег', 'абзац']
print(max(words, key=len)) #key - ключ сортировки
print("Количество символов: ", len(max(words, key=len)))