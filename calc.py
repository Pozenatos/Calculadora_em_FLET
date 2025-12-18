import flet as ft
import math as mat

def main(page: ft.Page):

    page.window.width = 360
    page.window.height = 640
    page.expand=True
    page.window_resizable = False 
    page.padding=0
    page.bgcolor="black"

    page.theme = ft.Theme(
        text_theme=ft.TextTheme(
            # body_medium é o padrão para ft.Text()
            body_medium=ft.TextStyle(size=20, color="white"), 
            
            # label_large é o padrão para textos de botões (ElevatedButton, etc)
            label_large=ft.TextStyle(size=20, weight=ft.FontWeight.BOLD),
            
            # title_medium é usado frequentemente em listas e subtítulos
            title_medium=ft.TextStyle(size=12)
        )
    )
    
    texto_visor = ft.Text(
        str("0"),
        size=60,
    )

    def limpar_tudo(e):
        texto_visor.value = "0"
        texto_visor.update()
    
    def digito0(e):
        if len (texto_visor.value) == 12:
            return

        valor_atual = str(texto_visor.value)
        if valor_atual == "0":
            texto_visor.value = "0"
        else:
            texto_visor.value = valor_atual + "0" 
        texto_visor.update()

    def digito1(e):
        if len (texto_visor.value) == 12:
            return

        valor_atual = str(texto_visor.value)
        if valor_atual == "0":
            texto_visor.value = "1"
        else:
            texto_visor.value = valor_atual + "1" 
        texto_visor.update()

    def digito2(e):
        if len (texto_visor.value) == 12:
            return

        valor_atual = str(texto_visor.value)
        if valor_atual == "0":
            texto_visor.value = "2"
        else:
            texto_visor.value = valor_atual + "2" 
        texto_visor.update()
    
    def digito3(e):
        if len (texto_visor.value) == 12:
            return

        valor_atual = str(texto_visor.value)
        if valor_atual == "0":
            texto_visor.value = "3"
        else:
            texto_visor.value = valor_atual + "3" 
        texto_visor.update()
    
    def digito4(e):
        if len (texto_visor.value) == 12:
            return

        valor_atual = str(texto_visor.value)
        if valor_atual == "0":
            texto_visor.value = "4"
        else:
            texto_visor.value = valor_atual + "4" 
        texto_visor.update()
    
    def digito5(e):
        if len (texto_visor.value) == 12:
            return

        valor_atual = str(texto_visor.value)
        if valor_atual == "0":
            texto_visor.value = "5"
        else:
            texto_visor.value = valor_atual + "5" 
        texto_visor.update()

    def digito6(e):
        if len (texto_visor.value) == 12:
            return

        valor_atual = str(texto_visor.value)
        if valor_atual == "0":
            texto_visor.value = "6"
        else:
            texto_visor.value = valor_atual + "6" 
        texto_visor.update()

    def digito7(e):
        if len (texto_visor.value) == 12:
            return

        valor_atual = str(texto_visor.value)
        if valor_atual == "0":
            texto_visor.value = "7"
        else:
            texto_visor.value = valor_atual + "7" 
        texto_visor.update()

    def digito8(e):
        if len (texto_visor.value) == 12:
            return

        valor_atual = str(texto_visor.value)
        if valor_atual == "0":
            texto_visor.value = "8"
        else:
            texto_visor.value = valor_atual + "8" 
        texto_visor.update()

    def digito9(e):
        if len (texto_visor.value) == 12:
            return

        valor_atual = str(texto_visor.value)
        if valor_atual == "0":
            texto_visor.value = "9"
        else:
            texto_visor.value = valor_atual + "9" 
        texto_visor.update() 
    
    def apagar(e):
        valor_atual = str(texto_visor.value)

        if len(valor_atual) > 1:
            texto_visor.value = valor_atual[:-1]
        
        else:
            texto_visor.value = "0"
        texto_visor.update()

    def digito_virgula(e):
        valor_atual = str(texto_visor.value)
        if valor_atual == "0":
            texto_visor.value = "0"

        else:
            texto_visor.value = valor_atual + "," 
        texto_visor.update()  
  
    visor = ft.Container( 
        texto_visor,
        bgcolor="black",
        width=float("inf"),
        expand=2,
        alignment=ft.alignment.bottom_right,
    )

    teclado = ft.Container(
        ft.Row(
            expand=True,
            controls=[
                ft.Container( # primeira Coluna
                    ft.Column(
                        controls=[
                            ft.Container( #Primeira Linha
                                ft.Text("C", color="#FF8400", size=30 ),
                                border_radius = 100,
                                alignment=ft.alignment.center,
                                ink=True,
                                expand=1,

                                on_click = limpar_tudo
                                
                            ),
                            ft.Container( #Segunda Linha
                                    ft.Text("7", color="white", size=30 ),
                                    border_radius = 100,
                                    alignment=ft.alignment.center,
                                    ink=True,    
                                    expand=1,

                                     on_click = digito7
                            ),
                            ft.Container( #Terceira Linha
                                    ft.Text("4", color="white", size=30 ),
                                    border_radius = 100,
                                    alignment=ft.alignment.center,
                                    ink=True,    
                                    expand=1,

                                    on_click = digito4
                            ),
                            ft.Container( #Quarta Linha
                                    ft.Text("1", color="white", size=30 ),
                                    border_radius = 100,
                                    alignment=ft.alignment.center,
                                    ink=True,     
                                    expand=1,

                                    on_click = digito1
                            ),
                            ft.Container( #Quinta Linha
                                    ft.Text("⌫", color="#FF8400", size=30 ),
                                    border_radius = 100,
                                    alignment=ft.alignment.center,
                                    ink=True,    
                                    expand=1,

                                    on_click = apagar
                            ),

                        ]
                    ),
                    expand=1
                    
                ),
                ft.Container( # Segunda Coluna
                    ft.Column(
                        controls=[
                            ft.Container( #Primeira Linha
                                ft.Text("√", color="#FF8400", size=30, weight="bold" ),
                                border_radius = 100,
                                alignment=ft.alignment.center,
                                ink=True,expand=1,
                            ),
                            ft.Container( #Segunda Linha
                                    ft.Text("8", color="white", size=30 ),
                                    border_radius = 100,
                                    alignment=ft.alignment.center,
                                    ink=True,   
                                    expand=1,

                                    on_click = digito8
                            ),
                            ft.Container( #Terceira Linha
                                    ft.Text("5", color="white", size=30 ),
                                    border_radius = 100,
                                    alignment=ft.alignment.center,
                                    ink=True,    
                                    expand=1,

                                    on_click = digito5
                            ),
                            ft.Container( #Quarta Linha
                                    ft.Text("2", color="white", size=30 ),
                                    border_radius = 100,
                                    alignment=ft.alignment.center,
                                    ink=True,    
                                    expand=1,

                                    on_click = digito2
                            ),
                            ft.Container( #Quinta Linha
                                    ft.Text("0", color="white", size=30 ),
                                    border_radius = 100,
                                    alignment=ft.alignment.center,
                                    ink=True,    
                                    expand=1,

                                    on_click = digito0
                            ),
                            

                        ]
                    ),
                    expand=1
                ),
                ft.Container( # Terceira Coluna
                    ft.Column(
                        controls=[
                            ft.Container( #Primeira Linha
                                ft.Text("%", color="#FF8400", size=30, weight="bold" ),
                                border_radius = 100,
                                alignment=ft.alignment.center,
                                ink=True,
                                expand=1,
                            ),
                            ft.Container( #Segunda Linha
                                    ft.Text("9", color="white", size=30 ),
                                    border_radius = 100,
                                    alignment=ft.alignment.center,
                                    ink=True,    
                                    expand=1,

                                    on_click = digito9
                            ),
                            ft.Container( #Terceira Linha
                                    ft.Text("6", color="white", size=30 ),
                                    border_radius = 100,
                                    alignment=ft.alignment.center,
                                    ink=True,   
                                    expand=1,

                                    on_click = digito6  
                            ),
                            ft.Container( #Quarta Linha
                                    ft.Text("3", color="white", size=30 ),
                                    border_radius = 100,
                                    alignment=ft.alignment.center,
                                    ink=True,   
                                    expand=1,

                                    on_click = digito3
                            ),
                            ft.Container( #Quinta Linha
                                    ft.Text(",", color="white", size=30 ),
                                    border_radius = 100,
                                    alignment=ft.alignment.center,
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
                                alignment=ft.alignment.center,
                                ink=True,
                                expand=1,
                            ),
                            ft.Container( #Segunda Linha
                                    ft.Text("×", color="#FF8400", size=40 ),
                                    border_radius = 100,
                                    alignment=ft.alignment.center,
                                    ink=True,   
                                    expand=1,
                            ),
                            ft.Container( #Terceira Linha
                                    ft.Text("-", color="#FF8400", size=40 ),
                                    border_radius = 100,
                                    alignment=ft.alignment.center,
                                    ink=True,   
                                    expand=1,
                            ),
                            ft.Container( #Quarta Linha
                                    ft.Text("+", color="#FF8400", size=40 ),
                                    border_radius = 100,
                                    alignment=ft.alignment.center,
                                    ink=True,   
                                    expand=1,
                            ),
                            ft.Container( #Quinta Linha
                                    ft.Text("=", color="white", size=40 ),
                                    border_radius = 40,
                                    bgcolor="#FF931F",
                                    alignment=ft.alignment.center,
                                    ink=True,    
                                    expand=1,
                            ),
                        ]
                    ),
                    expand=1
                ),
            ]
        ),
        border_radius=25,
        bgcolor='black',
        padding=25,
        expand=3
        

    )

    page.add(
        ft.Column( #collumn pai
            spacing=0,
            expand=True,
            controls=[visor,teclado]
        )
    )

    page.update()

ft.app(target=main)