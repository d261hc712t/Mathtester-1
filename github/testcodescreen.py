from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.graphics import Color, Ellipse, Line
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.progressbar import ProgressBar
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.dropdown import DropDown
import random
import time
Window.size = (500,700)
Window.size = Window.size
if Window.size[0] != 500 and Window.size[1] !=700:
    Window.size = (500,700)
class Screen3(Screen):
    dem = 0
    level = 0
    tong = 0
    def __init__(self, **kwargs):
        super(Screen3, self).__init__(**kwargs)
        label2 =Label(
            color=(0, 0, 0, 1),
            text = 'MÀN 2',

            outline_color=(1, 1, 1, 1),
            outline_width=5,
            font_size = 50,
            font_name = 'Roboto',
            pos_hint ={'center_x':0.5, 'center_y':0.95}
        )
        self.add_widget(label2)
        self.button = Button(
            text="Xác nhận",
            color=(0, 0, 0, 1),
            font_name='Roboto',
            bold=True,
            font_size=35,
            size_hint=(0.3, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.1},
            background_normal='',
            background_down='',
            background_color=(0, 1, 0.8, 1),
            on_press = self.points
        )
        layout1 = FloatLayout()
        img2 = Image(
            source = 'reverse.png',
            pos_hint = {'center_x':0.1, 'center_y':0.1},
            size_hint = (None, None),
            size = (60,60)
        )
        buttonreverse = Button(
            pos_hint={'center_x': 0.1, 'center_y': 0.1},
            size_hint=(None, None),
            background_normal='',
            background_down='',
        #    background_color=(0, 1, 0.8, 1),
            size=(60, 60),
            on_press= self.reverse1
        )
        dropdown = DropDown()
        dropdown1 = DropDown()
        dem1 = 0
        luu = 'False'

        for i in range(4):
            y = random.randint(0, 3)

            a = random.randint(0, 15)
            if dem1 ==2:
                y=0
            if y>1:
                dem1 +=1
                btn = Button(text='{}'.format(a), size_hint_y=None, height=44)
                btn.bind(on_release=lambda btn: dropdown.select(btn.text))
                btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            elif y<=1 and luu=='False':
                btn = Button(text='{}'.format(a), size_hint_y=None, height=44)
                btn.bind(on_release=lambda btn: dropdown.select(btn.text))
                luu = 'True'
                n = a
                print(n)
            elif y<=1 and luu == 'True':
                btn = Button(text='{}'.format(a), size_hint_y=None, height=44)
                btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
        self.add_widget(
            Label(text="+", color=(0, 0, 0, 1), pos_hint={'center_x': 0.325, 'center_y': 0.65},
                  size_hint=(0.8, 0.2), font_name='Roboto', font_size=80))
        layout6= FloatLayout()
        main_button = Button(
            text="",
            color = (0, 0, 0, 1),
            font_size = 35,
            size_hint=(None, None),
            size = (90, 90),
            background_normal='',
            background_down='',
            pos_hint={'center_x':0.16125, 'center_y':0.65}
        )
        img7 = Image(
            source = 'box.png',
            size_hint = (None, None),
            size =(300,300),
            pos_hint = {'center_x':0.165, 'center_y':0.65}
        )
        layout6.add_widget(main_button)
        layout6.add_widget(img7)
        self.add_widget(layout6)
        main_button.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(main_button, 'text', x))

        luu1 = 'False'

        dem2 = 0
        for i1 in range(4):
            y1 = random.randint(0, 2)
            a1 = random.randint(0, 15)
            if dem2 == 2:
                y1 = 0
            if y1>1:
                dem2+=1
                btn1 = Button(text='{}'.format(a1), size_hint_y=None, height=44)
                btn1.bind(on_release=lambda btn1: dropdown1.select(btn1.text))
            elif y1<=1 and luu1=='False':
                btn1 = Button(text='{}'.format(a1), size_hint_y=None, height=44)
                btn1.bind(on_release=lambda btn1: dropdown1.select(btn1.text))
                luu1 = 'True'
                j = a1
                print(j)
            elif y1<=1 and luu1 == 'True':
                btn1 = Button(text='{}'.format(a1), size_hint_y=None, height=44)
                btn1.bind(on_release=lambda btn1: dropdown1.select(btn1.text))
            dropdown1.add_widget(btn1)
        layout9 = FloatLayout()
        main_button1 = Button(
            text="",
            color = (0, 0, 0, 1),
            font_size = 35,
            size_hint=(None, None),
            background_normal='',
            background_down='',
            size=(90, 90),
            pos_hint={'center_x': 0.4885, 'center_y': 0.65}
        )
        img9 = Image(
            source ='box.png',
            size_hint = (None, None),
            size = (300, 300),
            pos_hint = {'center_x': 0.5, 'center_y': 0.65}
        )
        main_button1.bind(on_release=dropdown1.open)

        dropdown1.bind(on_select=lambda instance, x: setattr(main_button1, 'text', x))
        layout9.add_widget(main_button1)
        layout9.add_widget(img9)
        self.add_widget(layout9)
        dropdown2 = DropDown()
        tong = j + n
        kt = 'False'
        dem3=0
        for i2 in range(4):
            y2 = random.randint(0, 2)
            a2 = random.randint(0, 15)
            if dem3==2:
                y2=0
            if y2 > 1 :
                dem3+=1
                btn2 = Button(text='{}'.format(a2), size_hint_y=None, height=44)
                btn2.bind(on_release=lambda btn2: dropdown2.select(btn2.text))
            elif y2 <= 1 and kt == 'False':
                btn2 = Button(text='{}'.format(tong), size_hint_y=None, height=44)
                btn2.bind(on_release=lambda btn2: dropdown2.select(btn2.text))
                print(tong)
                kt = 'True'
            elif y2 <= 1 and kt == 'True':
                btn2 = Button(text='{}'.format(a2), size_hint_y=None, height=44)
                btn2.bind(on_release=lambda btn2: dropdown2.select(btn2.text))
            dropdown2.add_widget(btn2)
        layout7 =FloatLayout()
        main_button2 = Button(
            text="",
            color = (0, 0, 0, 1),
            font_size = 35,
            size_hint=(None, None),
            background_normal='',
            background_down='',
            size=(90, 90),
            pos_hint={'center_x': 0.835, 'center_y': 0.65}
        )
        img8 = Image(
            source = 'box.png',
            size_hint = (None, None),
            size = (300, 300),
            pos_hint = {'center_x':0.85, 'center_y': 0.65}

        )
        main_button2.bind(on_release=dropdown2.open)

        dropdown2.bind(on_select=lambda instance, x: setattr(main_button2, 'text', x))
        layout7.add_widget(main_button2)
        layout7.add_widget(img8)
        self.add_widget(layout7)
        # print(self.tong)
        label4 = Label(
            text = '=',
            size_hint = (None, None),
            size = ( 50, 50),
            color = (0, 0, 0, 1),
            font_size = 80,
            pos_hint = {'center_x': 0.665, 'center_y':0.65}
        )

        self.add_widget(label4)
    #.a)
        if self.dem == 0:
            img5 = Image(
                source= 'normal.png',
                pos_hint = {'center_x':0.5, 'center_y':0.85},
                size_hint = (None, None),
                size = (400, 200)
            )
        elif self.dem == 1:
            img5 = Image(
                source='level1.png',
                pos_hint={'center_x': 0.5, 'center_y': 0.85},
                size_hint=(None, None),
                size=(400, 200)
            )
        elif self.dem == 2:
            img5 = Image(
                source='level2 (2).png',
                pos_hint={'center_x': 0.5, 'center_y': 0.85},
                size_hint=(None, None),
                size=(400, 200)
            )
        elif self.dem == 3:
            img5 = Image(
                source='level3 (2).png',
                pos_hint={'center_x': 0.5, 'center_y': 0.85},
                size_hint=(None, None),
                size=(400, 200)
            )
        elif self.dem == 4:
            img5 = Image(
                source='level4 (2).png',
                pos_hint={'center_x': 0.5, 'center_y': 0.85},
                size_hint=(None, None),
                size=(400, 200)
            )
        elif self.dem == 5:
            img5 = Image(
                source='level5.png',
                pos_hint={'center_x': 0.5, 'center_y': 0.85},
                size_hint=(None, None),
                size=(400, 200)
            )
        elif self.dem == 6:
            img5 = Image(
                source='level6.png',
                pos_hint={'center_x': 0.5, 'center_y': 0.85},
                size_hint=(None, None),
                size=(400, 200)
            )
        elif self.dem == 7:
            img5 = Image(
                source='level7.png',
                pos_hint={'center_x': 0.5, 'center_y': 0.85},
                size_hint=(None, None),
                size=(400, 200)
            )
        elif self.dem == 8:
            img5 = Image(
                source='level8.png',
                pos_hint={'center_x': 0.5, 'center_y': 0.85},
                size_hint=(None, None),
                size=(400, 200)
            )
        elif self.dem == 9 :
            img5 = Image(
                source='level9.png',
                pos_hint={'center_x': 0.5, 'center_y': 0.85},
                size_hint=(None, None),
                size=(400, 200)
            )
        elif self.dem == 10:
            img5 = Image(
                source='level10.png',
                pos_hint={'center_x': 0.5, 'center_y': 0.85},
                size_hint=(None, None),
                size=(400, 200)
            )


        self.add_widget(img5)
        layout1.add_widget(buttonreverse)
        layout1.add_widget(img2)
        self.add_widget(layout1)
        self.add_widget(self.button)
        if self.dem >= 10:
            self.dem = 0
            self.level = 1
            app = App.get_running_app()
            app.root.current = 'screen1'
        self.selected_item = [None]  # qtrong khi dung dropdown
        self.selected_item1 = [None]
        self.selected_item2 = [None]
        def update_selected_item(instance, x):
            self.selected_item[0] = x

        def update_selected_item1(instance, x):
            self.selected_item1[0] = x

        def update_selected_item2(instance, x):
            self.selected_item2[0] = x
        dropdown.bind(on_select=update_selected_item)
        dropdown1.bind(on_select=update_selected_item1)
        dropdown2.bind(on_select=update_selected_item2)

    def points(self, instance):
        if self.selected_item[0] is not None and self.selected_item1[0] is not None and self.selected_item2[0] is not None:
            if int(self.selected_item[0]) + int(self.selected_item1[0]) == int(self.selected_item2[0]):
                self.dem += 1
                self.clear_widgets()
                self.__init__()

        else:
            print("Please select values for all items")

    # Code bên dưới để gán các phương thức vào dropdowns
    def reverse1(self, instance):
        app = App.get_running_app()
        app.root.current = 'screen1'

            #print("Selected item:", self
kv = Builder.load_string("""
<Screen3>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size  
        Color:
            rgba: 0, 0.7, 0.7, 1
        Rectangle:
            pos: 0, self.height*0.9   # Đặt vị trí của hình chữ nhật bằng với vị trí của Widget chứa nó
            size: self.width, self.height * 0.15
""")
class Test1(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Screen3(name='screen3'))
        return sm
        return kv
Test1().run()