x = 50

def func(x):
    print('x равен', x)
    x = 2
    print('Замена локалього х на', x)

func(x)
print('х по-прежнему', x)