def n(a):
    b  = 1
    for c in range(0, a):
        b *= a-c
    return b
        
        
x = int(input('Digite um número inteiro: '))
y = n(x)
print(f'{x}! = {y}')
