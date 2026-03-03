import os

restaurantes = []

def exibir_logo_programa():
    print("""

    ██╗░░██╗███████╗██╗░░░░░██╗░░░░░░█████╗░  ░██╗░░░░░░░██╗░█████╗░██████╗░██╗░░░░░██████╗░
    ██║░░██║██╔════╝██║░░░░░██║░░░░░██╔══██╗  ░██║░░██╗░░██║██╔══██╗██╔══██╗██║░░░░░██╔══██╗
    ███████║█████╗░░██║░░░░░██║░░░░░██║░░██║  ░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░░░░██║░░██║
    ██╔══██║██╔══╝░░██║░░░░░██║░░░░░██║░░██║  ░░████╔═████║░██║░░██║██╔══██╗██║░░░░░██║░░██║
    ██║░░██║███████╗███████╗███████╗╚█████╔╝  ░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║███████╗██████╔╝
    ╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝░╚════╝░  ░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░
    """)

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def opcao_invalida():
    print('Opção inválida!\n')
    input('Digite uma tecla para voltar ao menu principal.')
    main()

def cadastrar_novo_restaurante():
    os.system('clear')
    print('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    input('Digite uma tecla para voltar ao menu principal! ')
    main()

def listar_novos_restaurantes():
    os.system('clear')
    for i in restaurantes:
        print(f'.{i}')

    input('Digite uma tecla para voltar ao menu principal! ')
    main()

def escolher_opcao():

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opcao: {opcao_escolhida}')

        def ativar_app():
            os.system('clear')
            print('Ativacao de Restaurante')

        def finalizar_app():
            os.system('clear')
            print('Você saiu!')
        
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_novos_restaurantes()
        elif opcao_escolhida == 3:
            ativar_app()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
def main():
    os.system('clear')
    exibir_logo_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()




#Interpolar: juntar um texto com variáveis (formatação f-string)