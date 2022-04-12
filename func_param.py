def printmax(a,b):
    if a > b:
        print(a, 'Больше')
    elif a == b:
        print(a,'Равно', b)
    else:
        print(b, 'Больше')

printmax(3, 4) # прямая передача значений

x = 5
y = 7

printmax(x, y) # передача переменных в качестве аргументов