def fatorial(num):
    res = 1
    for i in range(1, num + 1):
        res *= i
    print(res)

x = int(input('Número: '))
fatorial(x)