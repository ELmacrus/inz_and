from kivy.app import App
#from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from things import show_heatmap

class SimpleKivy(App):
    def build(self):
        layout = GridLayout(cols=2)
        layout.add_widget(Image(source='mylogo.jpg'))
        layout.add_widget(Image(source=show_heatmap()))
        return layout


SimpleKivy().run()