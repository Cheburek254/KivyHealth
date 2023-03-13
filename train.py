#Здесь будут экраны с тренировками
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
from instructions import *
from main_app import *
from runner import *
from kivy.animation import Animation
from kivy.uix.image import Image,AsyncImage
z = 0
class train_main(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        lbl1 = Label(text = '[b]' +tr1 + '[/b]', halign = 'right', markup=True)

        self.btn1 = Button(text ='[u]' +'[b]'+  'Уровень 1'+ '[/u]',markup=True,color=black,background_normal = 'button_vertical.png',font_size = 50)
        self.btn1.on_press = self.next1

        self.btn2 = Button(text ='[u]' + '[b]'+ 'Уровень 2'+ '[/u]',markup=True,color=black,background_normal = 'button_vertical.png',font_size = 50)
        self.btn2.on_press = self.next2

        self.btn3 = Button(text ='[u]' +'[b]'+ '[b]'+ 'Уровень 3'+ '[/u]',markup=True,color=black,background_normal = 'button_vertical.png',font_size = 50)
        self.btn3.on_press = self.next3

        self.btn = Button(text ='[u]'+'[b]' +  'назад'+ '[/u]',size_hint = (0.5,0.5) , pos_hint = {'center_x': 0.5},markup=True,color=black,background_normal = 'button_vertical.png',font_size = 50)
        self.btn.on_press = self.back

        main = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        right = BoxLayout(orientation = 'vertical')
        hor = BoxLayout()
        hor.add_widget(lbl1)
        right.add_widget(self.btn1)
        right.add_widget(self.btn2)
        right.add_widget(self.btn3)
        hor.add_widget(right)
        main.add_widget(hor)
        main.add_widget(self.btn)
        self.add_widget(main)
    def back(self):
        self.manager.current = 'main'
    def next1(self):
        
        self.manager.current = 'tr_l1_1'
    def next2(self):
        
        self.manager.current = 'tr_l2_1'
    def next3(self):
        
        self.manager.current = 'tr_l3_1'




class tr_test(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        lbl1 = Label(text = '[b]' +'Это экран упражнения, здесь будет его описание' + '[/b]', halign = 'right', markup=True)
        lbl2 = Label(text = '[b]' +'Здесь будет таймер' + '[/b]', halign = 'right', markup=True)
        lbl3 = Label(text = '[b]' +'Здесь будет анимация.\n По кнопке завершить вы врнетесь на нач. экран по кнопке запустить таймер/далее\n вы запустите таймер упражнения и по его окончанию вы сможете начать следующее\n но в данный момент вы вернетесь на нач экран' + '[/b]', halign = 'right', markup=True)
        self.btn1 = Button(text ='[u]' +  'Завершить'+ '[/u]', size_hint=(0.5, 0.4), pos_hint = {'center_x': 0.5}, background_color = btn_color, markup=True)
        self.btn1.on_press = self.back
        self.btn2 = Button(text ='[u]' +  'Запустить таймер/далее'+ '[/u]', size_hint=(0.5, 0.4), pos_hint = {'center_x': 0.5}, background_color = btn_color, markup=True)
        self.btn2.on_press = self.next
        main = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        hor = BoxLayout()
        hor.add_widget(self.btn1)
        hor.add_widget(self.btn2)
        main.add_widget(lbl1)
        main.add_widget(lbl2)
        main.add_widget(lbl3)
        main.add_widget(hor)
        self.add_widget(main)
    def back(self):
        self.manager.current = 'train_main'
    def next(self):
        self.manager.current = 'train_main'




class tr_l1_1(Screen):
    def __init__(self,**kwargs):
        
        super().__init__(**kwargs)
        self.next_screen = False
        
        instr = Label(text = '[b]'+'Упражнение 1.'+'[/b]'+ 'Ножницы\nКоличество повторений:'+'[b]'+ '10 подходов х 5 раз'+'[/b]',halign = 'center',font_size = 45,markup = True)
        wimg = Image(source='l1_1.jpg')
        '''self.timer = Seconds(45)#45
        self.timer.bind(done=self.sec_finished)'''
        self.btn = Button(text ='[u]'+'[b]' + 'Далее'+ '[/u]', pos_hint = {'center_x': 0.5}, markup=True,color=black,background_normal = 'button_horizontal.png',font_size = 40)
        self.btn.on_press = self.next
        
        self.btn1 = Button(text ='[u]'+'[b]' +  'Завершить'+ '[/u]',pos_hint = {'center_x': 0.5}, markup=True,color=black,background_normal = 'button_horizontal.png',font_size = 40)
        self.btn1.on_press = self.back
        hor = BoxLayout()
        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        outer.add_widget(instr)
        outer.add_widget(wimg)
        '''outer.add_widget(self.timer)'''
        hor.add_widget(self.btn)
        hor.add_widget(self.btn1)
        outer.add_widget(hor)
        self.add_widget(outer)
    
    '''def sec_finished(self, *args):
        self.next_screen = True
        
        self.btn.set_disabled(False)
        self.btn.text ='[u]' +  'Продолжить'+ '[/u]' '''
    def next(self):
        '''if not self.next_screen:
            self.btn.set_disabled(True)
            self.timer.start()'''
        '''else:'''
        self.manager.current = 'tr_l1_2'
        '''    self.timer.restartnew(45)#45
            self.btn.text ='[u]' +  'Запустить таймер'+ '[/u]'
            self.next_screen = False'''
    def back(self):
        
            self.manager.current = 'train_main'
            




class tr_l1_2(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        
        instr = Label(text = '[b]'+'Упражнение 2.'+'[/b]'+ 'Махи ногами вперёд\nКоличество повторений:'+'[b]'+ '10 раз на каждую ногу'+'[/b]',halign = 'center',font_size = 45,markup = True)
        wimg = Image(source='l1_2.jpg')
        #self.timer = Seconds(45)
        #self.timer.bind(done=self.sec_finished)
        self.btn = Button(text ='[u]'+'[b]' + 'Далее'+ '[/u]',pos_hint = {'center_x': 0.5}, markup=True,color=black,background_normal = 'button_horizontal.png',font_size = 40)
        self.btn.on_press = self.next
        
        self.btn1 = Button(text ='[u]'+'[b]' +  'Завершить'+ '[/u]',pos_hint = {'center_x': 0.5}, markup=True,color=black,background_normal = 'button_horizontal.png',font_size = 40)
        self.btn1.on_press = self.back

        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        outer.add_widget(instr)
        outer.add_widget(wimg)
        #outer.add_widget(self.timer)
        
        hor = BoxLayout()
        hor.add_widget(self.btn)
        hor.add_widget(self.btn1)
        outer.add_widget(hor)
        self.add_widget(outer)
    
    '''def sec_finished(self, *args):
        self.next_screen = True
        
        self.btn.set_disabled(False)
        
        self.btn.text ='[u]' +  'Продолжить'+ '[/u]' '''
    def next(self):
        '''if not self.next_screen:
            self.btn.set_disabled(True)
            self.timer.start()'''
        #else:
        self.manager.current = 'tr_l1_3'

    def back(self):
        
        self.manager.current = 'train_main'




class tr_l1_3(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        
        instr = Label(text = '[b]'+'Упражнение 3.'+'[/b]'+ 'Выпады в сторону\nКолличество повторений:'+'[b]'+ '10 раз на каждую ногу'+'[/b]',halign = 'center',font_size = 45,markup = True)
        wimg = Image(source='l1_3.jpg')
        self.btn = Button(text ='[u]'+'[b]' + 'Далее'+ '[/u]', pos_hint = {'center_x': 0.5}, markup=True,color=black,background_normal = 'button_horizontal.png',font_size = 40)
        self.btn.on_press = self.next
        
        self.btn1 = Button(text ='[u]'+'[b]' +  'Завершить'+ '[/u]',  pos_hint = {'center_x': 0.5}, markup=True,color=black,background_normal = 'button_horizontal.png',font_size = 40)
        self.btn1.on_press = self.back

        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        outer.add_widget(instr)
        outer.add_widget(wimg)
        
        hor = BoxLayout()
        hor.add_widget(self.btn)
        hor.add_widget(self.btn1)
        outer.add_widget(hor)
        self.add_widget(outer)
    
    
    def next(self):
        
        self.manager.current = 'tr_l1_4'
    def back(self):
        
        self.manager.current = 'train_main'
        





class tr_l1_4(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        
        
        instr = Label(text = '[b]'+'Упражнение 4.'+'[/b]'+ 'Подъемы ног\nКоличество повторений:'+'[b]'+ '12 раз'+'[/b]',halign = 'center',font_size = 45,markup = True)
        wimg = Image(source='l1_4.jpg')
        self.btn = Button(text ='[u]'+'[b]' +  'Далее'+ '[/u]', pos_hint = {'center_x': 0.5}, markup=True,color=black,background_normal = 'button_horizontal.png',font_size = 40)
        self.btn.on_press = self.next

        self.btn1 = Button(text ='[u]'+'[b]' +  'Завершить'+ '[/u]', pos_hint = {'center_x': 0.5}, markup=True,color=black,background_normal = 'button_horizontal.png',font_size = 40)
        self.btn1.on_press = self.back

        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        outer.add_widget(instr)
        outer.add_widget(wimg)
        hor = BoxLayout()
        hor.add_widget(self.btn)
        hor.add_widget(self.btn1)
        outer.add_widget(hor)
        self.add_widget(outer)
    
    
    
    def next(self):
        
        self.manager.current = 'tr_l1_5'
    def back(self):
        
        self.manager.current = 'train_main'
            
            

class tr_l1_5(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        
        
        
        instr = Label(text = '[b]'+'Упражнение 5.'+'[/b]'+ 'Велосипед\nКоличество повторений:'+'[b]'+ 'минута'+'[/b]',halign = 'center',font_size = 45,markup = True)
        wimg = Image(source='l1_5.jpg')
        #elif  z == 3:
            #instr = Label(text = 'Вам предстоит сделать 60 отжиманий за 90 секунд')
        self.timer = Seconds(60)#60
        self.timer.bind(done=self.sec_finished)
        
        
        self.btn1 = Button(text ='[u]'+'[b]' +  'Запустить таймер'+ '[/u]', pos_hint = {'center_x': 0.5}, markup=True,color=black,background_normal = 'button_horizontal.png',font_size = 40)
        self.btn1.on_press = self.back

        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        outer.add_widget(instr)
        outer.add_widget(wimg)
        outer.add_widget(self.timer)
        hor = BoxLayout()
        hor.add_widget(self.btn1)
        #hor.add_widget(self.btn1)
        outer.add_widget(hor)
        self.add_widget(outer)
    
    def sec_finished(self, *args):
        self.next_screen = True
        self.btn1.set_disabled(False)
        
        self.btn1.text ='[u]'+'[b]' +  'Завершить'+ '[/u]'
    
    def back(self):
        if not self.next_screen:
            self.btn1.set_disabled(True)
            self.timer.start()
        else:
            self.manager.current = 'train_main'
            self.timer.restartnew(60)#60
            self.btn1.text ='[u]'+'[b]' +  'Запустить таймер'+ '[/u]'
            self.next_screen = False









class tr_l2_1(Screen):
    def __init__(self,**kwargs):
        
        super().__init__(**kwargs)
        
        
        
        instr = Label(text = '[b]'+'Упражнение 1.'+'[/b]'+ 'Приседания\nКоличество повторений:'+'[b]'+ '20 раз'+'[/b]',halign = 'center',font_size = 45,markup = True)
        wimg = Image(source='l2_1.jpg')
        self.btn = Button(text ='[u]'+'[b]' + 'Далее'+ '[/u]', pos_hint = {'center_x': 0.5}, markup=True,color=black,background_normal = 'button_horizontal.png',font_size = 40)
        self.btn.on_press = self.next
        
        self.btn1 = Button(text ='[u]'+'[b]' +  'Завершить'+ '[/u]', pos_hint = {'center_x': 0.5}, markup=True,color=black,background_normal = 'button_horizontal.png',font_size = 40)
        self.btn1.on_press = self.back

        hor = BoxLayout()
        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        outer.add_widget(instr)
        outer.add_widget(wimg)
        hor.add_widget(self.btn)
        hor.add_widget(self.btn1)
        outer.add_widget(hor)
        self.add_widget(outer)
    
    
    def next(self):
        
        self.manager.current = 'tr_l2_2'
    def back(self):
        
        self.manager.current = 'train_main'
        
            




class tr_l2_2(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        
        
        instr = Label(text = '[b]'+'Упражнение 2.'+'[/b]'+ 'Наклоны туловища\nКоличество повторений:'+'[b]'+ '20 раз'+'[/b]',halign = 'center',font_size = 45,markup = True)
        wimg = Image(source='l2_2.jpg')
        self.btn = Button(text ='[u]'+'[b]' + 'Далее'+ '[/u]', pos_hint = {'center_x': 0.5}, markup=True,color=black,background_normal = 'button_horizontal.png',font_size = 40)
        self.btn.on_press = self.next
        
        self.btn1 = Button(text ='[u]'+'[b]' +  'Завершить'+ '[/u]',pos_hint = {'center_x': 0.5}, markup=True,color=black,background_normal = 'button_horizontal.png',font_size = 40)
        self.btn1.on_press = self.back

        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        outer.add_widget(instr)
        outer.add_widget(wimg)
        
        hor = BoxLayout()
        hor.add_widget(self.btn)
        hor.add_widget(self.btn1)
        outer.add_widget(hor)
        self.add_widget(outer)
    
    
    def next(self):
        
        self.manager.current = 'tr_l2_3'
    def back(self):
        
        self.manager.current = 'train_main'
        
            




class tr_l2_3(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        
        
        instr = Label(text = '[b]'+'Упражнение 3.'+'[/b]'+ 'Перебирание руками\nКоличество повторений:'+'[b]'+ '3 подхода х 10 раз'+'[/b]',halign = 'center',font_size = 45,markup = True)
        wimg = Image(source='l2_3.jpg')
        self.btn = Button(text ='[u]'+'[b]' + 'Далее'+ '[/u]',pos_hint = {'center_x': 0.5}, markup=True,color=black,background_normal = 'button_horizontal.png',font_size = 40)
        self.btn.on_press = self.next
        
        self.btn1 = Button(text ='[u]'+'[b]' +  'Завершить'+ '[/u]',pos_hint = {'center_x': 0.5}, markup=True,color=black,background_normal = 'button_horizontal.png',font_size = 40)
        self.btn1.on_press = self.back

        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        outer.add_widget(instr)
        outer.add_widget(wimg)
        hor = BoxLayout()
        hor.add_widget(self.btn)
        hor.add_widget(self.btn1)
        outer.add_widget(hor)
        self.add_widget(outer)
    
    
    def next(self):
        
        self.manager.current = 'tr_l2_4'
    def back(self):
        
        self.manager.current = 'train_main'
        
        





class tr_l2_4(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        
        instr = Label(text = '[b]'+'Упражнение 4.'+'[/b]'+ 'Шаг-выпад вперёд\nКолличество повторений:'+'[b]'+ '3 подхода х 20 раз'+'[/b]',halign = 'center',font_size = 45,markup = True)
        wimg = Image(source='2v.jpg')
        self.btn = Button(text ='[u]'+'[b]' + 'Далее'+ '[/u]',pos_hint = {'center_x': 0.5}, markup=True,color=black,background_normal = 'button_horizontal.png',font_size = 40)
        self.btn.on_press = self.next

        self.btn1 = Button(text ='[u]'+'[b]' +  'Завершить'+ '[/u]',pos_hint = {'center_x': 0.5}, markup=True,color=black,background_normal = 'button_horizontal.png',font_size = 40)
        self.btn1.on_press = self.back

        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        outer.add_widget(instr)
        outer.add_widget(wimg)
        hor = BoxLayout()
        hor.add_widget(self.btn)
        hor.add_widget(self.btn1)
        outer.add_widget(hor)
        self.add_widget(outer)
    
    def next(self):
        
            self.manager.current = 'tr_l2_5'
    def back(self):
        
        self.manager.current = 'train_main'
        
        


class tr_l2_5(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        
        
        
        instr = Label(text = '[b]'+'Упражнение 5.'+'[/b]'+ 'Махи ногами\nКоличество повторений:'+'[b]'+ '3 подхода х 15 раз\n на каждую ногу'+'[/b]',halign = 'center',font_size = 45,markup = True)
        wimg = Image(source='l2_6.jpg')
        self.btn1 = Button(text ='[u]'+'[b]' + 'Завершить'+ '[/u]',pos_hint = {'center_x': 0.5}, markup=True,color=black,background_normal = 'button_horizontal.png',font_size = 40)
        self.btn1.on_press = self.back

        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        outer.add_widget(instr)
        outer.add_widget(wimg)
        hor = BoxLayout()
        hor.add_widget(self.btn1)
        #hor.add_widget(self.btn1)
        outer.add_widget(hor)
        self.add_widget(outer)
    
    
    
    def back(self):
        
        self.manager.current = 'train_main'
    
        










class tr_l3_1(Screen):
    def __init__(self,**kwargs):
        
        super().__init__(**kwargs)
        self.next_screen = False
        
        
        
        instr = Label(text = '[b]'+'Упражнение 1.'+'[/b]'+ 'Джамплинг джек\nКоличество повторений:'+'[b]'+ '3 подхода х 15 раз'+'[/b]',halign = 'center',font_size = 45,markup = True)
        wimg = Image(source='l3_1.jpg')
        self.btn = Button(text ='[u]'+'[b]' + 'Далее'+ '[/u]', pos_hint = {'center_x': 0.5}, markup=True,color=black,background_normal = 'button_horizontal.png',font_size = 40)
        self.btn.on_press = self.next
        
        self.btn1 = Button(text ='[u]'+'[b]' +  'Завершить'+ '[/u]',pos_hint = {'center_x': 0.5}, markup=True,color=black,background_normal = 'button_horizontal.png',font_size = 40)
        self.btn1.on_press = self.back
        
        hor = BoxLayout()
        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        outer.add_widget(instr)
        outer.add_widget(wimg)
        hor.add_widget(self.btn)
        hor.add_widget(self.btn1)
        outer.add_widget(hor)
        self.add_widget(outer)
    
    
    def next(self):
        
        self.manager.current = 'tr_l3_2'
    def back(self):
        
        self.manager.current = 'train_main'
            




class tr_l3_2(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        
        
        
        instr = Label(text = '[b]'+'Упражнение 2.'+'[/b]'+ 'Разношка на возвышенности\nКоличество повторений:'+'[b]'+ '3 подхода х 50 раз'+'[/b]',halign = 'center',font_size = 45,markup = True)
        wimg = Image(source='l3_2.jpg')
        self.btn = Button(text ='[u]'+'[b]' + 'Далее'+ '[/u]', pos_hint = {'center_x': 0.5}, markup=True,color=black,background_normal = 'button_horizontal.png',font_size = 40)
        self.btn.on_press = self.next
        
        self.btn1 = Button(text ='[u]'+'[b]' +  'Завершить'+ '[/u]', pos_hint = {'center_x': 0.5}, markup=True,color=black,background_normal = 'button_horizontal.png',font_size = 40)
        self.btn1.on_press = self.back

        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        outer.add_widget(instr)
        outer.add_widget(wimg)
        
        hor = BoxLayout()
        hor.add_widget(self.btn)
        hor.add_widget(self.btn1)
        outer.add_widget(hor)
        self.add_widget(outer)
    
    
    def next(self):
        
        self.manager.current = 'tr_l3_3'
    def back(self):
        
        self.manager.current = 'train_main'
            




class tr_l3_3(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        
        
        
        instr = Label(text = '[b]'+'Упражнение 3.'+'[/b]'+ 'Скалолаз\nКолличество повторений:'+'[b]'+ '30 раз х 3 подхода'+'[/b]',halign = 'center',font_size = 45,markup = True)
        wimg = Image(source='skalolaz.jpg')
        self.btn = Button(text ='[u]'+'[b]' + 'Далее'+ '[/u]',  pos_hint = {'center_x': 0.5}, markup=True,color=black,background_normal = 'button_horizontal.png',font_size = 40)
        self.btn.on_press = self.next
        
        self.btn1 = Button(text ='[u]'+'[b]' +  'Завершить'+ '[/u]',  pos_hint = {'center_x': 0.5}, markup=True,color=black,background_normal = 'button_horizontal.png',font_size = 40)
        self.btn1.on_press = self.back

        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        outer.add_widget(instr)
        outer.add_widget(wimg)
        
        hor = BoxLayout()
        hor.add_widget(self.btn)
        hor.add_widget(self.btn1)
        outer.add_widget(hor)
        self.add_widget(outer)
    
    
    def next(self):
        
        self.manager.current = 'tr_l3_4'
    def back(self):
        
        self.manager.current = 'train_main'
            





class tr_l3_4(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        
        
        
        
        instr = Label(text = '[b]'+'Упражнение 4.'+'[/b]'+ 'Выпрыгивания\nКоличество повторений:'+'[b]'+ '3 подхода х 15 раз'+'[/b]',halign = 'center',font_size = 45,markup = True)
        wimg = Image(source='l3_4.jpg')
        self.btn = Button(text ='[u]'+'[b]' +  'Далее'+ '[/u]', pos_hint = {'center_x': 0.5}, markup=True,color=black,background_normal = 'button_horizontal.png',font_size = 40)
        self.btn.on_press = self.next

        self.btn1 = Button(text ='[u]'+'[b]' +  'Завершить'+ '[/u]', pos_hint = {'center_x': 0.5}, markup=True,color=black,background_normal = 'button_horizontal.png',font_size = 40)
        self.btn1.on_press = self.back

        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        outer.add_widget(instr)
        outer.add_widget(wimg)
        hor = BoxLayout()
        hor.add_widget(self.btn)
        hor.add_widget(self.btn1)
        outer.add_widget(hor)
        self.add_widget(outer)
    
    
    
    def next(self):
        
        self.manager.current = 'tr_l3_5'
    def back(self):
        
        self.manager.current = 'train_main'
        



class tr_l3_5(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        
        
        
        
        instr = Label(text = '[b]'+'Упражнение 5.'+'[/b]'+ 'Берпи\nКоличество повторений:'+'[b]'+ '2 минуты'+'[/b]',halign = 'center',font_size = 45,markup = True)
        self.timer = Seconds(120)#90
        self.timer.bind(done=self.sec_finished)
        wimg = Image(source='l3_5.jpg')
        
        self.btn1 = Button(text ='[u]'+'[b]' +  'Запустить таймер'+ '[/u]',  pos_hint = {'center_x': 0.5}, markup=True,color=black,background_normal = 'button_horizontal.png',font_size = 40)
        self.btn1.on_press = self.back

        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        outer.add_widget(instr)
        outer.add_widget(wimg)
        outer.add_widget(self.timer)
        hor = BoxLayout()
        hor.add_widget(self.btn1)
        outer.add_widget(hor)
        self.add_widget(outer)
    
    def sec_finished(self, *args):
        self.next_screen = True
        self.btn1.set_disabled(False)
        
        self.btn1.text ='[u]'+'[b]' +  'Завершить'+ '[/u]'
    
    def back(self):
        if not self.next_screen:
            self.btn1.set_disabled(True)
            self.timer.start()
        else:
            self.manager.current = 'train_main'
            self.timer.restartnew(120)#90
            self.btn1.text ='[u]'+'[b]' +  'Запустить таймер'+ '[/u]'
            self.next_screen = False