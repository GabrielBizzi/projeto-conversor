# Important biblioteca do sistema operacional
import os
# Excutando comando do sistema para limpar o terminal
os.system('cls' or 'clear')

# Iniciando estrutura de repetição para apresentação do menu
while True:
    # Variável de ligar/desligar
    confirm = input('Iniciar o conversor? (y/n): ')
    # Caso ligar
    if (confirm == 'y'):
        # Pedir numero da decimal
        decimal = int(input('\nDigite o número decimal para realizar as conversões: '))
        # Apresenta uma informação
        print('\n\033[34m[i]\033[0;0m Escolha apenas entre as opções fornecidas (digite o número da opção desejada).\n')
        # Apresenta as opções
        print('[1] Converter para Binário')
        print('[2] Converter para Octadecimal')
        print('[3] Converter para Hexadecimal\n')

        # Armazena a opção escolhida
        opt = int(input('Digite uma das opções: '))

        # Mostra uma mensagem de funcionamento para o usuário
        print('\n\033[32mRealizando conversão...\033[0;0m\n')

        # Condicional para verificar o valor do menu escolhido pelo usuário
        if (opt == 1):
            # código da conversão Binária
            print('Conversão para Binário\n')
        elif (opt == 2):
            # código da conversão Octadecimal
            print('Conversão para Octadecimal\n')
        elif (opt == 3):
            # código da conversão Hexadecimal
            print('Conversão para Hexadecimal\n')

    # Caso desligue
    elif (confirm == 'n'):
        # Fecha o código
        break
    # Opção inválida
    else:
        # Mensagem
        print('Digite "y" para sim e "n" para não')
        # Continuar o código e reiniciar a repetição
        continue
                    