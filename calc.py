import flet as ft
import math as math
import re

# Configuração de proporção e personalização da tela
def main(page: ft.Page):
    page.window_width = 360
    page.window_height = 640
    page.window_resizable = False 
    page.expand = True
    page.padding = 0
    page.bgcolor = "black"

    page.theme = ft.Theme(
        text_theme=ft.TextTheme(
            body_medium=ft.TextStyle(size=20, color="white"), 
            label_large=ft.TextStyle(size=20, weight=ft.FontWeight.BOLD),
            title_medium=ft.TextStyle(size=12)
        )
    )
    
    # Caracteres que representam os números na parte superior
    texto_visor = ft.Text(
        str("0"),
        size=40,
    )

    # Função que limpa todos os caracteres no visor
    def limpar_tudo(e):
        texto_visor.value = "0"
        texto_visor.update()
    
    # Função que serve para todos os digitos numéricos
    def digitar_numero(numero):
        def adicionar(e):
            # Trava de 20 caracteres para não exceder o limite da tela
            if len(texto_visor.value) == 20:
                return
            
            valor_atual = str(texto_visor.value)
            
            # Se for 0 ou Erro, substitui. Se não, adicionar o número no final.
            if valor_atual in ["0", "Erro"]:
                texto_visor.value = str(numero)
            else:
                texto_visor.value = valor_atual + str(numero)
            
            texto_visor.update() #Atualiza o visor
        return adicionar 
    
    # Apaga o último caracter digitado
    def apagar(e):
        valor_atual = str(texto_visor.value)
        if len(valor_atual) > 1:
            texto_visor.value = valor_atual[:-1]
        else:
            texto_visor.value = "0"
        texto_visor.update()

    # Insere uma virgula no visor
    def digito_virgula(e):
        # Travinha básica de 20 caracteres pro visor não bugar
        if len(texto_visor.value) >= 20:
            return
        
        valor_atual = str(texto_visor.value)
        
        # Se o último botão clicado foi um sinal (+, -, etc), eu já coloco "0," 
        # Isso ajuda o usuário (ex: em vez de "+ ,", fica "+ 0,")
        if valor_atual[-1] in ["+", "-", "×", "÷"]:
            texto_visor.value = valor_atual + "0,"
            texto_visor.update()
            return

        # Aqui é onde eu descubro onde começa o último número da conta
        ultimo_operador = -1
        for op in ["+", "-", "×", "÷"]:
            # Procuro o operador mais próximo do final (da direita pra esquerda)
            posicao = valor_atual.rfind(op)
            if posicao > ultimo_operador:
                ultimo_operador = posicao
        
        # Pego só o pedaço do texto que vem DEPOIS do último sinal (o número atual)
        ultimo_bloco_numeral = valor_atual[ultimo_operador + 1:]
        
        # Só deixo colocar a vírgula se esse número específico ainda não tiver uma
        # Isso evita que o cara digite "5,5,5" e quebre tudo
        if "," not in ultimo_bloco_numeral:
            texto_visor.value = valor_atual + ","
            
        texto_visor.update() 
    
    # As quatros funções abaixo servem para inserir operadores binários no visor
    def digitar_operador(op):
        def adicionar(e):
            valor_atual = str(texto_visor.value)
            # Evita colocar dois operadores seguidos
            if valor_atual[-1] in ["+", "-", "×", "÷"] or valor_atual == "Erro":
                return
            else:
                texto_visor.value = valor_atual + op
            texto_visor.update()
        return adicionar

    # Esse operador é diferente caso o usuário queira somar com um número negativo
    def subtrair(e):
        valor_atual = str(texto_visor.value)
        if valor_atual in ["0", "Erro"]:
            texto_visor.value = "-" 
        elif valor_atual[-1] in ["×", "÷"]:
            return
        else:
            texto_visor.value = valor_atual + "-"
        texto_visor.update()
    

    # Seguimento de funções para inserir operadores unários
    def elevar_ao_quadrado(e):
        valor_atual = str(texto_visor.value)
        if valor_atual == "0" or valor_atual[-1] in ["+", "-", "×", "÷", "²", "!",] or valor_atual == "Erro":
            return
        else:
            texto_visor.value = valor_atual + "²"
        texto_visor.update()

    def calcular_fatorial(e):
        valor_atual = str(texto_visor.value)
        if valor_atual[-1].isdigit():
            texto_visor.value = valor_atual + "!"
        texto_visor.update()

    def calcular(e):
        
        try: # Try para evitar que o código quebre

            conta = texto_visor.value
            
            conta = conta.replace("²", "**2") # Traduz a potência para o Python
            
            conta = re.sub(r'(\d+)!', r'math.factorial(\1)', conta) # Procura um padrão que seja um número que termine com "!" e substitui para ser uma função do math
            
            conta = conta.replace("×", "*").replace("÷", "/").replace(",", ".") # Traduz os operadores para o python

            # Normalização de operadores adjacentes (Regra de Sinais)
            conta = conta.replace("+-", "-").replace("-+", "-")
            conta = conta.replace("++", "+").replace("--", "+")
            
            resultado = eval(conta) # O Eval é responsável por realizar o calculo
            
            texto_visor.value = str(round(resultado, 4)).replace(".", ",") # retorna o resultado da conta para o visor
        
        except Exception as err:
            print(f"Erro: {err}") 
            texto_visor.value = "Erro"
    
        texto_visor.update()
        
    # Container que representa o visor    
    visor = ft.Container( 
        texto_visor, # é os caracteres que irão estar dentro do visor
        padding=ft.Padding.only(right=25), # Afasta os caracteres da direita
        bgcolor="black", # Deixa o fundo preto
        width=float("inf"), # Garante que o visor ocupe toda a largura da tela.
        expand=2, # Faz com que o visor preencha 1/3 da tela
        alignment=ft.Alignment(1, 1), 
    )

    # Container que preenche 2/3 da tela para o teclado 
    teclado = ft.Container(
        ft.Row( # O Row faz com que as colunas fiquem uma do lado da outra
            expand=True, # Faz com o que o Row ocupe todo o espaço na horizontal
            controls=[ # É tudo que vai ficar armazenado dentro dessa Row
                ft.Container( # primeira Coluna
                    ft.Column( # Cria uma coluna que armazena todos esses container na vertical
                        controls=[ # É tudo que vai ficar armazenado dentro dessa coluna
                            ft.Container( #Primeira Linha (Leve em conta que todos esses containers são os botões da calculadora!)
                                ft.Text("C", color="#FF8400", size=30 ), # Define o caracter que estará dentro do botão, a cor e tamanho do caracter
                                border_radius = 100, # Faz o botão ter uma borda mais suave
                                alignment=ft.Alignment(0, 0), # Este comando faz com que o texto fique no centro do botão
                                ink=True, # Exibe uma sombra ao redor do botão ao ser clicado
                                expand=1, # Ocupa um devido espaço no teclado, colocar "expand=1" em todos esses containers faz com que eles fiquem em seus devidos lugares
                                on_click = limpar_tudo # Este on_click faz que este botão seja ligado diretamente com a função criada anteriormente
                            ),
                            ft.Container( #Segunda Linha
                                    ft.Text("7", color="white", size=30 ),
                                    border_radius = 100,
                                    alignment=ft.Alignment(0, 0),
                                    ink=True,    
                                    expand=1,
                                    on_click = digitar_numero(7)
                            ),
                            ft.Container( #Terceira Linha
                                    ft.Text("4", color="white", size=30 ),
                                    border_radius = 100,
                                    alignment=ft.Alignment(0, 0),
                                    ink=True,    
                                    expand=1,
                                    on_click = digitar_numero(4)
                            ),
                            ft.Container( #Quarta Linha
                                    ft.Text("1", color="white", size=30 ),
                                    border_radius = 100,
                                    alignment=ft.Alignment(0, 0),
                                    ink=True,     
                                    expand=1,
                                    on_click = digitar_numero(1)
                            ),
                            ft.Container( #Quinta Linha
                                    ft.Text("⌫", color="#FF8400", size=30 ),
                                    border_radius = 100,
                                    alignment=ft.Alignment(0, 0),
                                    ink=True,    
                                    expand=1,
                                    on_click = apagar
                            ),
                        ]
                    ),
                    expand=1 # Cumpre o mesmo papel que os expand's dos sub-container's dentro desse container, mas dessa vez faz com que o container não ocupe o espaço dos conatainer's abaixo
                ),
                ft.Container( # Segunda Coluna
                    ft.Column(
                        controls=[
                            ft.Container( #Primeira Linha
                                ft.Text("x!", color="#FF8400", size=30, weight="bold" ),
                                border_radius = 100,
                                alignment=ft.Alignment(0, 0),
                                ink=True,expand=1,
                                on_click=calcular_fatorial
                                
                            ),
                            ft.Container( #Segunda Linha
                                    ft.Text("8", color="white", size=30 ),
                                    border_radius = 100,
                                    alignment=ft.Alignment(0, 0),
                                    ink=True,   
                                    expand=1,
                                    on_click = digitar_numero(8)
                            ),
                            ft.Container( #Terceira Linha
                                    ft.Text("5", color="white", size=30 ),
                                    border_radius = 100,
                                    alignment=ft.Alignment(0, 0),
                                    ink=True,    
                                    expand=1,
                                    on_click = digitar_numero(5)
                            ),
                            ft.Container( #Quarta Linha
                                    ft.Text("2", color="white", size=30 ),
                                    border_radius = 100,
                                    alignment=ft.Alignment(0, 0),
                                    ink=True,    
                                    expand=1,
                                    on_click = digitar_numero(2)
                            ),
                            ft.Container( #Quinta Linha
                                    ft.Text("0", color="white", size=30 ),
                                    border_radius = 100,
                                    alignment=ft.Alignment(0, 0),
                                    ink=True,    
                                    expand=1,
                                    on_click = digitar_numero(0)
                            ),
                        ]
                    ),
                    expand=1
                ),
                ft.Container( # Terceira Coluna
                    ft.Column(
                        controls=[
                            ft.Container( #Primeira Linha
                                ft.Text("x²", color="#FF8400", size=30, weight="bold" ),
                                border_radius = 100,
                                alignment=ft.Alignment(0, 0),
                                ink=True,
                                expand=1,
                                on_click=elevar_ao_quadrado
                            ),
                            ft.Container( #Segunda Linha
                                    ft.Text("9", color="white", size=30 ),
                                    border_radius = 100,
                                    alignment=ft.Alignment(0, 0),
                                    ink=True,    
                                    expand=1,
                                    on_click = digitar_numero(9)
                            ),
                            ft.Container( #Terceira Linha
                                    ft.Text("6", color="white", size=30 ),
                                    border_radius = 100,
                                    alignment=ft.Alignment(0, 0),
                                    ink=True,   
                                    expand=1,
                                    on_click = digitar_numero(6)  
                            ),
                            ft.Container( #Quarta Linha
                                    ft.Text("3", color="white", size=30 ),
                                    border_radius = 100,
                                    alignment=ft.Alignment(0, 0),
                                    ink=True,   
                                    expand=1,
                                    on_click = digitar_numero(3)
                            ),
                            ft.Container( #Quinta Linha
                                    ft.Text(",", color="white", size=30 ),
                                    border_radius = 100,
                                    alignment=ft.Alignment(0, 0),
                                    ink=True,    
                                    expand=1,
                                    on_click = digito_virgula
                            ),
                        ]
                    ),
                    expand=1
                ),
                ft.Container( # Quarta Coluna
                    ft.Column(
                        controls=[
                            ft.Container( #Primeira Linha
                                ft.Text("÷", color="#FF8400", size=40 ),
                                border_radius = 100,
                                alignment=ft.Alignment(0, 0),
                                ink=True,
                                expand=1,
                                on_click = digitar_operador("÷")
                            ),
                            ft.Container( #Segunda Linha
                                    ft.Text("×", color="#FF8400", size=40 ),
                                    border_radius = 100,
                                    alignment=ft.Alignment(0, 0),
                                    ink=True,   
                                    expand=1,
                                    on_click = digitar_operador("×")
                            ),
                            ft.Container( #Terceira Linha
                                    ft.Text("-", color="#FF8400", size=40 ),
                                    border_radius = 100,
                                    alignment=ft.Alignment(0, 0),
                                    ink=True,   
                                    expand=1,
                                    on_click = subtrair
                            ),
                            ft.Container( #Quarta Linha
                                    ft.Text("+", color="#FF8400", size=40 ),
                                    border_radius = 100,
                                    alignment=ft.Alignment(0, 0),
                                    ink=True,   
                                    expand=1,
                                    on_click = digitar_operador("+")
                            ),
                            ft.Container( #Quinta Linha
                                    ft.Text("=", color="white", size=40 ),
                                    border_radius = 40,
                                    bgcolor="#FF931F",
                                    alignment=ft.Alignment(0, 0),
                                    ink=True,    
                                    expand=1,
                                    on_click = calcular
                            ),
                        ]
                    ),
                    expand=1
                ),
            ]
        ),
        bgcolor='black', # Deixa o fundo do teclado preto
        padding=25, # Deixa um espaçamento entre as bordas
        expand=3 # faz com que ocupe 2/3 da tela
    )

    page.add( # adiciona os componentes abaixo na página
        ft.Column( # É a coluna que engloba praticamente tudo que foi criado
            spacing=0, # Garante que não tenha nenhum espaço em branco entre o teclado e o visor
            expand=True, # Faz com que esta coluna preencha toda tela
            controls=[visor,teclado] # São os conteúdos dentro desta coluna principal
        )
    )
    page.update() # Atualiza a tela para o usuário

ft.run(main) # Essencial para que o flet funcione