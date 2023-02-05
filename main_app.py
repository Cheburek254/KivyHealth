# напиши здесь свое приложение
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
from runner import *
from kivy.animation import Animation
from kivy.uix.image import Image,AsyncImage
age = 7
name = 'Имя'
p1 =0 
p2 = 0
p3 =  0
color = (0.43, 0.4, 0.84, 1)
btn_color = (0.18, 0.07, 0.83, 1)

class MyTextInput(TextInput):
    def __init__(self,**args):
        super().__init__()
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.text = ""
            return True
        return super(MyTextInput, self).on_touch_down(touch)
'''
class MainTest(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
        self.btn_to_test = Button(text ='[u]' +  'Перейти к тесту'+ '[/u]', pos_hint = {'center_x': 0.5}, background_color = btn_color, markup=True)
        self.btn_to_test.on_press = self.to_test
        self.btn_to_unstr = Button(text ='[u]' +  'Инструкция'+ '[/u]', pos_hint = {'center_x': 0.5}, background_color = btn_color, markup=True)
        self.btn_to_instr.on_press = self.to_instr

        self.btn_back = Button(text ='[u]' +  'назад'+ '[/u]',  pos_hint = {'center_x': 0.5}, background_color = btn_color, markup=True)
        self.btn_back.on_press = self.back

        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 5,size_hint=(1,0.8))
        outer.add_widget(self.btn_to_test)
        
        outer.add_widget(self.)


    def back(self):
        self.manager.current = 'main'
    def to_instr(self):
        self.manager.current = 'instr'
    def to_test(self):
        self.manager.current = 'test'

class InstrScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        instr = Label(text = txt_instruction,font_size = 35)
        self.btn2 = Button(text ='[u]' +  'назад'+ '[/u]', size_hint=(0.3, 0.4), pos_hint = {'center_x': 0.5}, background_color = btn_color, markup=True)
        
        self.btn2.on_press = self.back
        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 5,size_hint=(1,0.8))
        outer.add_widget(instr)
        outer.add_widget(self.btn2)
        self.add_widget(outer)
    def back(self):
        self.manager.current = 'test_main'
'''
class InstrScr(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        instr = Label(text = 'Диагностика вашего работоспособности сердца\nпо пробе Руфье',font_size = 30)
        instr2 = Label(text = '''1. Измерьте частоту пульса за 15 с
2. Выполните приседания за 45 с
3. Измерьте частоту пульса за 15 с
4. Отдых 30 с
5. Измерьте частоту пульса за 15 с''',font_size = 30)
        wimg = Image(source='test.jpg')
        lbl1 = Label(text = '[b]' +'Введите имя' + '[/b]', halign = 'right', markup=True)
        self.in_name = TextInput(text = '',multiline =False)
        lbl2 = Label(text = '[b]' +'Введите возраст'+'[/b]', halign = 'right', markup=True)
        self.in_age = TextInput(text = '', multiline=False)
        self.btn = Button(text ='[u]' +  'начать'+ '[/u]', size_hint=(0.3, 0.4), pos_hint = {'center_x': 0.5}, background_color = btn_color, markup=True)
        l1 = BoxLayout()
        self.btn.on_press = self.next
        self.btn2 = Button(text ='[u]' +  'назад'+ '[/u]', size_hint=(0.3, 0.4), pos_hint = {'center_x': 0.5}, background_color = btn_color, markup=True)
        
        self.btn2.on_press = self.back
        line1 = BoxLayout(size_hint=(0.8,None), height='30sp')#size_hint=(0.8,None), height='30sp'
        line2 = BoxLayout(size_hint=(0.8,None), height='30sp')#size_hint=(0.8,None), height='30sp'
        line3 = BoxLayout()
        
        line1.add_widget(lbl1)
        line1.add_widget(self.in_name)
        line2.add_widget(lbl2)
        line2.add_widget(self.in_age)
        line3.add_widget(self.btn2)
        line3.add_widget(self.btn)
        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 5,size_hint=(1,0.8))#,size_hint=(1,0.8)
        outer.add_widget(instr)
        outer.add_widget(instr2)
        outer.add_widget(wimg)
        outer.add_widget(l1)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(line3)
        
        self.add_widget(outer)
    def next(self):
        global age
        global name
        
        try:
                
            age = int(self.in_age.text)
            name = self.in_name.text
            self.manager.current = 'pulse1'
            if age<7:
                age = 7
            
            
        except:
            self.age.text = '' 
    def back(self):
        self.manager.current = 'main'
                



class PulseScr(Screen):
    def __init__(self,**kwargs):
        self.next_screen = False
        super().__init__(**kwargs)
        instr = Label(text = txt_test1)
        lbl_result = Label(text ='[b]' + 'Введите результат'+'[/b]', halign='right', markup=True)
        self.timer = Seconds(15,font_size = 45,markup = True)
        
        self.timer.bind(done=self.sec_finished)
        wimg = Image(source='timer.jpg')
        
        self.pulse1 = TextInput(multiline =False, size_hint=(0.2, 0.5), pos_hint = {'center_x': 0.5})
        self.pulse1.set_disabled(True)
        self.btn = Button(text ='[u]' +  'Начать таймер'+ '[/u]', size_hint=(0.3, 0.2), pos_hint = {'center_x': 0.5},background_color = btn_color, markup=True)
        self.btn.on_press = self.next
        
        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        outer.add_widget(instr)
        outer.add_widget(wimg)
        outer.add_widget(self.timer)
        outer.add_widget(lbl_result)
        outer.add_widget(self.pulse1)
        outer.add_widget(self.btn)
        self.add_widget(outer)


    def sec_finished(self, *args):
        self.next_screen = True
        self.pulse1.set_disabled(False)
        self.btn.set_disabled(False)
        self.btn.text ='[u]' +  'Продолжить'+ '[/u]'
    def next(self):
        global p1
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.timer.start()
        else:
            try:
                p1 = int(self.pulse1.text)
                self.manager.current = 'sits'
                self.timer.restartnew(15)
                self.btn.text ='[u]' +  'Начать таймер'+ '[/u]'
                self.pulse1.text = ''
                self.next_screen = False
                self.pulse1.set_disabled(False)
                self.btn.set_disabled(False)
            except:
                self.pulse1.text = ''    

class CheckSits(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.finished = False
        self.next_screen = False
        instr = Label(text = txt_sits)
        self.timer = Seconds(45)
        self.timer.bind(done=self.sec_finished)
        self.btn = Button(text ='[u]' + 'Запустить таймер'+ '[/u]', size_hint=(0.3, 0.2), pos_hint = {'center_x': 0.5},background_color = btn_color, markup=True)
        self.btn.on_press = self.next
        
        h = BoxLayout()
        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        outer.add_widget(instr)
        
        
        outer.add_widget(self.timer)
        outer.add_widget(self.btn)
        #h.add_widget(self.run)
        #h.add_widget(outer)
        self.add_widget(outer)
    
    def sec_finished(self, *args):
        self.next_screen = True
        
        self.btn.set_disabled(False)
        self.btn.text ='[u]' +  'Продолжить'+ '[/u]'
    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.timer.start()
            #self.run.start(self.run)
        else:
            self.manager.current = 'pulse2'
            self.timer.restartnew(45)
            self.btn.text ='[u]' +  'Запустить таймер'+ '[/u]'
            self.next_screen = False

class PulseScr2(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        instr = Label(text = txt_test3)
        self.stage = 0
        self.next_screen = False
        self.lbl1 = Label(text = 'Измерьте пульс')
        lbl_result2 = Label(text ='[b]' + 'Введите результат'+'[/b]', halign='right', markup=True)
        lbl_result3 = Label(text = '[b]' +'Введите результат после отдыха'+'[/b]', halign='right', markup=True)
        self.pulse1 = TextInput(multiline =False,  pos_hint = {'center_x': 0.5})
        self.pulse2 = TextInput(multiline =False, pos_hint = {'center_x': 0.5})
        self.btn = Button(text ='[u]' + 'Запустить таймер'+ '[/u]', size_hint=(0.3, 0.2), pos_hint = {'center_x': 0.5},background_color = btn_color, markup=True)
        self.btn.on_press = self.next
        self.timer = Seconds(15)
        
        self.timer.bind(done=self.sec_finished)
        
        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        outer.add_widget(instr)
        outer.add_widget(self.lbl1)
        outer.add_widget(self.timer)
        line1 = BoxLayout(size_hint=(0.8,None), height='30sp')
        line2 = BoxLayout(size_hint=(0.8,None), height='30sp')
        line1.add_widget(lbl_result2)
        line2.add_widget(lbl_result3)
        line1.add_widget(self.pulse1)
        line2.add_widget(self.pulse2)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)


    def sec_finished(self, *args):
   	  if self.timer.done:
	      if self.stage == 0:
	          # закончили первый подсчет, отдыхаем
	          self.stage = 1
	          self.lbl1.text = 'Отдыхайте'
	          self.timer.restart(30)
	          self.pulse1.set_disabled(False)
	      elif self.stage == 1:
	          # закончили отдых, считаем
	          self.stage = 2
	          self.lbl1.text='Считайте пульс'
	          self.timer.restart(15)
	      elif self.stage == 2:
	          self.pulse2.set_disabled(False)
	          self.btn.set_disabled(False)
	          self.btn.text ='[u]' +  'Завершить'+ '[/u]'
	          self.next_screen = True


    def next(self):
        global p2
        global p3
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.timer.start()
        else:
            try:
                p2 = int(self.pulse1.text)
                p3 = int(self.pulse2.text)
                self.manager.current = 'result'
                self.timer.restartnew(15)
                self.btn.text ='[u]' +  'Начать таймер'+ '[/u]'
                self.stage = 0
                self.pulse1.text = ''
                self.pulse2.text = '' 
                self.next_screen = False
            except:
                self.pulse1.text = ''
                self.pulse2.text = ''   

class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        
        self.btn = Button(text ='[u]' +'начать заново'+ '[/u]', size_hint=(0.3, 0.2), pos_hint = {'center_x': 0.5}, background_color = btn_color, markup=True)
        self.btn.on_press = self.next
        self.instr = Label(text = '')
        self.outer.add_widget(self.instr)
        self.add_widget(self.outer)
        self.add_widget(self.btn)
        self.on_enter = self.before
    def before(self):
        global name
        self.instr.text = name + '\n' + test(p1,p2,p3,age)
    def next(self):
        global age
        global name
        global p1
        global p2
        global p3
        age = 7
        name = 'Имя'
        p1 =0 
        p2 = 0
        p3 =0 
        self.manager.current = 'test'


class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name='instr'))
        sm.add_widget(PulseScr(name='pulse1'))
        sm.add_widget(CheckSits(name='sits'))
        sm.add_widget(PulseScr2(name='pulse2'))
        sm.add_widget(Result(name='result'))
        Window.clearcolor = color
        return sm

#app = HeartCheck()
#app.run()


