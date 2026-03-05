import os

restaurantes = [{'nome':'GildoLanches', 'categoria':'Fast-Food', 'ativo': True},
                {'nome': 'Pizzaria do Gordo', 'categoria': 'Pizza', 'ativo': False},
                {'nome': 'Cafetao Cafeteria', 'categoria': 'Cafeteria', 'ativo': True}]

def exibir_logo_programa():
    '''
    Exibe a logo central do nome do sistema.
    '''

    print("""

░█████╗░░█████╗░██████╗░░█████╗░░██████╗████████╗██████╗░░█████╗░  ██████╗░███████╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗  ██╔══██╗██╔════╝
██║░░╚═╝███████║██║░░██║███████║╚█████╗░░░░██║░░░██████╔╝██║░░██║  ██║░░██║█████╗░░
██║░░██╗██╔══██║██║░░██║██╔══██║░╚═══██╗░░░██║░░░██╔══██╗██║░░██║  ██║░░██║██╔══╝░░
╚█████╔╝██║░░██║██████╔╝██║░░██║██████╔╝░░░██║░░░██║░░██║╚█████╔╝  ██████╔╝███████╗
░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ╚═════╝░╚══════╝

██████╗░███████╗░██████╗████████╗░█████╗░██╗░░░██╗██████╗░░█████╗░███╗░░██╗████████╗███████╗░██████╗
██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗██║░░░██║██╔══██╗██╔══██╗████╗░██║╚══██╔══╝██╔════╝██╔════╝
██████╔╝█████╗░░╚█████╗░░░░██║░░░███████║██║░░░██║██████╔╝███████║██╔██╗██║░░░██║░░░█████╗░░╚█████╗░
██╔══██╗██╔══╝░░░╚═══██╗░░░██║░░░██╔══██║██║░░░██║██╔══██╗██╔══██║██║╚████║░░░██║░░░██╔══╝░░░╚═══██╗
██║░░██║███████╗██████╔╝░░░██║░░░██║░░██║╚██████╔╝██║░░██║██║░░██║██║░╚███║░░░██║░░░███████╗██████╔╝
╚═╝░░╚═╝╚══════╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═════╝░
   
    """)

def exibir_opcoes():
    '''
    Exibe as opções possível de escolher dentro do sistema.
    '''

    print('1. Cadastrar Restaurante', '2. Listar Restaurantes', '3. Alternar Situação do Restaurante', '4. Sair\n', sep='\n')

def voltar_ao_menu_principal():
    '''
    Função para voltar ao menu principal toda vez que finalizar uma função.

    Input:
    - Tecla para sair

    '''

    input('\nDigite uma tecla para voltar ao menu principal! ')
    main()

def exibir_subtitulos(texto):
    '''
    Função criada para exibir os subtitulos das opções escolhidas, junto com a capacidade de limpeza do terminal

    Output:
    - Texto subtitulo arrumado e personalizado.

    '''

    os.system('clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)

def opcao_invalida():
    '''
    Função para se o usuário digitar alguma informação incorreta.

    '''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    '''
    Função para cadastrar o restaurante que deseja

    Inputs:
    - Nome do Restaurante
    - Categoria do Restaurante

    Output:
    - Cadastra o restaurante ao sistema

    '''
    exibir_subtitulos('Cadastro de Novos Restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_novos_restaurantes():
    '''
    Função para listar os restaurantes cadastrados e sua situação cadastral
    '''
    
    exibir_subtitulos('Listagem de Restaurantes')
    print(f'{"RESTAURANTES".ljust(22)} | {"CATEGORIA".ljust(20)} | {"SITUAÇÃO"}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria =  restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'. {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

def alterando_estado_do_restaurante():
    '''
    Função que altera o estado de atividade do restaurante de acordo como o sistema.

    Inputs:
    - Nome do Restaurante

    Output:
    - Mensagem informando que a situação cadastral do restaurante foi ativada/desativada
    '''

    exibir_subtitulos('Atualizando Estado do Restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja ativar/desativar estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso.' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso.'
            print(mensagem)

    if not restaurante_encontrado:
        print(f'Infelizmente o restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():

    '''
    Função para o usuário escolher uma opção de como deseja interagir com o sistema

    Inputs:
    - Número de opção

    Output:
    - Selecionar opção de acordo com número requisitado
    '''

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opcao: {opcao_escolhida}')

        def ativar_app():
            os.system('clear')
            print('Ativacao de Restaurante')

        def finalizar_app():
            exibir_subtitulos('Finalizar Programa!')
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_novos_restaurantes()
            case 3:
                alterando_estado_do_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
            
    except ValueError:
        opcao_invalida()
        
def main():

    '''
    Função principal do código, do qual é capaz de chamar todas as funções e também botar diretrizes gerais a todo o código
    '''

    os.system('clear')
    exibir_logo_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()

