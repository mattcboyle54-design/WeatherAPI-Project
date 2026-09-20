from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.textinput import TextInput
from Weather import get_weather
from Weather import save_data
from Weather import get_file

#Directions for how to build the widget/kivy object
class Menu(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #creates top actionbar in app to add different cities 
        self.actionbar = FloatLayout(size_hint=(1, None), height=50)
        self.actionbar.pos_hint = {'top': 1}  
        
        #draws background rectangle for the actionbar
        with self.actionbar.canvas.before:
            Color(0.5, 0.5, 0.5, 1) 
            self.rect = Rectangle(pos=self.actionbar.pos, size=self.actionbar.size)

        
        self.actionbar.bind(pos=self.update_rect, size=self.update_rect) #creates dynamic object 

        
        self.label = Label(text="Add a location:", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.01, 'center_y': 0.5})
        self.actionbar.add_widget(self.label) #creates location label

        self.inputs = TextInput(multiline=False, size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.2, 'center_y': 0.5})
        self.actionbar.add_widget(self.inputs) #creates input for city location 

        self.button = Button(background_normal='source/button.png',
                        background_down='source/button.png',
                        size_hint=(None, None),
                        size=(50, 50),
                        pos_hint={'right': 0.99, 'center_y': 0.5})
        self.button.bind(on_press = self.callback) #give input button functionality to enter information 
        self.actionbar.add_widget(self.button) #creates input button
        self.add_widget(self.actionbar) #adds whole actionbar to the window 

        temp = get_file()
        self.module = BoxLayout(orientation = 'vertical', padding = 10, spacing = 10,)
        for items in temp: 
             label_text = (f"{items.get('location')}          {items.get('temp')}°F\n"
                           f"{items.get('weather')}          H: {items.get('temp_max')}°  L:{items.get('temp_min')}")
             label = Label(text=label_text)
             self.module.add_widget(label)
        self.add_widget(self.module)#creates weather widgets 

    #reloads weather widgets when new locations is added 
    def makeModules(self,instance): 
        temp = get_file()
        self.module = BoxLayout(orientation = 'vertical', padding = 10, spacing = 10,)
        for items in temp: 
             label_text = (f"{items.get('location')}          {items.get('temp')}°F\n"
                           f"{items.get('weather')}          H: {items.get('temp_max')}°  L:{items.get('temp_min')}")
             label = Label(text=label_text)
             self.module.add_widget(label)
        self.add_widget(self.module)

    #actions on button press 
    def callback(self, instance):
        if not self.inputs.text:
            print("EMPTY STRING")
        else:
            data = get_weather('132843fdcf70be79b9cbbfcd89dd9058', self.inputs.text)
            if data is not None:
                save_data(self.inputs.text, data)
                self.module.clear_widgets()
                self.makeModules(instance)  # Corrected function call
            else:
                print("Failed to fetch weather data.")
    #keeps dynamic objects 
    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

#Creates Kivy object using directons from menu 
class MyApp(App):
    def build(self):
        return Menu()

#runs the widget/app
if __name__ == "__main__":
    MyApp().run()
