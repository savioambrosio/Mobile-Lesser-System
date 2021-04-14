from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.animation import Animation
from kivymd.uix.dialog import MDDialog
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.tab import MDTabsBase
from kivy.uix.screenmanager import Screen,ScreenManager
import requests
from kivymd.toast import toast
import json
from random import randint
from kivy.uix.anchorlayout import AnchorLayout
import tkinter
from kivy.uix.boxlayout import BoxLayout
from tkinter import *
from firebase import firebase
import firebase_admin
from kivy.clock import mainthread
import threading
from kivymd.uix.button import MDFlatButton
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
import smtplib
import re
from kivy.properties import ObjectProperty

#945 512 220
#amzf418!
Window.size = (285,500)

janela = """
ScreenManager:
    LoginScreen:
    EmpreScreen:
    
<Content>:
    name: "ola"
    size_hint_y: None
    height: "230dp"
    orientation: "vertical"
    
    FloatLayout:
    
        MDLabel:
            text: "RESPONDER"
            user_font_size: "18dp"
            theme_text_color: "Custom"
            text_color: [135/255,135/255,135/255,2] 
            bold:True
            pos_hint: {"center_x":.78, "center_y":.99}
            
        MDIconButton:
            icon: "close-circle"
            user_font_size: "25dp"
            theme_text_color:"Custom"
            text_color: [135/255,135/255,135/255,2] 
            pos_hint: {"center_x":.10, "center_y":.99}
            on_release: app.closs()
            
        MDIconButton:
            icon: "email-edit"
            user_font_size: "33dp"
            theme_text_color:"Custom"
            text_color: [135/255,135/255,135/255,2] 
            pos_hint: {"center_x":0.5, "center_y":.85}   
            
        MDTextField:
            id: cli
            hint_text: "Email do cliente..."
            size_hint_x:.98
            font_size: 15
            icon_right: "email"
            icon_right_color:[169/255,169/255,169/255,2] 
            hint_text_color: 1,0,0,1
            cursor_color: 0,0,0,1
            pos_hint: {"center_x":0.5, "center_y":.59}

        MDFillRoundFlatIconButton:
            text: "Recusar Pedido"
            icon: "close"
            pos_hint: {"center_x":0.5, "center_y":.12}
            on_release: app.resp2()
                   
        MDFillRoundFlatIconButton:
            text: "Aceitar Pedido"
            icon: "check"
            pos_hint: {"center_x":0.5, "center_y":.32}
            on_release: app.resp1()
            
<TooltipMDIconButton@MDIconButton+MDTooltip>

<LoginScreen>:
    name : "login"

    Content:
    
    BoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "Rent Car"
            left_action_items: [["close",lambda x: app.stop()]]
            height: 36

        MDTabs:
            id: log
            md_bg_color:[30/255,144/255,255/255,1]
            Tab:
                text: "Login"
                MDCard:
                    id: card37
                    size_hint_y:0.20
                    radius:[25,25,0,0]
                    md_bg_color: 1,1,1,1
                    pos_hint:{"center_x":0.5,"center_y":.44}
                    spacing:'16dp'
                    padding:'17dp'

                MDIconButton:
                    icon:"shield-account"
                    user_font_size: "38sp"
                    theme_text_color:"Custom"
                    text_color: [135/255,135/255,135/255,2] 
                    pos_hint: {"center_x":0.5, "center_y":.77}
                    
                MDLabel:
                    text: "LOGIN"
                    user_font_size: "10dp"
                    theme_text_color: "Custom"
                    text_color: [135/255,135/255,135/255,2] 
                    bold:True
                    halign:"center"
                    pos_hint: {"center_x":0.5, "center_y":.69}                    
                
                MDTextFieldRound:
                    id:emai
                    hint_text: "Insira o seu email..."
                    icon_right: "email"
                    icon_right_color:1,1,1,1
                    foreground_color: 1,1,1,1
                    hint_text_color: 1,1,1,1
                    cursor_color: 0,0,0,1
                    font_size:16
                    focus: True
                    size_hint_x:.75
                    pos_hint: {"center_x":0.5, "center_y":.55}

                MDTextFieldRound:
                    id:sen
                    hint_text: "Senha..."
                    multiline: False
                    size_hint_x:.75
                    foreground_color: 1,1,1,1
                    hint_text_color:1,1,1,1
                    font_size: 16
                    focus: True
                    cursor_color:0,0,0,1
                    pos_hint: {"center_x":0.5, "center_y":.43}
                    password: True
                    
                MDIconButton:
                    id: lok
                    icon: "eye-off"
                    user_font_size: "26dp"
                    pos_hint: {"center_x":.83, "center_y":.43}
                    on_press: app.togglevisibility() 
                    
                MDFloatingActionButton:
                    id: acessar
                    icon: "arrow-right-circle"
                    elevation_normal:12
                    md_bg_color: app.theme_cls.primary_color   
                    theme_text_color: "Custom"
                    text_color: 1,1,1,1                                
                    pos_hint: {"center_x":0.5, "center_y":.20}
                    on_release:
                        app.login()
                        root.manager.transition.direction = 'down'
                    
            Tab:
                text:"Cadastrar-se"
                
                MDCard:
                    size_hint_y:0.90
                    radius:[28,28,0,0]
                    pos_hint: {"center_x":0.5, "center_y":.43}

                MDIconButton:
                    icon: "account-circle"
                    user_font_size: "34sp"
                    theme_text_color: "Custom"
                    text_color: [135/255,135/255,135/255,2] 
                    pos_hint: {"center_x":0.5, "center_y":.80}

                MDLabel:
                    text: "FUNCIONÁRIO"
                    user_font_size: "10dp"
                    theme_text_color: "Custom"
                    text_color: [169/255,169/255,169/255,2] 
                    bold:True
                    halign:"center"
                    pos_hint: {"center_x":0.5, "center_y":.73}

                MDTextFieldRound:
                    id: nom
                    hint_text:"Insira o seu nome..."
                    font_size:15
                    icon_right:"account"
                    foreground_color:1,1,1,1
                    text_color:1,1,1,1
                    size_hint_x:.75
                    cursor_color:0,0,0,1
                    pos_hint: {"center_x":0.5, "center_y":.62}

                MDTextFieldRound:
                    id: ema
                    hint_text:"Insira o seu email..."
                    font_size:15
                    icon_right:"email"
                    foreground_color:1,1,1,1
                    text_color:1,1,1,1
                    size_hint_x:.75
                    cursor_color:0,0,0,1
                    pos_hint: {"center_x":0.5, "center_y":.52}

                MDTextFieldRound:
                    id: seusuario
                    hint_text:"Insira a sua senha..."
                    font_size:15
                    foreground_color:1,1,1,1
                    text_color:1,1,1,1
                    size_hint_x:.75
                    password:True
                    cursor_color:0,0,0,1
                    pos_hint: {"center_x":0.5, "center_y":.41}
                    
                MDIconButton:
                    id: loko
                    icon: "eye-off"
                    user_font_size: "26dp"
                    pos_hint: {"center_x":.83, "center_y":.41}
                    on_release: app.togglevisibility()
                    
                MDTextFieldRound:
                    id: sempresa
                    hint_text:"senha da empresa..."
                    font_size:15
                    foreground_color:1,1,1,1
                    text_color:1,1,1,1
                    size_hint_x:.75
                    password: True
                    cursor_color:0,0,0,1
                    pos_hint: {"center_x":0.5, "center_y":.30}
                    
                MDIconButton:
                    id: loki
                    icon: "eye-off"
                    user_font_size: "26dp"
                    pos_hint: {"center_x":.83, "center_y":.30}
                    on_release: app.plo()
                    
                MDFillRoundFlatIconButton:
                    id:grav
                    icon:"content-save-move" 
                    text:"Guardar Dados"                         
                    pos_hint: {"center_x":0.5, "center_y":.15}
                    on_release:
                        app.salvar()
<EmpreScreen>:
    name : "empre"
    BoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "Rent Car"
            right_action_items: [["close",lambda x: app.sair()]]
            left_action_items: [["car-multiple",lambda x: None]]
            height:50

            MDSwitch:
                id: switch
                size: 40,30
                width:40
                pos_hint: {"center_x":0.1, "center_y":0.5}
                on_active: app.check(*args)
                thumb_color: 1,1,1,1

        MDTabs:
            id: tabs
            Tab:
                text: 'Veiculos'
                
                MDCard:
                    size_hint: .96, 0.97
                    radius: [19,19,10,10]
                    orientation: "vertical"
                    spacing: '8dp'
                    padding: '25dp'
                    pos_hint: {"center_x":0.5, "center_y":.50}

                MDIconButton:
                    id: car
                    icon: "shield-car"
                    user_font_size: "32sp"
                    theme_text_color: "Custom"
                    text_color: [71/200,73/200,82/200,2] 
                    pos_hint: {"center_x":0.5, "center_y":.90}

                TooltipMDIconButton:
                    id: upd
                    icon: "update"
                    theme_text_color: "Custom"
                    user_font_size: "25sp"
                    theme_text_color: "Custom"
                    tooltip_text: "Actualizar estado"
                    text_color: [71/200,73/200,82/200,2] 
                    pos_hint: {"center_x":.84, "center_y":.93}
                    on_release: app.actua()

                MDTextField:
                    id: hu
                    hint_text: "Insira a marca"
                    size_hint_x:.79
                    font_size: 15
                    pos_hint: {"center_x":0.5, "center_y":.79}

                MDTextField:
                    id:mdl
                    hint_text: "Modelo"
                    size_hint_x:.39
                    font_size: 15
                    pos_hint: {"center_x":0.3, "center_y":.68}
                
                MDTextField:
                    id: matri
                    hint_text: "Matricula"
                    size_hint_x:.34
                    helper_text:'erro'
                    helper_text_mode:  'on_error'                    
                    font_size: 15
                    required: True
                    pos_hint: {"center_x":.72, "center_y":.68}
                
                MDTextField:
                    id: tp
                    hint_text: "Tipo de Veiculo"
                    size_hint_x:.79
                    font_size: 15
                    pos_hint: {"center_x":0.5, "center_y":.57}

                MDTextField:
                    id: cr
                    hint_text: "Cor"
                    size_hint_x:.39
                    font_size: 15
                    pos_hint: {"center_x":0.3, "center_y":.46}
                
                MDTextField:
                    id: an
                    hint_text: "Ano...."
                    size_hint_x:.34
                    max_text_length: 4                 
                    font_size: 15
                    pos_hint: {"center_x":.73, "center_y":.46}

                MDTextField:
                    id: conh
                    hint_text: "Combustível"
                    size_hint_x:.79
                    font_size: 15
                    pos_hint: {"center_x":0.5, "center_y":.35}

                MDTextField:
                    id: mt
                    hint_text:"Nº do motor"
                    size_hint_x:.39
                    font_size: 15
                    pos_hint: {"center_x":0.3, "center_y":.24}

                MDTextField:
                    id: acti
                    hint_text: "Activo"
                    size_hint_x:.34                
                    font_size: 15
                    pos_hint: {"center_x":.73, "center_y":.24}                    

                MDFillRoundFlatIconButton:
                    id:cad
                    text: "Cadastrar Veiculo"
                    icon: "content-save-move"
                    pos_hint: {"center_x":0.5, "center_y":.12}
                    on_press:
                        app.gravar_veiculo()

            Tab:
                id: tbdop
                text: 'Taxas'
                
                MDCard:
                    size_hint: .96, 0.97
                    radius: [19,19,10,10]
                    orientation: "vertical"
                    pos_hint: {"center_x":0.5, "center_y":.50}

                MDIconButton:
                    id: hj
                    icon: "clipboard-edit"
                    theme_text_color: "Custom"
                    text_color: [71/200,73/200,82/200,2] 
                    user_font_size: "31sp"
                    pos_hint: {"center_x":0.5, "center_y":.88}
                    
                MDIconButton:
                    id: updd
                    icon: "update"
                    theme_text_color: "Custom"
                    user_font_size: "25sp"
                    theme_text_color: "Custom"
                    text_color: [71/200,73/200,82/200,2] 
                    pos_hint: {"center_x":.84, "center_y":.92}
                    on_release:app.actualiz()

                MDTextField:
                    id:marca
                    size_hint_x:.80
                    hint_text: "Insira o modelo do veiculo"
                    font_size: 15
                    pos_hint: {"center_x":0.5, "center_y":.76}

                MDTextField:
                    id: vd
                    size_hint_x:.80
                    hint_text: "Valor diario kz...."
                    font_size: 15
                    pos_hint: {"center_x":0.5, "center_y":.65}

                MDTextField:
                    id: vs
                    size_hint_x:.80
                    hint_text: "Valor semanal kz...."
                    font_size: 15
                    pos_hint: {"center_x":0.5, "center_y":.54}

                MDTextField:
                    id: vm
                    size_hint_x:.80
                    hint_text: "Valor mensal kz...."
                    font_size: 15
                    pos_hint: {"center_x":0.5, "center_y":.42}

                MDTextField:
                    id: vlf
                    size_hint_x:.80
                    hint_text: "Valor fim de semana kz...."
                    font_size: 15
                    pos_hint: {"center_x":0.5, "center_y":.30}   

                MDFillRoundFlatIconButton:
                    id: cd
                    icon: "clipboard-text"
                    text: "Cadastrar Taxas"
                    pos_hint: {"center_x":0.5, "center_y":.12}
                    on_release: app.gravar_taxas()
                                 
            Tab:
                id: tabd
                text: 'Clientes'

                MDCard:
                    id: card7
                    size_hint_x: .98
                    radius:[15,15,15,15]
                    orientation: "vertical"
                    pos_hint: {'center_x':0.5,'center_y':.42}   

                MDCard:
                    size_hint: .98, 0.10
                    md_bg_color:1,1,1,1
                    radius:[9,9,9,9]
                    orientation: "vertical"
                    pos_hint: {'center_x':0.5,'center_y':.93}    

                    FloatLayout: 
                        TooltipMDIconButton:
                            id: atc
                            icon: "update"
                            user_font_size: "30dp"
                            theme_text_color: "Custom"
                            text_color: [169/255,169/255,169/255,2]
                            tooltip_text: "Actualizar clientes recentes"
                            pos_hint: {"center_x":.38, "center_y":0.5} 
                            on_release: app.client()

                        TooltipMDIconButton:
                            id: pedu
                            icon: "delete"
                            user_font_size: "30sp"
                            theme_text_color: "Custom"
                            tooltip_text: "Eleminar pedido"
                            text_color: [169/255,169/255,169/255,2]
                            pos_hint: {"center_x":.63, "center_y":0.5} 
                            on_release: app.client()

            Tab:
                id: pedid
                text: 'Pedidos'

                MDCard:
                    id: card8
                    size_hint_x: .98
                    radius:[15,15,15,15]
                    orientation: "vertical"
                    pos_hint: {'center_x':0.5,'center_y':.41}   

                MDCard:
                    size_hint: .98, 0.10
                    md_bg_color:1,1,1,1
                    radius:[9,9,9,9]
                    orientation: "vertical"
                    pos_hint: {'center_x':0.5,'center_y':.93}    

                    FloatLayout: 
                        TooltipMDIconButton:
                            id: peo
                            icon: "update"
                            user_font_size: "30sp"
                            theme_text_color: "Custom"
                            tooltip_text: "Actualizar pedidos"
                            text_color:[169/255,169/255,169/255,2]
                            pos_hint: {"center_x":.36, "center_y":0.5} 
                            on_release: app.pedido_load()

                        TooltipMDIconButton:
                            id: pede
                            icon: "gmail"
                            user_font_size: "30sp"
                            theme_text_color: "Custom"
                            tooltip_text: "Responder Pedido"
                            text_color:[169/255,169/255,169/255,2]
                            pos_hint: {"center_x":.53, "center_y":0.5} 
                            on_release: app.responder()
                        
                        TooltipMDIconButton:
                            id: ped
                            icon: "delete-empty"
                            user_font_size: "30sp"
                            theme_text_color: "Custom"
                            tooltip_text: "Eliminar pedido"
                            text_color:[169/255,169/255,169/255,2]
                            pos_hint: {"center_x":.70, "center_y":0.5} 
                            on_release: app.pedido_load()

            Tab:
                id: vei
                text: "Consultar Veiculos"

                MDCard:
                    id:card9
                    size_hint_x: .98
                    radius:[15,15,15,15]
                    orientation: "vertical"
                    pos_hint: {'center_x':0.5,'center_y':.42}                

                MDCard:
                    size_hint: .98, 0.10
                    md_bg_color:1,1,1,1
                    radius:[9,9,9,9]
                    orientation: "vertical"
                    pos_hint: {'center_x':0.5,'center_y':.93}                       

                    FloatLayout:  
                        TooltipMDIconButton:
                            icon:"update"
                            tooltip_text:"Actualizar veiculos"
                            user_font_size:"30sp"
                            theme_text_color:"Custom"
                            text_color:[169/255,169/255,169/255,2] 
                            pos_hint: {"center_x":.38, "center_y":0.5} 
                            on_release: app.veicu()

                        TooltipMDIconButton:
                            icon:"delete-empty"
                            tooltip_text:"Eliminar veiculo"
                            user_font_size:"30sp"
                            theme_text_color:"Custom"
                            text_color:[169/255,169/255,169/255,2] 
                            pos_hint: {"center_x":.63, "center_y":0.5} 
                            on_release: app.veicu()
            Tab:
                id: tax
                text: "Consultar Taxas"
                MDCard:
                    id:card10
                    size_hint_x: .98
                    radius:[15,15,15,15]
                    orientation: "vertical"
                    pos_hint: {'center_x':0.5,'center_y':.41}   

                MDCard:
                    size_hint: .98, 0.10
                    md_bg_color:1,1,1,1
                    radius:[9,9,9,9]
                    orientation: "vertical"
                    pos_hint: {'center_x':0.5,'center_y':.93}    

                    FloatLayout:               

                        TooltipMDIconButton:
                            icon:"update"
                            tooltip_text:"Actualizar Taxas"
                            user_font_size:"30sp"
                            theme_text_color:"Custom"
                            text_color: [169/255,169/255,169/255,2] 
                            pos_hint: {"center_x":.38, "center_y":0.5} 
                            on_release: app.taxasrec()

                        TooltipMDIconButton:
                            icon:"delete"
                            tooltip_text:"Eliminar Taxas"
                            user_font_size:"30sp"
                            theme_text_color:"Custom"
                            text_color:[169/255,169/255,169/255,2] 
                            pos_hint: {"center_x":.63, "center_y":0.5}       
                            on_release: app.taxasrec()                       

"""
class LoginScreen(Screen):
    sen = ObjectProperty(None)
    pass
class  EmpreScreen(Screen):
    pass
class Tab(FloatLayout, MDTabsBase):
    pass    
class Content(BoxLayout):
    pass

sm = ScreenManager()
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(EmpreScreen(name='empre'))

firebase = firebase.FirebaseApplication('https://rent-car-banco-dados-default-rtdb.firebaseio.com/',None)

TRIPS_SELECTED = []
url = 'https://login-7c9e3-default-rtdb.firebaseio.com/.json'
urll = 'https://login-7c9e3-default-rtdb.firebaseio.com/.json'
class RentCarEmpresa(MDApp):    
    def on_start(self):
        self.client()
        self.veicu()
        self.pedido()
        self.taxasrec()
        self.strng.get_screen("empre").ids.acti.text = "Não"
        
    def client(self):
        threading.Thread(target=self.client_load).start()

    def client_load(self):
        if TRIPS_SELECTED:
            for n_trip in TRIPS_SELECTED:
                dele = requests.delete(f'https://rent-car-banco-dados-default-rtdb.firebaseio.com/Cliente/{n_trip}.json')
            toast("Cliente eliminado")

        resquest = requests.get(f'https://rent-car-banco-dados-default-rtdb.firebaseio.com/Cliente.json')
        buscare = json.loads(resquest.content.decode())

        cols = ["ID"]
        values = []
        cont = 0

        for trip, data in buscare.items():
            lista = []
            lista.append(trip)

            for key, info in data.items():
                lista.append(info)

                if cont == 0:
                    cols.append(key)
            cont +=1
            values.append(lista)

        self.client_tabela(cols, values)

    def on_check_press(self, instance_table,current_row):
        if current_row[0] in TRIPS_SELECTED:
            TRIPS_SELECTED.remove(current_row[0])
        else:
            TRIPS_SELECTED.append(current_row[0])

    @mainthread
    def client_tabela(self, cols, values):
        self.strng.get_screen("empre").ids.card7.clear_widgets()
        self.cliente = MDDataTable(pos_hint={'center_x':0.5,'center_y':.50},
                            rows_num=300,
                            size_hint = (.99,0.90),
                            use_pagination=False,
                            column_data=[    
                                (col,dp(26)) for col in cols                                                             
                            ],
                            row_data = values,
                            check = True
                            )               
        self.cliente.bind(on_check_press=self.on_check_press)        
        self.strng.get_screen("empre").ids.card7.add_widget(self.cliente)

    def veicu(self):
        threading.Thread(target=self.veicu_load).start()

    def veicu_load(self):
        if TRIPS_SELECTED:
            for n_trip in TRIPS_SELECTED:
                dele = requests.delete(f'https://rent-car-banco-dados-default-rtdb.firebaseio.com/Veiculos/{n_trip}.json')
            toast("Veiculo eliminado")

        request = requests.get(f'https://rent-car-banco-dados-default-rtdb.firebaseio.com/Veiculos/.json')
        pegarr = json.loads(request.content.decode())

        cols = ["Modelo"]
        values = []
        cont = 0

        for trip, data in pegarr.items():
            lista=[]
            lista.append(trip)

            for key, info in data.items():
                lista.append(info)
                if cont == 0 :
                    cols.append(key)

            cont+=1
            values.append(lista)

        self.veicu_table(cols,values)

    def on_check_press(self, instance_table,current_row):
        if current_row[0] in TRIPS_SELECTED:
            TRIPS_SELECTED.remove(current_row[0])
        else:
            TRIPS_SELECTED.append(current_row[0])

    @mainthread
    def veicu_table(self, cols, values):
        self.strng.get_screen("empre").ids.card9.clear_widgets()
        self.veiculo = MDDataTable(pos_hint={'center_x':0.5,'center_y':.59},
                            rows_num=300,
                            size_hint = (.99,0.90),
                            use_pagination=False,
                            column_data=[    
                                (col,dp(27)) for col in cols                                                             
                            ],
                            row_data = values,
                            check = True
                            )    
        self.veiculo.bind(on_check_press=self.on_check_press)
        self.strng.get_screen("empre").ids.card9.add_widget(self.veiculo)

    def taxasrec(self):
        threading.Thread(target=self.taxas_lod).start()
    
    def taxas_lod(self):
        if TRIPS_SELECTED:
            for n_trip in TRIPS_SELECTED:
                post_rquests = requests.delete(f'https://rent-car-banco-dados-default-rtdb.firebaseio.com/Taxas/{n_trip}.json')
            toast("Taxas eliminada") 

        bd = requests.get(f'https://rent-car-banco-dados-default-rtdb.firebaseio.com/Taxas.json')
        buscar = json.loads(bd.content.decode())

        count = 0
        values = []
        cols = ["Modelo"]

        for trip, data in buscar.items():
            lista = []
            lista.append(trip)

            for key, info in data.items():
                lista.append(info)
                if count == 0:
                    cols.append(key) 
            count +=1
            values.append(lista)
        
        self.taxastable(cols, values)
    
    def on_check_press(self, instance_table,current_row):
        if current_row[0] in TRIPS_SELECTED:
            TRIPS_SELECTED.remove(current_row[0])
        else:
            TRIPS_SELECTED.append(current_row[0])

    @mainthread
    def taxastable(self, cols, values):
        layout = AnchorLayout()
        self.strng.get_screen("empre").ids.card10.clear_widgets()
        self.taxass = MDDataTable(pos_hint={'center_x':0.5,'center_y':.5},
                            rows_num=300,
                            size_hint = (.99,0.90),
                            use_pagination=False,
                            column_data=[    
                                (col,dp(28)) for col in cols                                                             
                            ],
                            row_data = values,
                            check = True
                            )    
        self.taxass.bind(on_check_press=self.on_check_press)
        self.strng.get_screen("empre").ids.card10.add_widget(self.taxass)
        return layout
        
    def pedido(self):
        threading.Thread(target=self.pedido_load).start()

    def pedido_load(self):
        if TRIPS_SELECTED:
            for n_trip in TRIPS_SELECTED:
                post_request = requests.delete(f'https://rent-car-banco-dados-default-rtdb.firebaseio.com/Pedidos/{n_trip}.json')
            toast("Pedido excluído")
        buscar = requests.get(f'https://rent-car-banco-dados-default-rtdb.firebaseio.com/Pedidos.json')
        buscarorganizado = json.loads(buscar.content.decode())

        count = 0
        cols = ["ID"]
        values = []

        for trip, data in buscarorganizado.items():
            lista = []
            lista.append(trip)

            for key, info in data.items():
                lista.append(info)
                if count == 0:
                    cols.append(key)

            count +=1
            values.append(lista)

        self.actualizar(cols, values)

    def on_check_press(self, instance_table, current_row):
        if current_row [0] in TRIPS_SELECTED:
            TRIPS_SELECTED.remove(current_row [0])
        else:
            TRIPS_SELECTED.append(current_row[0])

    @mainthread
    def actualizar(self,cols,values): 
        self.strng.get_screen("empre").ids.card8.clear_widgets()
        self.pedido = MDDataTable(pos_hint={'center_x':0.5,'center_y':.40},
                            rows_num=300,
                            size_hint = (.99,0.80),
                            use_pagination=False,
                            column_data=[    
                                (col,dp(27)) for col in cols                                                             
                            ],
                            row_data = values,
                            check = True
                            )    
        self.pedido.bind(on_check_press = self.on_check_press)
        self.strng.get_screen("empre").ids.card8.add_widget(self.pedido)  

    def build(self):
        self.theme_cls.primary_palette = "Blue" 
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.accent_palette = "Yellow"
        self.strng = Builder.load_string(janela)
        
        animka = Animation(text_color = (1,1,1,1)) + Animation(text_color = (1,1,1, .2))
        animka.repeat = True        
        animka.start(self.strng.get_screen("empre").ids.cad)

        an = Animation(text_color = (1,1,1,1)) + Animation(text_color = (1,1,1, .2))
        an.repeat = True         
        an.start(self.strng.get_screen("empre").ids.cd)

        animae = Animation(text_color = (1,1,1,1)) + Animation(text_color = (1,1,1, .2))
        animae.repeat = True        
        animae.start(self.strng.get_screen("login").ids.acessar)

        animaed = Animation(text_color = (1,1,1,1)) + Animation(text_color = (1,1,1, .2))
        animaed.repeat = True 
        animaed.start(self.strng.get_screen("login").ids.grav)

        animaal = Animation(text_color = ([71/200,73/200,82/200,2])) + Animation (text_color = (1,1,1,1))
        animaal.repeat=True       
        animaal.start(self.strng.get_screen("empre").ids.updd)

        aimaak = Animation(text_color = ([169/255,169/255,169/255,2])) + Animation (text_color = (128/255,128/255,128/255,1))
        aimaak.repeat=True
        aimaak.start(self.strng.get_screen("empre").ids.atc)

        animali = Animation(text_color = ([169/255,169/255,169/255,2])) + Animation (text_color = (128/255,128/255,128/255,1))
        animali.repeat=True       
        animali.start(self.strng.get_screen("empre").ids.ped) 
    
        animalid = Animation(text_color = ([169/255,169/255,169/255,2])) + Animation (text_color = (128/255,128/255,128/255,1))
        animalid.repeat=True       
        animalid.start(self.strng.get_screen("empre").ids.pede)     

        animalui = Animation(text_color = ([169/255,169/255,169/255,2])) + Animation (text_color = (128/255,128/255,128/255,1))
        animalui.repeat=True       
        animalui.start(self.strng.get_screen("empre").ids.peo)                                                     
    
        animaluiy = Animation(text_color = ([169/255,169/255,169/255,2])) + Animation (text_color = (128/255,128/255,128/255,1))
        animaluiy.repeat=True       
        animaluiy.start(self.strng.get_screen("empre").ids.pedu)  

        animaea = Animation(size_hint_y = (0.88),duration=1)
        animaea.start(self.strng.get_screen("login").ids.card37)  

        return self.strng  
    
    def gravar_veiculo(self):
        marc = self.strng.get_screen("empre").ids.hu.text
        mode = self.strng.get_screen("empre").ids.mdl.text
        anoo = self.strng.get_screen("empre").ids.an.text
        combu = self.strng.get_screen("empre").ids.conh.text
        tipos = self.strng.get_screen("empre").ids.tp.text
        cores = self.strng.get_screen("empre").ids.cr.text
        matr = self.strng.get_screen("empre").ids.matri.text
        mti = self.strng.get_screen("empre").ids.mt.text
        ar = self.strng.get_screen("empre").ids.acti.text

        if mode is "" or marc is "" or anoo is "" or combu is "" or tipos is "" or cores is "" or matr is "":
            toast("Por favor preencha todo o formulário")
        elif len(marc)>15 or len(marc)<2:
            toast("Marca do veiculo inválido")
        elif len(anoo)>4:
            toast("Ano do veiculo inválido")
        elif combu not in ("Gasolina","gasoleo","Gasoleo","gasolina"):
            toast("Tipo de Combustivél inválido")
        elif tipos not in ("Autómatico","manual","Automatico","automatico","automático","Manual","Automático"):
            toast("Tipo de veiculo inválido")            
        elif re. search ("[a-zA-Z]", mti):
            toast("O número do motor está inválido")
        elif ar not in ("Não","não","Sim","sim"):
            toast("Apenas sim ou não")
        else:
            closer = MDIconButton(icon="thumb-up",on_release=self.clos)
            self.dialog = MDDialog(title="Rent Car",text="Dados do veiculo "+marc+" cadastrado com sucesso",size_hint=(0.8,0.3),buttons=[closer])
            self.dialog.open()
            result = firebase.put('/Veiculos',mode,{"Alugado":ar,"Matricula":matr,"Marca":marc,"Ano":anoo,"Cor":cores,"Tipo de Veiculo":tipos,"Combusível":combu,"Nº do Motor":mti}) 
            marc = self.strng.get_screen("empre").ids.hu.text=""
            mode = self.strng.get_screen("empre").ids.mdl.text=""
            anoo = self.strng.get_screen("empre").ids.an.text=""
            combu = self.strng.get_screen("empre").ids.conh.text=""
            tipos = self.strng.get_screen("empre").ids.tp.text=""
            cores = self.strng.get_screen("empre").ids.cr.text=""
            matr = self.strng.get_screen("empre").ids.matri.text=""
            mti = self.strng.get_screen("empre").ids.mt.text=""
            ar = self.strng.get_screen("empre").ids.acti.text=""

    def actua(self):
            mode = self.strng.get_screen("empre").ids.mdl.text
            ar = self.strng.get_screen("empre").ids.acti.text
            marc = self.strng.get_screen("empre").ids.hu.text=""
            cores = self.strng.get_screen("empre").ids.cr.text=""
            if mode is "":
                toast("Preencha o modelo pretendio")   
            elif ar is "":
                toast("Preencha o estado aluguel")
            elif ar not in ("Não","não","Sim","sim"):
                toast("Apenas Sim ou Não")
            else:
                toast("Estado de alguel actualizado")
                signup_info = firebase.put('/Veiculos\"{mode}\"','Alugado',ar)
                print(signup_info)
           
    def gravar_taxas(self):
        valor1 = self.strng.get_screen("empre").ids.vd.text
        valor2  = self.strng.get_screen("empre").ids.vs.text
        valor3 = self.strng.get_screen("empre").ids.vm.text
        valor4 = self.strng.get_screen("empre").ids.vlf.text
        modeo = self.strng.get_screen("empre").ids.marca.text

        if modeo is "" or valor1 is "" or valor2 is "" or valor3 is "" or valor4 is "":
            toast("Preencha o formulário correctamente!")
        
        elif len(modeo)<3:
            toast("Modelo do veiculo inválido")
            
        elif len(valor1)<3 or len(valor2)<3 or len(valor3)<3 or len(valor4)<3:
            toast("Numeros dos valores inválido")

        elif  re. search ("[a-zA-Z]", valor1) or re. search ("[a-zA-Z]", valor2) or re. search ("[a-zA-Z]", valor3) or re. search ("[a-zA-Z]", valor4):
            toast("Valor do veículo inválido")

        else:            
            gravar = firebase.put('/Taxas',modeo,{"Valor Diário":valor1,"Valor Semanal":valor2,"Valor Mensal":valor3,"Fim de Semana":valor4})
            fecharr = MDIconButton(icon="thumb-up",on_release=self.clos)
            self.dialog = MDDialog(title="Rent Car",text="Taxas do veiculo "+modeo+" cadastrado com sucesso!",size_hint=(0.8,0.3),buttons=[fecharr])
            self.dialog.open()
            
    def actualiz(self):
        valor1 = self.strng.get_screen("empre").ids.vd.text
        valor2  = self.strng.get_screen("empre").ids.vs.text
        valor3 = self.strng.get_screen("empre").ids.vm.text
        valor4 = self.strng.get_screen("empre").ids.vlf.text
        modeo = self.strng.get_screen("empre").ids.marca.text

        if modeo is "" or valor1 is "" or valor2 is "" or valor3 is "" or valor4 is "":
            toast("Preencha o formulário correctamente!")
        
        elif len(modeo)<3:
            toast("Modelo do veiculo inválido")
            
        elif len(valor1)<3 or len(valor2)<3 or len(valor3)<3 or len(valor4)<3:
            toast("Numeros dos valores inválido")

        elif  re. search ("[a-zA-Z]", valor1) or re. search ("[a-zA-Z]", valor2) or re. search ("[a-zA-Z]", valor3) or re. search ("[a-zA-Z]", valor4):
            toast("Valor do veículo inválido")

        else:            
            gravar = firebase.put('/Taxas',modeo,{"Valor Diário":valor1,"Valor Semanal":valor2,"Valor Mensal":valor3,"Fim de Semana":valor4})
            toast("Taxas "+modeo+ " actualizadas")
                   
    def salvar(self):   
        nomr = self.strng.get_screen("login").ids.nom.text
        email = self.strng.get_screen("login").ids.ema.text
        password = self.strng.get_screen("login").ids.seusuario.text
        empresa = self.strng.get_screen("login").ids.sempresa.text

        if nomr is "" or email is "" or password is "" or empresa is "":
            toast("Preencha todos os campos")
            
        elif not re. match(r"[^@]+@[^@]+\.[^@]+", email):
            toast("Email incorrecto "+nomr)
                           
        elif empresa != "rentcar2021":
            toast("Senha da empresa incorrecta "+nomr)
                           
        else:            
            signup_info = str({f'\"{email}\":{{"Nome":\"{nomr}\","Senha":\"{password}\"}}'})
            signup_info = signup_info.replace(".","-")
            signup_info = signup_info.replace("\'","")
            to_database = json.loads(signup_info)
            print((to_database))
            requests.patch(url = urll,json = to_database)
            toast("Dados cadastrado com sucesso")

    auth =  'fVCTQKZdM93XfnRWQd2UEgqLeYEgzueEf5SllvfF'
    
    def login(self):
        emaill = self.strng.get_screen("login").ids.emai.text
        senha = self.strng.get_screen("login").ids.sen.text

        self.login_check = False
        request = requests.get(url+'?auth'+self.auth)
        data = request.json()
        emails = set()
        for key,value in data.items():
            emails.add(key)
        if emaill in emails and senha == data[emaill]['Senha']:
            self.login_check = True
            self.strng.get_screen('empre').manager.current = 'empre'           
        else:
            toast("Funcionário não cadastrado")
            senha = self.strng.get_screen("login").ids.sen.text = ""
    i = 1       
    def togglevisibility(self):
        self.i += 1
        if self.i%2 == 0:
            self.strng.get_screen("login").ids.sen.password =  False           
            self.strng.get_screen("login").ids.seusuario.password =  False          
            self.strng.get_screen("login").ids.lok.icon =  "eye"
            self.strng.get_screen("login").ids.loko.icon =  "eye"
        else:
           self.strng.get_screen("login").ids.sen.password =  True
           self.strng.get_screen("login").ids.seusuario.password =  True         
           self.strng.get_screen("login").ids.lok.icon =  "eye-off"
           self.strng.get_screen("login").ids.loko.icon =  "eye-off"
           
    def plo(self):
        self.i += 1
        if self.i%2 == 0:
            self.strng.get_screen("login").ids.sempresa.password =  False            
            self.strng.get_screen("login").ids.loki.icon =  "eye"
        else:
           self.strng.get_screen("login").ids.sempresa.password =  True  
           self.strng.get_screen("login").ids.loki.icon =  "eye-off"
           
    def check(self, checkbox, value):
        if value:
            self.theme_cls.theme_style = 'Dark'
            self.strng.get_screen("empre").ids.switch.thumb_color_down = [71/200,73/200,82/200,2] 
            self.strng.get_screen("empre").ids.car.text_color = 1,1,1,1 
            self.strng.get_screen("empre").ids.upd.text_color = 1,1,1,1
            self.strng.get_screen("empre").ids.updd.text_color = 1,1,1,1          
            self.strng.get_screen("empre").ids.hj.text_color = 1,1,1,1
        else:
            self.theme_cls.theme_style = 'Light'
            self.strng.get_screen("empre").ids.switch.thumb_color_down = 1,1,1,1
            self.strng.get_screen("empre").ids.car.text_color = [71/200,73/200,82/200,2] 
            self.strng.get_screen("empre").ids.upd.text_color = [71/200,73/200,82/200,2] 
            self.strng.get_screen("empre").ids.updd.text_color = [71/200,73/200,82/200,2]            
            self.strng.get_screen("empre").ids.hj.text_color = [71/200,73/200,82/200,2]
            
    def responder(self):
        self.dialog = MDDialog(
            type = "custom",
            content_cls = Content(),
        )
        self.dialog.open()

    def resp1(self):
        ema = self.dialog.content_cls.ids.cli.text
        if ema is "":
            toast("Preencha o email senhor")
            
        elif not re. match(r"[^@]+@[^@]+\.[^@]+", ema):
            toast("Email incorrecto senhor")            
        else:
            email_from = "rentcarluanda2021@gmail.com"
            email_to = ema
            senha = "rentcar2021"
            mensagem = "O seu pedido de alguel foi aceite com sucesso,esperamos que cumpra com as respectivas"
            outra = " normas e regras. \n\nObrigado pela preferencia!"
            titulo = "RentCar Luanda"

            smtp = "smtp.gmail.com"
            server = smtplib.SMTP(smtp, 587)
            server.starttls()
            server.login(email_from,senha)
            
            message = 'Subject: {}\n\n\n{}{}'.format(titulo,mensagem,outra)
            server.sendmail(email_from,email_to,message)

            toast("Notificação enviado com exito")
            
    def resp2(self):
        ema = self.dialog.content_cls.ids.cli.text

        if ema is "":
            toast("Preencha o email senhor!")
            
        elif not re.match(r"[^@]+@[^@]+\.[^@]+",ema):
            toast("Email incorrecto senhor")
        else:
            email_from = "rentcarluanda2021@gmail.com"
            email_to = ema
            senha = "rentcar2021"
            mensagem = "O seu pedido foi recusado, pois o veiculo not se encontra disponivel para ser alugado"
            mensa = " escolhe outro veiculo da sua escolha. \n\nObrigado pela preferencia!"
            titulo = "RentCar Luanda"

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(email_from,senha)

            messages = 'Subject: {}\n\n{}{}'.format(titulo,mensagem,mensa)
            server.sendmail(email_from,email_to,messages)

            toast("Notificação enviada com sucesso")

    def sair(self):
        sim = MDIconButton(icon="thumb-down",on_release=self.clos)
        nao = MDIconButton(icon="thumb-up",on_release=self.fech)
        self.dialog = MDDialog(title="Rent Car",text="Tens a certeza que queres sair?",size_hint=(0.7,0.5),buttons=[sim,nao])
        self.dialog.open()
        
    def closs(self):
        self.dialog.dismiss()
    def clos(self,obg):
        self.dialog.dismiss()
    def fech(self,obj):
        self.stop()
    
RentCarEmpresa().run()
