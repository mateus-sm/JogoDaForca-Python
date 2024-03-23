# Jogo da forca

#Desenhos Ascii
des_forca = ['''
 +---+
 |   |
     |
     |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
     |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
 |   |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |    
=========
''']

arvores_frutiferas = [
    'Macieira',
    'Pereira',
    'Cerejeira',
    'Pessegueiro',
    'Ameixeira',
    'Videira',
    'Morangueiro',
    'Limoeiro',
    'Laranjeira',
    'Abacateiro',
    'Mangueira',
    'Bananeira',
    'Kiwi',
    'Romãzeira',
    'Coqueiro',
    'Nogueira-Pecã',
    'Figueira',
    'Cajueiro',
    'Ameixeira-amarela',
    'Framboeseira',
    'Amoreira',
    'Abacaxizeiro',
    'Cerejeira-do-rio-grande',
    'Goizeiro',
    'Maracujazeiro',
    'Figueira-da-índia',
    'Nespereira',
    'Lichieira',
    'Goiabeira',
    'Sapote'
]

#Fonte: https://ascii.co.uk/art/tree
arvore_ascii = """
                                         . . .
                                       .        .  .     ..    .
                                    .                 .         .  .
                                                   .
                                                  .                ..
                                  .          .            .              .
                                  .            '.,        .               .
                                  .              'b      *
                                   .              '$    #.                ..
                                  .    .           $:   #:               .
                                ..      .  ..      *#  @):        .   . .
                                             .     :@,@):   ,.**:'   .
                                 .      .,         :@@*: ..**'      .   .
                                          '#o.    .:(@'.@*"'  .
                                  .  .       'bq,..:,@@*'   ,*      .  .
                                            ,p$q8,:@)'  .p*'      .
                                     .     '  . '@@Pp@@*'    .  .
                                      .  . ..    Y7'.'     .  .
                                                :@):.
                                              .:@:'.
                                           .::(@:.
"""

#Fonte: https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
you_win = """

 ____  ____                 ____      ____  _            _  
|_  _||_  _|               |_  _|    |_  _|(_)          | | 
  \ \  / / .--.   __   _     \ \  /\  / /  __   _ .--.  | | 
   \ \/ // .'`\ \[  | | |     \ \/  \/ /  [  | [ `.-. | | | 
   _|  |_| \__. | | \_/ |,     \  /\  /    | |  | | | | |_| 
  |______|'.__.'  '.__.'_/      \/  \/    [___][___||__](_) 

"""

#Fonte: https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
game_over = """
 ______     ______     __    __     ______        ______     __   __   ______     ______    
/\  ___\   /\  __ \   /\ "-./  \   /\  ___\      /\  __ \   /\ \ / /  /\  ___\   /\  == \   
\ \ \__ \  \ \  __ \  \ \ \-./\ \  \ \  __\      \ \ \/\ \  \ \ \'/   \ \  __\   \ \  __<   
 \ \_____\  \ \_\ \_\  \ \_\ \ \_\  \ \_____\     \ \_____\  \ \__|    \ \_____\  \ \_\ \_\ 
  \/_____/   \/_/\/_/   \/_/  \/_/   \/_____/      \/_____/   \/_/      \/_____/   \/_/ /_/ 
                                                                                            
"""

import random

# Inicio do codigo

# Tamanho das linhas.
largura_linha = 95

# Menu inicial.
print("Bem-vindo ao jogo da forca.".center(largura_linha))
print("O jogo tem como tema árvores frutíferas.".center(largura_linha))
print("Você pode jogar com esse tema ou fornecer sua própria lista de palavras.".center(largura_linha))
print("Deseja iniciar o jogo ou criar uma lista de palavras personalizada?".center(largura_linha))
print("1. Iniciar o jogo.")
print("2. Criar lista.")

# Repetição até que uma opção valida seja digitada.
opcao1_menu = int(input())
while opcao1_menu != 1 and opcao1_menu != 2:
    print("Opção invalida, digite novamente!")
    opcao1_menu = int(input())

# Caso a opção for 1 sorteia posição aleatoria da lista de arvores, caso contrario faz lista personalizada.
if opcao1_menu == 1:
    # Decide um número aleatório e usa como index da lista para para definir palavra aleatória.
    pos = random.randint(0, (len(arvores_frutiferas) - 1))
    lista_final = arvores_frutiferas[pos]
    lista_final = lista_final.lower()
else:
    lista_personalizada = []
    print("Digite uma palavra seguida de 'Enter' para adicionar a lista, digite 'SAIR' para encerrar.".center(largura_linha))
    
    # Repetição para obter os elementos da lista personalizada.
    palavra_inserir = input()
    while palavra_inserir != 'SAIR':
     lista_personalizada.append(palavra_inserir) 
     palavra_inserir = input()

    # Decide um número aleatório e usa como index da lista para para definir palavra aleatória.
    pos = random.randint(0, (len(lista_personalizada) - 1))
    lista_final = lista_personalizada[pos]
    lista_final = lista_final.lower()

# Inicio do jogo.
print("***** Jogo da Forca *****".center(largura_linha))
# Declara lista com underscores ou hifens baseada na lista final
# para todos os elementos em lista final, se o elemento for um hifem, 
# lista chute recebe um hifem,
# se for um espaço recebe um espaço,
# caso contrario recebe underscore.
lista_chute = []
for letra in lista_final:
     if letra == " ":
          lista_chute.append(" ")
     else:
          if letra == "-":
               lista_chute.append("-")
          else:
               lista_chute.append("_")

print("A qualquer momento, caso souber a palavra toda, é permitido arriscar e chutar!")
# Imprime lista, se o local for hifem ou underscore imprime os mesmos,
# caso for letra imprime a mesma.
for letra in lista_chute:
     if letra == "_":
          print("_", end=" ")
     elif letra == "-":
          print("-", end=" ")
     else:
          print(letra, end=" ")
print(" ")

cont_erros = 0
vitoria = False
derrota = False
# Enquanto vitória ou derrota não acontecerem execute.
while (not vitoria and not derrota):
     # Considera apenas primeiro digito da entrada.
     entrada = input("Digite seu chute: ").lower()
     if entrada == lista_final:
          vitoria = True
          continue
     else:
          chute = entrada[0]

     # Caso chute esteja em lista.
     if (chute in lista_final):
          
          # Enumerate enumera os valores do index e valores do conteúdo
          # para todo index e conteúdo em lista.
          for index_lista, valor_lista in enumerate(lista_final):
               # Se o valor do conteúdo for igual o chute.
               if valor_lista == chute:
                    # Coloque o chute naquela posição.
                    lista_chute[index_lista] = valor_lista
                    # Primeira letra maiúscula.
                    if index_lista == 0:
                         lista_chute[index_lista] = valor_lista.upper()
          
          # Retorna true se acabarem os traços.
          vitoria = "_" not in lista_chute

          # Se acertar imprime a lista atualizada com acerto.
          for letra in lista_chute:
               if letra == "_":
                    print("_", end=" ")
               elif letra == "-":
                    print("-", end=" ")
               else:
                    print(letra, end=" ")
          print(" ")           
     else:
          # Aumenta o contador de erros, utilizar para indexar o desenho.
          cont_erros += 1     

          # Se o contador chegar no final da forca ativa derrota.
          if cont_erros == len(des_forca):
               derrota = True
          else:
               print(des_forca[cont_erros])

# Ao sair da repetição, se vitória imprime mensagens de vitória,
# caso derrota imprime mensagem de derrota e resposta correta.
if vitoria:
    # Se vitória e usado a lista padrão mostra desenho de árvore, 
    # mensagem de vitoria e resposta correta, caso lista for 
    # personalizada, mostra outro desenho, mensagem de 
    # vitória e resposta correta.
    if opcao1_menu == 1:
          print(arvore_ascii)
          print("You Win!".center(largura_linha))
          print(f"A resposta é: {lista_final.capitalize()}!")
    else:
          print(you_win)
          print(f"Resposta correta: {lista_final.capitalize()}!")
else:
    print(game_over)
    print(f"Resposta correta: {lista_final.capitalize()}!")

# Pedido de entrada do usuário para finalizar o programa.
input("Press Enter to continue...")
