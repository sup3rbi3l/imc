from kivy.lang import Builder

from kivymd.app import MDApp

from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from kivy.config import Config
from kivy.app import App
from kivy import platform
from kivymd.uix.filemanager import MDFileManager 
from kivymd.uix.selectioncontrol import MDCheckbox
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from datetime import date
from kivy.uix.screenmanager import ScreenManager, Screen


screen = '''

ScreenManager:
    TelaInicio:
    TelaIMC:
    
<TelaInicio>:
    id:home 
    name:'home'
    
    MDToolbar:
        title: "Sistema de controle de IMC"
        pos_hint: {"top" : 1}
        
    MDTextField:
        id: nome
        size_hint_x:(0.3)
        pos_hint : {"center_x":0.5,"center_y":0.8}
    
    MDLabel:
        text:'Nome:'
        pos_hint : {"center_x":0.70,"center_y":0.8}
        
    MDTextField:
        id: peso
        size_hint_x:(0.3)
        pos_hint : {"center_x":0.5,"center_y":0.6}
        
    MDLabel:
        text:'Peso(Kg):'
        pos_hint : {"center_x":0.70,"center_y":0.6,}
        
    MDTextField:
        id: altura
        size_hint_x:(0.3)
        pos_hint : {"center_x":0.5,"center_y":0.4}
    
    MDLabel:
        text:'Altura(M):'
        pos_hint : {"center_x":0.70,"center_y":0.39,}
        
    MDCheckbox:
        group:'1'
        size_hint: None, None
        size: "48dp", "48dp"
        pos_hint: {'center_x': .9, 'center_y': .15}
        on_active: app.printa()
        
    MDCheckbox:
        group:'1'
        size_hint: None, None
        size: "48dp", "48dp"
        pos_hint: {'center_x': .9, 'center_y': .25}
        on_active: app.printa()
        
    MDLabel:
        text:'XX'
        font_style:'H4'
        pos_hint: {'center_x': 1.12, 'center_y': .25}
        
    MDLabel:
        text:'XY'
        font_style:'H4'
        pos_hint: {'center_x': 1.12, 'center_y': .15}
        
    MDFillRoundFlatIconButton:
        text:'calcular'
        font_size:25
        pos_hint: {"center_x":0.35,"center_y":0.2,}
        size_hint:(0.3,0.15)
        on_press: app.printa_info()
        on_press: root.manager.current = 'imc'
        
        
        
<TelaIMC>:

    name:'imc'
    MDToolbar:
        title: "Resultado"
        pos_hint: {"top" : 1}

    MDLabel:
        id: nome
        text:''
        font_style:'H6'
        pos_hint: {"center_x":0.7,"center_y":0.8,}
        
    MDLabel:
        id: imc
        text:''
        font_style:'H6'
        pos_hint: {"center_x":0.7,"center_y":0.7,}
        
    MDLabel:
        id: data
        text:''
        font_style:'H6'
        pos_hint: {"center_x":0.7,"center_y":0.6,}
        
    MDLabel:
        id: resultado
        text:''
        font_style:'H6'
        pos_hint: {"center_x":0.7,"center_y":0.4,}
        
    MDFillRoundFlatIconButton:
        text:'voltar'
        font_size:25
        pos_hint: {"center_x":0.5,"center_y":0.2,}
        size_hint:(0.3,0.15)
        on_press: root.manager.current = 'home'
        
        
        
'''








class TelaInicio(Screen):
    pass


class TelaIMC(Screen):
    pass




# Create the screen manager
sm = ScreenManager()
sm.add_widget(TelaInicio(name='home'))
sm.add_widget(TelaIMC(name='imc'))


class calcula_imc(MDApp):

    def build(self):
        self.screen=Builder.load_string(screen)
        
        
    
        
        return self.screen
    
    
    def printa(self):
        print('a')
        
    def printa_info(self):
        
        
        nome = self.root.get_screen('home').ids.nome.text 
        peso = int (self.root.get_screen('home').ids.peso.text) 
        altura = float(self.root.get_screen('home').ids.altura.text )
        self.imc = peso/altura**2
        self.imc = round(self.imc)
        data = date.today()
        
        self.root.get_screen('imc').ids.nome.text = f'Nome:{nome}'
        self.root.get_screen('imc').ids.imc.text = f'IMC:{self.imc}'
        self.root.get_screen('imc').ids.data.text = f'Data:{data}'
        
        if self.imc < 18.5:
            resultado = "Você está com magresa"
        elif self.imc < 25:
            resultado = "Você está com peso normal"
        elif self.imc < 30:
            resultado = "Você está com sobrepeso"
        elif self.imc < 40:
            resultado = "Você está com obesidade"
        else:
            resultado = "Você está com osbesidade grave"
        self.root.get_screen('imc').ids.resultado.text = f'Resultado:{resultado}'





        
        
calcula_imc().run()