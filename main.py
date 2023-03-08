from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits
from ruffier import test
from kivy.clock import Clock
from seconds import Seconds
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown
from instructions import *
from main_app import *
from train import *
from runner import *
from kivy.animation import Animation
from kivy.lang.builder import Builder
from kivy.uix.scrollview import ScrollView
from texst import *


KV = '''
Screen:

    MDRoundFlatButton:
       text: "MDROUNDFLATBUTTON"
'''


    

color = (0.27, 0.27, 0.27, 1)
btn_color = (0.79, 0.6, 0, 1)#(0.41, 0.49, 1, 1)
a = (0,0,0,1)
b = (0.65,0.54,0,1)
c = (0.43, 0.4, 0.84, 1)
d = (0.2,0.87,0.42,1)
a_btn = (0.18,0.18,0.18,1)
b_btn = (0.38,0.32,0,1)
c_btn = (0.18, 0.07, 0.83, 1)
d_btn = (0.07,0.3,0.08,1)
black = (0, 0, 0, 1)

class Policy(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        s = ScrollView(size_hint=(1,1))
        
        self.label = Label(text = sogl,halign = 'right',size_hint_y = None)
        
        '''w = label.texture_size[0]
        h = label.texture_size[1]
        label.height = h'''
        s.add_widget(self.label)
        self.label.bind(size = self.resize)
        self.btn = Button(text ='[b]' +  'Принять'+ '[/b]', size_hint=(0.5, 0.4), pos_hint = {'center_x': 0.5}, markup=True,color=black,background_normal = 'button_horizontal.png',font_size = 90)
        self.btn.on_press = self.next
        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        outer.add_widget(s)
        outer.add_widget(self.btn)
        self.add_widget(outer)
    def next(self):
        
        self.manager.current = 'first'
    def resize(self,w,h):
        self.label.text_size = (self.label.width,None)
        self.label.texture_update()
        self.label.height = self.label.texture_size[1]



class First(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        instr = Label(text = ti,font_size = 45,halign = 'justify')
        self.btn = Button(text ='[b]' +  'далее'+ '[/b]', size_hint=(0.5, 0.4), pos_hint = {'center_x': 0.5}, markup=True,color=black,background_normal = 'button_horizontal.png',font_size = 90)
        self.btn.on_press = self.next
        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        '''self.btn3 = Button(text ='[b]' +  'Пользовательское\nсоглашение'+ '[/b]', size_hint=(0.5, 0.4), pos_hint = {'center_x': 0.5}, markup=True,color=black,background_normal = 'button_horizontal.png',font_size = 50)
        self.btn3.on_press = self.next3'''
        l1 = BoxLayout()
        outer.add_widget(instr)
        l1.add_widget(self.btn)
        #l1.add_widget(self.btn3)
        outer.add_widget(l1)
        self.add_widget(outer)
    def next(self):
        
        self.manager.current = 'main'
    def next3(self):
        self.manager.current = 'policy'
        

class Main(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        instr = Label(text = '[b]'+'KivyHealth',halign = 'right',markup = True,font_size = 90)
        '''dropdown = DropDown()
        mainbutton = Button(text='Меню',  size_hint=(0.7, 0.6), pos_hint = {'center_x': 0.5})'''
        self.btn1 = Button(text ='[b]' +  'Тест\nРуфье'+ '[/b]', size_hint=(0.8, 0.7), pos_hint = {'center_x': 0.5}, markup=True,color=black,background_normal = 'button_vertical.png',font_size = 60)
        self.btn1.on_press = self.next1
        self.btn2 = Button(text ='[b]' +  'Тренировки'+ '[/b]', size_hint=(0.8, 0.7), pos_hint = {'center_x': 0.5},markup=True,color=black,background_normal = 'button_vertical.png',font_size = 50)
        self.btn2.on_press = self.next2
        '''self.btn3 = Button(text ='[b]' +  'Пользовательское\nсоглашение'+ '[/b]', size_hint=(0.8, 0.7), pos_hint = {'center_x': 0.5}, markup=True,color=black,background_normal = 'button_vertical.png',font_size = 50)
        self.btn3.on_press = self.next3'''
        wimg = Image(source='main_icon.png')
        line1 = BoxLayout( padding = 8, spacing = 8)
        line2= BoxLayout(orientation='vertical')
        #line1.add_widget(line2)
        line2.add_widget(instr)
        line2.add_widget(wimg)
        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        outer.add_widget(self.btn1)
        outer.add_widget(self.btn2)
        #outer.add_widget(self.btn3)
        line1.add_widget(line2)
        line1.add_widget(outer)
        
        '''
        line1 = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        dropdown.add_widget(self.btn1)
        dropdown.add_widget(self.btn2)
        dropdown.add_widget(self.btn3)
        mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
        
        line1.add_widget(dropdown)'''

        self.add_widget(line1)
    def next1(self):
        self.manager.current = 'test'
    def next2(self):
        self.manager.current = 'train_main'
    def next3(self):
        self.manager.current = 'policy'
        


'''
class Settings(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        instr = Label(text = 'В настройках вы можете изменить цвет приложения')
        self.btn = Button(text ='[u]' +  'НАЗАД'+ '[/u]', size_hint=(0.3, 0.2), pos_hint = {'center_x': 0.5}, background_color = btn_color, markup=True)
        self.btn.on_press = self.next


        self.btna = Button(text ='[u]' +  'Сменить цвет на черный'+ '[/u]', size_hint=(0.3, 0.2), pos_hint = {'center_x': 0.5}, background_color = a_btn, markup=True)
        self.btna.on_press = self.nexta

        self.btnb = Button(text ='[u]' +  'Сменить цвет на желтый'+ '[/u]', size_hint=(0.3, 0.2), pos_hint = {'center_x': 0.5}, background_color = b_btn, markup=True)
        self.btnb.on_press = self.nextb

        self.btnc = Button(text ='[u]' +  'Сменить цвет на стандартный'+ '[/u]', size_hint=(0.3, 0.2), pos_hint = {'center_x': 0.5}, background_color = c_btn, markup=True)
        self.btnc.on_press = self.nextc

        self.btnd = Button(text ='[u]' +  'Сменить цвет на зеленый'+ '[/u]', size_hint=(0.3, 0.2), pos_hint = {'center_x': 0.5}, background_color = d_btn, markup=True)
        self.btnd.on_press = self.nextd

        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        outer.add_widget(instr)
        outer.add_widget(self.btna)
        outer.add_widget(self.btnb)
        outer.add_widget(self.btnc)
        outer.add_widget(self.btnd)
        outer.add_widget(self.btn)
        self.add_widget(outer)
    def next(self):
        
        self.manager.current = 'main'
    def nexta(self):
        global color
        global a
        global a_btn
        global btn_color
        color = a
        btn_color = btn_color
        Window.clearcolor = color
        self.manager.current = 'main'
    def nextb(self):
        global color
        global btn_color
        global b
        global b_btn
        color = b
        btn_color = b_btn
        Window.clearcolor = color
        self.manager.current = 'main'
    def nextc(self):
        global color
        global btn_color
        global c
        global c_btn
        color = c
        btn_color = c_btn
        Window.clearcolor = color
        self.manager.current = 'main'
    def nextd(self):
        global color
        global btn_color
        global d
        global d_btn
        color = d
        btn_color = d_btn
        Window.clearcolor = color
        self.manager.current = 'main'

'''

class KivyHealth(App):
    def build(self):
        sm = ScreenManager()
        
            
        sm.add_widget(First(name='first'))
        sm.add_widget(Main(name='main'))
        sm.add_widget(Policy(name='policy'))

        sm.add_widget(train_main(name='train_main'))
        sm.add_widget(tr_l1_1(name='tr_l1_1'))
        sm.add_widget(tr_l1_2(name='tr_l1_2'))
        sm.add_widget(tr_l1_3(name='tr_l1_3'))
        sm.add_widget(tr_l1_4(name='tr_l1_4'))
        sm.add_widget(tr_l1_5(name='tr_l1_5'))

        sm.add_widget(tr_l2_1(name='tr_l2_1'))
        sm.add_widget(tr_l2_2(name='tr_l2_2'))
        sm.add_widget(tr_l2_3(name='tr_l2_3'))
        sm.add_widget(tr_l2_4(name='tr_l2_4'))
        sm.add_widget(tr_l2_5(name='tr_l2_5'))

        sm.add_widget(tr_l3_1(name='tr_l3_1'))
        sm.add_widget(tr_l3_2(name='tr_l3_2'))
        sm.add_widget(tr_l3_3(name='tr_l3_3'))
        sm.add_widget(tr_l3_4(name='tr_l3_4'))
        sm.add_widget(tr_l3_5(name='tr_l3_5'))
        
        #sm.add_widget(Settings(name='settings'))
        sm.add_widget(InstrScr(name='test'))
        sm.add_widget(PulseScr(name='pulse1'))
        sm.add_widget(CheckSits(name='sits'))
        sm.add_widget(PulseScr2(name='pulse2'))
        sm.add_widget(Result(name='result'))
        Window.clearcolor = color
        return sm



app = KivyHealth()
app.run()

