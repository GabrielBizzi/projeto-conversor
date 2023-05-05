# Important biblioteca do sistema operacional
import os
# Excutando comando do sistema para limpar o terminal
os.system('cls' or 'clear')

# Iniciando estrutura de repetição para apresentação do menu
while True:
    # Variável de ligar/desligar
     print('Olá! Escolha apenas entre as opções fornecidas.\n')
     print('[1] Iniciar Conversor')
     print('[2] Informações')
     print('[3] Sair\n')
     confirm = int(input("Digite uma opção do menu apresentado: "))

    # Caso ligar
     if (confirm== 1):
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
           bin = ''
           temp = decimal 

           while decimal > 0:

                bin = str(decimal%2) + bin
                decimal = decimal//2

           print(f'O decimal {temp} é igual ao binário {bin}.\n')
           input('Pressione "Enter" para continuar')
           os.system('cls')

        elif (opt == 2):
        
            # código da conversão Octadecimal

            # Reservar variável para utilizar depois
            octa = ''

            # Variável de backup
            temp = decimal

            # Iniciar repetição enquanto meu decimal for maior que 0
            while decimal > 0:

                # Fracionamento da base octal
                octa = str(decimal%8) + octa 

                # Resto da divisão  
                decimal = decimal//8

            # Resultado
            print(f"O decimal \033[34m{temp}\033[0;0m é igual ao Octadecimal {octa}\n")
            input('Pressione "Enter" para continuar')
            os.system('cls')
            
        elif (opt == 3):
            # código da conversão Hexadecimal
            conversion_table = {0: '0', 1: '1', 2:  '2', 3: '3', 4: '4',
                                5: '5', 6: '6', 7: '7',
                                8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                                13: 'D', 14: 'E', 15: 'F'}


            hexa = ''
            hexadecimal = ''

            temp = decimal


            while(decimal > 0):
                hexa = decimal % 16
                hexadecimal = conversion_table[hexa] + hexadecimal
                decimal = decimal //16



            print(f"O decimal \033[34m{temp}\033[0;0m é igual ao hexadecimal {hexadecimal}\n")
            input('Pressione "Enter" para continuar')
            os.system('cls')

    # Caso desligue
     elif (confirm == 2):
        # Informações do trabalho
             print('Escolha apenas entre as opções fornecidas.\n')
             print('[1] Curso')
             print('[2] Componentes do grupo')
             print('[3] Disciplinas envolvidas')
             print('[4] Versão do aplicativo\n')
             confirm_2 = int(input("Digite uma opção do menu apresentado: "))

             if (confirm_2== 1):
              print('\nCiência da Computação - Universidade Cruzeiro do Sul\n')
              input('Pressione "Enter" para continuar')
              os.system('cls')

             elif (confirm_2== 2):
                print("""
                Gabriel Bizzi
                Gustavo Feitosa
                kauã Aquino
                Manuella Caputo
                Pietra Duccini\n""")
                input('Pressione "Enter" para continuar')
                os.system('cls')
                
             elif(confirm_2== 3):
                 print('\nProgramação de Computadores\n')
                 input('Pressione "Enter" para continuar')
                 os.system('cls')

             elif(confirm_2== 4):
                 print('\nv1.0.5\n')
                 input('Pressione "Enter" para continuar')
                 os.system('cls')
     
     elif (confirm == 3):
        # Fecha o código
        break
    # Opção inválida
     else:
        # Mensagem
        print('Digite uma das opções apresentadas')
        # Continuar o código e reiniciar a repetição
        continue
                    