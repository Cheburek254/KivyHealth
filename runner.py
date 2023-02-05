# напиши модуль для работы с анимацией
from kivy.animation import Animation
from kivy.properties import BooleanProperty, NumericProperty
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits
class Runner(BoxLayout):
    # сколько сделано перемещений вниз-вверх
    value = NumericProperty(0)
    # сделаны ли все перемещения
    finished = BooleanProperty(False)
    def __init__(self, total=10, steptime=1, **kwargs):
        super().__init__(**kwargs)
        self.total = total
        self.animation = (Animation(pos_hint={'top': 0.1}, duration=steptime/2)+ Animation(pos_hint={'top': 1.0}, duration=steptime/2))
        self.btn = Button(size_hint=(0.3, 0.2), pos_hint = {'center_x': 0.5}, background_color = (0.18, 0.07, 0.83, 1), markup=True)
        self.add_widget(self.btn)
        self.animation.on_progress = self.next
        
        

    def start(self, *args):
        self.value = 0
        self.finished = False
        self.animation.repeat = True
        self.animation.start(self.btn)

    def next(self, widget, step, *args):
        if step == 1.0:
           self.value += 1
           if self.value >= self.total:
               self.animation.repeat = False
               self.finished = True
