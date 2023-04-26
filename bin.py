import os
os.system('cls' or 'clear')

decimal = int(input('Digite o número decimal para realizar a conversão: '))
bin = ''
temp = decimal 

while decimal > 0:

    bin = str(decimal%2) + bin
    decimal = decimal//2

print(f'O decimal {temp} é igual ao binário {bin}.')