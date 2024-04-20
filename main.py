import flet as ft

class App (ft.UserControl):
    #The class is used to define the UI of the page, here we define all the structures our page should have.
    def build(self):
        first_name = ft.Row(
            controls=[
                ft.Text(
                    value="Email: ",
                    size=55
                        ),
                
                ft.TextField(),
                ]
        )
        main_container = ft.Container(
            #the container is one of the major container controls in flet, it works more like a div in html, it can contain certain attributes which will be specified to the container only
            width=400,
            height = 400,
            bgcolor= ft.colors.BLUE_GREY_400,
            # border_radius=ft.border_radius.all(25),
            border_radius = ft.border_radius.only(top_right=25, bottom_left=25),
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=[ft.colors.BLUE, ft.colors.YELLOW],
                ),
            padding=ft.padding.all(25),
            
            
            #The content attribute in a container control is how we are able to add other controls to the container, note only one control can be passed here, so we will have to use other container controls like rows, coloumns and even another container. 
            content= ft.Column(
            controls=[
                ft.Text(
                value="Hello world", 
                color="black",
                text_align="center",
                weight = "w900", #boldness
                size = 25
                ),
                
                ft.Text(
                value="Precious Ojogu", 
                color="black",
                text_align="center"),
                
                ]
            ),   
        )
        
        return main_container
    
def main(page: ft.Page):
    #This is the main and entry point of our code, it specifies the page, here we set attributes attached to the window page
    #Page is the root container control, i.e it is a control that can nest other controls 
    #this are some attributes associated with the page container
    page.window_height = 800
    page.window_width = 700
    page.bgcolor = ft.colors.WHITE
    ft.colors.WHITE60
    page.window_resizable = False
    
    #creating an instance of the App class where we define our controls and design
    app = App()
    
    #adding the App object(our design) to the page, this is what renders the app(interface) unto the page
    page.add(
        app
    )
    
    # This tells Flet to use the main function as the starting point for your application. When you run the program, Flet will execute the code inside main.
if __name__ == "__main__":
    ft.app(target= main)