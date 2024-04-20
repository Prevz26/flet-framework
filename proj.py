import flet as ft
class Login(ft.UserControl):
    def build(self):
        welcome_msg = ft.Text("Welcome Back!", color=ft.colors.BLUE, text_align="center", weight= "w900", size= 25)
        email = ft.Text(value="Email: ", size= 25, weight="w900")
        inner_container = ft.Container(
            height= 400,
            width= 300,
            border_radius= ft.border_radius.all(25),
            bgcolor=ft.colors.WHITE,
            content= ft.Column(
                # horizontal_alignment= "center",
                controls=[welcome_msg, email]
            )
        )
        
        outer_container = ft.Container(
            height=400,
            width=600,
            bgcolor= ft.colors.BLUE_GREY_300,
            border_radius= ft.border_radius.all(25),
            content= ft.Column(
                controls=[inner_container]
            )
        )
        return outer_container

def main(page:ft.Page):
    page.window_height = 600
    page.window_width = 700
    page.bgcolor = ft.colors.WHITE
    page.title = "LOGIN PAGE"
    page.window_resizable = False
    

    
    app = Login()
    page.add(app)
if __name__ == "__main__":
    ft.app(target=main)
    
