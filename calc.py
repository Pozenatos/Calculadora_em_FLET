import flet as ft

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
            title_medium=ft.TextStyle(size=26)
        )
    )
    
    result = ft.Text(
        int(),
        size=60
    )

        
    def digito6(e):
        result.value = "6"  # Coloca o texto "6" (use aspas para ser texto)
        result.update()     # <--- O SEGREDO! Manda o Flet redesenhar o texto na tela
        print("Cliquei no 6") # Adicione isso para ver no terminal se funcionou

  

    visor = ft.Container( 
        result,
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
                                
                            ),
                            ft.Container( #Segunda Linha
                                    ft.Text("7", color="white", size=30 ),
                                    border_radius = 100,
                                    alignment=ft.alignment.center,
                                    ink=True,    
                                    expand=1,
                            ),
                            ft.Container( #Terceira Linha
                                    ft.Text("4", color="white", size=30 ),
                                    border_radius = 100,
                                    alignment=ft.alignment.center,
                                    ink=True,    
                                    expand=1,
                            ),
                            ft.Container( #Quarta Linha
                                    ft.Text("1", color="white", size=30 ),
                                    border_radius = 100,
                                    alignment=ft.alignment.center,
                                    ink=True,     
                                    expand=1,
                            ),
                            ft.Container( #Quinta Linha
                                    ft.Text("⌫", color="#FF8400", size=30 ),
                                    border_radius = 100,
                                    alignment=ft.alignment.center,
                                    ink=True,    
                                    expand=1,
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
                            ),
                            ft.Container( #Terceira Linha
                                    ft.Text("5", color="white", size=30 ),
                                    border_radius = 100,
                                    alignment=ft.alignment.center,
                                    ink=True,    
                                    expand=1,
                            ),
                            ft.Container( #Quarta Linha
                                    ft.Text("2", color="white", size=30 ),
                                    border_radius = 100,
                                    alignment=ft.alignment.center,
                                    ink=True,    
                                    expand=1,
                            ),
                            ft.Container( #Quinta Linha
                                    ft.Text("0", color="white", size=30 ),
                                    border_radius = 100,
                                    alignment=ft.alignment.center,
                                    ink=True,    
                                    expand=1,
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
                            ),
                            ft.Container( #Quinta Linha
                                    ft.Text(",", color="white", size=30 ),
                                    border_radius = 100,
                                    alignment=ft.alignment.center,
                                    ink=True,    
                                    expand=1,
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