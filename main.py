import flet as ft

class App (ft.UserControl):
    def build(self):
        first_name = ft.Row(
            controls=[
                ft.Text(value="Email: "),
                ft.TextField(),
                ]
        )
        main_container = ft.Container(
            width=400,
            height = 400,
            bgcolor= ft.colors.BLUE_GREY_400,
            # border_radius=ft.border_radius.all(25),
            border_radius=ft.border_radius.only(top_right=25),
            border_radius=ft.border_radius.only(top_left=25),
            content= ft.Column(
            controls=[first_name]
            ),
            
        )
        return main_container
    
def main(page: ft.Page):
    page.window_height = 800
    page.window_width = 700
    page.bgcolor = ft.colors.WHITE
    ft.colors.WHITE60
    page.window_resizable = False
    
    
    app = App()
    page.add(
        app
    )
if __name__ == "__main__":
    ft.app(target= main)