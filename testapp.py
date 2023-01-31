#create and launch a kivy application
from kivy.app import App 
from kivy.uix.label import Label #allow us to type title to screen
from kivy.core.window import Window
#use Object Oriented Programming  
#BasicApp inherits all properties of App class 
class BasicApp(App):
    # function "Build" from Kivy, always return root widget 
    # root widget = parent widget
    # we only have the label as a widget 
    def build(self): 
        Window.clearcolor = (0,191,255) #rgb value for color of app
        label = Label(text="Hello World \nMy first app.")
        return label 

#instance of Basic App class
app = BasicApp()

#open kivy interface and run
app.run()
