# Important biblioteca do sistema operacional
import os, time
# Excutando comando do sistema para limpar o terminal
os.system('cls' or 'clear')

# Iniciando estrutura de repetição para apresentação do menu
while True:
    # Variável de ligar/desligar
     print('Olá! Escolha apenas entre as opções fornecidas.\n')
     print('\033[34m[1]\033[0;0m Iniciar Conversor')
     print('\033[34m[2]\033[0;0m Informações')
     print('\033[34m[3]\033[0;0m Sair\n')
     confirm = int(input("Digite uma opção do menu apresentado: "))

    # Caso ligar
     if (confirm== 1):
        os.system('cls')
        # Pedir numero da decimal
        decimal = int(input('\nDigite o número decimal para realizar as conversões: '))
        # Apresenta uma informação
        print('\n\033[34m[i]\033[0;0m Escolha apenas entre as opções fornecidas (digite o número da opção desejada).\n')
        # Apresenta as opções
        print('\033[34m[1]\033[0;0m Converter para Binário')
        print('\033[34m[2]\033[0;0m Converter para Octadecimal')
        print('\033[34m[3]\033[0;0m Converter para Hexadecimal\n')

        # Armazena a opção escolhida
        opt = int(input('Digite uma das opções: '))

        os.system('cls')

        # Mostra uma mensagem de funcionamento para o usuário
        print('\n\033[32mRealizando conversão...\033[0;0m\n')

        time.sleep(2)
        os.system('cls')

        # Condicional para verificar o valor do menu escolhido pelo usuário
        if (opt == 1):
            # código da conversão Binária
           bin = ''
           temp = decimal 

           while decimal > 0:

                bin = str(decimal%2) + bin
                decimal = decimal//2

           print(f'O decimal \033[34m{temp}\033[0;0m é igual ao binário {bin}.\n')
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
             os.system('cls')
             print('Escolha apenas entre as opções fornecidas.\n')
             print('\033[34m[1]\033[0;0m Curso')
             print('\033[34m[2]\033[0;0m Componentes do grupo')
             print('\033[34m[3]\033[0;0m Disciplinas envolvidas')
             print('\033[34m[4]\033[0;0m Versão do aplicativo\n')
             confirm_2 = int(input("Digite uma opção do menu apresentado: "))
             os.system('cls')

             if (confirm_2== 1):
              print('\n\033[32mCiência da Computação - Universidade Cruzeiro do Sul\033[0;0m\n')
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
                 print('\n\033[32mProgramação de Computadores\033[0;0m\n')
                 input('Pressione "Enter" para continuar')
                 os.system('cls')

             elif(confirm_2== 4):
                 print('\n\033[32mv1.0.5\033[0;0m\n')
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
                    