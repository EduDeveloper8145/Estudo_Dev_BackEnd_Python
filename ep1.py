import os

restaurantes = [{'nome':'GildoLanches', 'categoria':'Fast-Food', 'ativo': True},
                {'nome': 'Pizzaria do Gordo', 'categoria': 'Pizza', 'ativo': False},
                {'nome': 'Cafetao Cafeteria', 'categoria': 'Cafeteria', 'ativo': True}]

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

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal! ')
    main()

def exibir_subtitulos(texto):
    os.system('clear')
    print(texto)

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    exibir_subtitulos('Cadastro de Novos Restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_novos_restaurantes():
    exibir_subtitulos('Listagem de Restaurantes')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria =  restaurante['categoria']
        ativo = 'ativado' if i['ativo'] else 'desativado'
        print(f'- NOME: {nome_restaurante} | CATEGORIA: {categoria} | SITUACAO: {ativo}')
    voltar_ao_menu_principal()

def alterando_estado_do_restaurante():
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

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opcao: {opcao_escolhida}')

        def ativar_app():
            os.system('clear')
            print('Ativacao de Restaurante')

        def finalizar_app():
            exibir_subtitulos('Finalizar Programa!')
        
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_novos_restaurantes()
        elif opcao_escolhida == 3:
            alterando_estado_do_restaurante()
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
#Tupla: são arrays imutáveis, para situações que precisam armazenar algo e não modificar. Ex.: coordenadas geográficas. Utilizada usando ()
#Lista: são arrays mutáveis, para situações que podem sofrer modificações. Ex.: lista de compras. Utilizada usando []
# For deve ser utilizado quando se tem um número determinado de tentativas, já o while é utilizado para casos indeterminados.