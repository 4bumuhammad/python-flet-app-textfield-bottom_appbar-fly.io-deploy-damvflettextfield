import flet as ft

def main(page: ft.Page):
    page.title = "DAMv Test" 

    page.appbar = ft.AppBar(
        title=ft.Text("Flet Test Home Page", color=ft.colors.WHITE),  
        bgcolor=ft.colors.BLUE,  
        center_title=True  
    )

    text_field_name = ft.TextField(value="", 
                              label="Name",
                              hint_text="Enter text here", 
                              text_size=50,
                              color=ft.colors.RED,
                              border_color=ft.colors.BLUE_200, 
                              capitalization="characters",
                              border=ft.InputBorder.UNDERLINE)

    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=ft.colors.BLUE,
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.MENU, icon_color=ft.colors.WHITE),
                ft.Container(expand=True),
                ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.WHITE),
                ft.IconButton(icon=ft.icons.FAVORITE, icon_color=ft.colors.WHITE),
            ]
        ),
    )

    page.add(text_field_name)

    
ft.app(target=main,port=8080, view=None)

## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Berhasil
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
