a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

delt = b ** 2 - 4 * a * c

x1 = (-b - delt ** 0.5) / (2 * a)
x2 = (-b + delt ** 0.5) / (2 * a)

print(f'O Delta é: {delt} e o X1 e X2 é: {x1}, {x2}')