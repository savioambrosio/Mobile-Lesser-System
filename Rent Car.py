from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.button import MDFlatButton,MDIconButton,MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog 
from kivymd.uix.picker import MDDatePicker,MDTimePicker
from datetime import datetime
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivy.factory import Factory
from kivy.animation import Animation 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.snackbar import Snackbar
from kivymd.toast import toast
from kivy.clock import Clock
from kivymd.uix.tab import MDTabsBase
import smtplib
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivy.uix.screenmanager import ScreenManager,Screen
from kivymd.uix.datatables import MDDataTable
import webbrowser
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A3
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
from kivy.metrics import dp
import requests
import json
from random import randint
from reportlab.pdfgen import canvas
import re
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import ObjectProperty
from time import sleep
from firebase import firebase
from kivymd.toast import toast 
from kivy.clock import mainthread
import threading

Window.size =(285,500)

janelas = """
#:import utils kivy.utils
#:import STANDARD_INCREMENT kivymd.material_resources.STANDARD_INCREMENT
<content>
    md_bg_color: 1,1,1,1
    orientation :"vertical"
    size_hint_y: None
    height: "260dp"

    Button
        size_hint:0.70,None
        height: 62
        background_normal: "Imagens/mul.png"        
        border:0,0,0,0
        pos_hint: {"center_x":0.5, "center_y":0.6}
        on_release: app.saire()
        
    MDTextField:
        id: senha
        hint_text: "Senha do cartão"
        password: True
        icon_right: "sack"
        icon_right_color:self.theme_cls.primary_color          
    
    ScrollView:   
        MDList:
            size_hint_y: None
            height: "40dp"
            spacing: "7dp"
            padding: "7dp"
            orientation: "horizontal"
            Button:
                size_hint:0.40,None
                height:93
                background_normal: "Imagens/pol.png"
                border:2,2,2,2
                on_release:app.relatorio()
            Button:
                size_hint:0.40,None
                height: 93
                background_normal: "Imagens/ko.png"        
                border:2,2,2,2
                on_release:app.relatorio()
            Button:
                size_hint:0.40,None
                height:93
                background_normal: "Imagens/bu.png"
                on_release:app.relatorio()
            Button:
                size_hint:0.40,None
                height:95
                background_normal: "Imagens/atla.png"        
                border:2,2,2,2
                on_release:app.relatorio()
            Button:
                size_hint:0.40,None
                height:93
                background_normal: "Imagens/bpi.png"        
                border:2,2,2,2
                on_release:app.relatorio()
                                                
<TooltipMDIconButton@MDIconButton+MDTooltip>

<CardItem@RelativeLayout>:
    size_hint_y:None
    height:125
    orientation: "vertical"
   
<CustomSheet@BoxLayout>:
    orientation: "vertical"
    size_hint_y: None
    height:"350dp"

    MDToolbar:
        title: "Sobre a Rent Car"
        right_action_items: [["car-multiple",lambda x: None]]
        height: 35

    FloatLayout:
        MDIconButton:
            icon: "email"
            pos_hint: {"center_x":0.1, "center_y":0.8}
            user_font_size:"21sp" 

        MDLabel:
            text: "RentCarLuanda@gmail.com"
            font_size: 15             
            pos_hint: {"center_x":0.7, "center_y":0.8}
            
        MDIconButton:
            icon: "map-marker-multiple"
            pos_hint: {"center_x":0.1, "center_y":0.6}
            user_font_size:"21sp" 

        MDLabel:
            text: "Luanda, Nova Vida, Rua 70"
            font_size: 15  
            pos_hint: {"center_x":0.7, "center_y":0.6}

        MDIconButton:
            icon: "phone-classic"
            pos_hint: {"center_x":0.1, "center_y":0.4}
            user_font_size:"21sp" 

        MDLabel:
            text: "Aberto: 8:30/20:00 Segunda a Sábado"
            font_size: 14 
            pos_hint: {"center_x":0.7, "center_y":0.2}     

        MDIconButton:
            icon: "clock"
            pos_hint: {"center_x":0.1, "center_y":0.2}
            user_font_size:"21sp" 

        MDLabel:
            text: "992419634/915918858"
            font_size: 15            
            pos_hint: {"center_x":0.7, "center_y":0.4}

<MyTile@SmartTileWithStar>
    size_hint_y: None
    height: "300dp"

Screen:
    name: "get_screen"

    NavigationLayout:
        md_bg_color: 1,1,1,1
        ScreenManager:
            id: screen_manager  

            Screen:
                name: "menu"
                BoxLayout:
                    orientation: "vertical"                              
                    MDToolbar:
                        title: 'Rent Car '
                        left_action_items: [["close",lambda x: app.stop()]]
                        elevation: 10
                        height: 36

                        MDIconButton:
                            icon: "account-circle"
                            theme_text_color: "Custom"
                            text_color: 1,1,1,1
                            user_font_size:"25sp" 
                            tooltip_bg_color: [71/200,73/200,82/200,2]                                                     
                            pos_hint: {"center_x":0.2, "center_y":0.5}
                            on_release: screen_manager.current = "screen1" 

                        MDSwitch:
                            size:18,18
                            id: switch
                            width: 48
                            pos_hint: {"center_x":0.1, "center_y":0.5}
                            on_active: app.check(*args)
                            thumb_color: 1,1,1,1                            

                    Carousel:                                   
                        MDFloatLayout:
                            md_bg_color: 1,1,1, .2

                            MDCard:
                                id: card29                               
                                size_hint: .8, 0.54
                                height:30
                                pos_hint: {"center_x":.5,"center_y":.63}
                                radius: [10,10,8,8]
                                                            
                                orientation: 'vertical'

                                MDLabel:
                                    id: al2
                                    text:"Alugue qualquer veiculo                                       sem sair de casa!"
                                    theme_text_color: "Custom"
                                    font_style: "Caption"
                                    bold: True
                                    text_color: [71/200,73/200,82/200,2] 
                                    size_hint_y: None
                                    font_size: 15
                                    height: self.texture_size[1] 
                                    pos_hint: {"center_x":.53} 

                                Image:
                                    source: "Imagens/TCRF.png"                                 
                                    pos_hint: {"center_x":.5,"center_y":.8}

                                MDGridLayout:
                                    cols: 3
                                    adaptive_height: True       
                             
                            TooltipMDIconButton:
                                id: yordania
                                icon: "arrow-right-circle"
                                pos_hint: {"center_x":.9,"center_y":.52}
                                tooltip_text: "Deslize imagem a direita"
                                tooltip_bg_color: [71/200,73/200,82/200,2]
                                user_font_size:"23sp"   
                                theme_text_color: "Custom"
                                text_color:1,1,1,1
                                on_release: app.direita()
                            
                            TooltipMDIconButton:
                                id: inss  
                                icon: "instagram"
                                pos_hint: {"center_x":.44,"center_y":.52}
                                user_font_size:"24sp"
                                theme_text_color: "Custom"
                                text_color:[71/200,73/200,82/200,2]
                                tooltip_text: "Instagram"
                                tooltip_bg_color:[71/200,73/200,82/200,2]
                                on_release: app.insta()

                            TooltipMDIconButton:
                                id: facc
                                icon: "facebook"
                                pos_hint: {"center_x":.55,"center_y":.52}
                                user_font_size:"24sp"                                
                                theme_text_color: "Custom"
                                text_color:[71/200,73/200,82/200,2]
                                tooltip_text: "Facebook"
                                tooltip_bg_color:[71/200,73/200,82/200,2]
                                on_release: app.face()
                                                            
                            FloatLayout:
                                MDCard:
                                    size_hint: .9, 0.28
                                    md_bg_color:[128/255,128/255,128/255,1]
                                    pos_hint: {"center_x":.5,"center_y":.32} 
                                    orientation: 'vertical' 

                                MDIconButton:
                                    id:fgb                                
                                    icon: "star-outline"
                                    user_font_size: "26dp"
                                    theme_text_color:"Custom"
                                    text_color: 1,1,1,1
                                    pos_hint: {"center_x":0.3,"center_y":.40}
                                    on_release: app.rot()

                                MDIconButton:
                                    id: fg
                                    icon: "star-outline"
                                    user_font_size: "26dp"
                                    theme_text_color:"Custom"
                                    text_color: 1,1,1,1
                                    pos_hint: {"center_x":0.5,"center_y":.40}
                                    on_release: app.rot()

                                MDIconButton:
                                    id: fga
                                    icon: "star-outline"
                                    user_font_size: "26dp"
                                    theme_text_color:"Custom"
                                    text_color: 1,1,1,1
                                    pos_hint: {"center_x":0.7,"center_y":.40}
                                    on_release: app.rot()

                                MDLabel:
                                    text: "5 000kz /dia"
                                    theme_text_color: "Custom" 
                                    bold: True
                                    font_size: 16
                                    text_color:1,1,1,1
                                    pos_hint: {"center_x":0.6,"center_y":.29}

                                MDLabel:
                                    text: "Wolskgan 2016 Automático"
                                    theme_text_color: "Custom" 
                                    font_size: 14
                                    text_color: 1,1,1,1
                                    pos_hint: {"center_x":0.6,"center_y":.23}
                                        
                            MDFillRoundFlatIconButton:
                                id: bottta
                                size: 45,35
                                icon: "car-multiple"
                                text: "Frotas Veiculos"  
                                theme_text_color: "Custom"
                                text_color:1,1,1,1
                                font_style: "Subtitle1"
                                line_color: [71/200,73/200,82/200,2]
                                icon_color: 1, 0, 0, 1
                                pos_hint: {"center_x":.5,"center_y":0.1}
                                on_press:
                                    screen_manager.current = "screen2"                              
                                    
                        MDFloatLayout:
                            md_bg_color: 1,1,1, .2

                            MDCard:                            
                                size_hint: .9, 0.67
                                height:30
                                pos_hint: {"center_x":.5,"center_y":.63}
                                radius: [10,10,8,8]
                                                            
                                orientation: 'vertical'

                                MDLabel:
                                    text:"Alugue qualquer veiculo                                       sem sair de casa!"
                                    theme_text_color: "Custom"
                                    font_style: "Caption"
                                    bold: True
                                    text_color: [71/200,73/200,82/200,2] 
                                    size_hint_y: None
                                    font_size: 15
                                    height: self.texture_size[1] 
                                    pos_hint: {"center_x":.53} 

                                Image:
                                    source: "Imagens/lop.png"                                 
                                    pos_hint: {"center_x":.5,"center_y":.8}

                                MDGridLayout:
                                    cols: 3
                                    adaptive_height: True   

                            TooltipMDIconButton:
                                id: lefro
                                icon: "arrow-left-circle"
                                pos_hint: {"center_x":.1,"center_y":.52}
                                tooltip_text: "Deslize imagem a esquerda"
                                tooltip_bg_color: [71/200,73/200,82/200,2]
                                user_font_size:"23sp"   
                                theme_text_color: "Custom"
                                text_color:1,1,1,1
                                on_release: app.esquerda()
                            
                            TooltipMDIconButton:

                                id: inst
                                icon: "instagram"
                                pos_hint: {"center_x":.44,"center_y":.52}
                                user_font_size:"24sp"
                                theme_text_color: "Custom"
                                text_color:[71/200,73/200,82/200,2]
                                tooltip_text: "Instagram"
                                tooltip_bg_color:[71/200,73/200,82/200,2]
                                on_release: app.insta()

                            TooltipMDIconButton:

                                id: fact
                                icon: "facebook"
                                pos_hint: {"center_x":.55,"center_y":.52}
                                user_font_size:"24sp"                                
                                theme_text_color: "Custom"
                                text_color:[71/200,73/200,82/200,2]
                                tooltip_text: "Facebook"
                                tooltip_bg_color:[71/200,73/200,82/200,2]
                                on_release: app.face()    

                            TooltipMDIconButton:

                                id: rigp
                                icon: "arrow-right-circle"
                                pos_hint: {"center_x":.9,"center_y":.52}
                                user_font_size:"23sp"
                                tooltip_text: "Deslize imagem a direita"
                                tooltip_bg_color: [71/200,73/200,82/200,2]
                                theme_text_color: "Custom"
                                text_color:1,1,1,1   
                                on_release: app.direita()
                                
                            FloatLayout:
                                MDCard:
                                    size_hint: .9, 0.28
                                    md_bg_color:[128/255,128/255,128/255,1]
                                    pos_hint: {"center_x":.5,"center_y":.32} 
                                    orientation: 'vertical' 

                                MDIconButton:
                                    id:fgbb                                
                                    icon: "star-outline"
                                    user_font_size: "26dp"
                                    theme_text_color:"Custom"
                                    text_color: 1,1,1,1
                                    pos_hint: {"center_x":0.3,"center_y":.40}
                                    on_release: app.roto()

                                MDIconButton:
                                    id: fgg
                                    icon: "star-outline"
                                    user_font_size: "26dp"
                                    theme_text_color:"Custom"
                                    text_color: 1,1,1,1
                                    pos_hint: {"center_x":0.5,"center_y":.40}
                                    on_release: app.roto()

                                MDIconButton:
                                    id: fgaa
                                    icon: "star-outline"
                                    user_font_size: "26dp"
                                    theme_text_color:"Custom"
                                    text_color: 1,1,1,1
                                    pos_hint: {"center_x":0.7,"center_y":.40}
                                    on_release: app.roto()


                                MDLabel:
                                    text: "7 000kz /dia"
                                    theme_text_color: "Custom" 
                                    bold: True
                                    font_size: 16
                                    text_color:1,1,1,1
                                    pos_hint: {"center_x":0.6,"center_y":.29}

                                MDLabel:
                                    text: "Jeep 2016 Automático"
                                    theme_text_color: "Custom" 
                                    font_size: 14
                                    text_color: 1,1,1,1
                                    pos_hint: {"center_x":0.6,"center_y":.23}

                            MDFillRoundFlatIconButton:
                                id: botaa
                                size: 45,35
                                icon: "car-multiple"
                                text: "Frotas Veiculos"  
                                theme_text_color: "Custom"
                                text_color:1,1,1,1
                                font_style: "Subtitle1"
                                line_color: [71/200,73/200,82/200,2]
                                icon_color: 1, 0, 0, 1
                                pos_hint: {"center_x":.5,"center_y":0.1}
                                on_press:
                                    screen_manager.current = "screen2"                                  
                                                                    
                        MDFloatLayout:
                            md_bg_color: 1,1,1, .2
                       
                            MDCard:                              
                                size_hint: .9, 0.67
                                height:30
                                pos_hint: {"center_x":.5,"center_y":.63}
                                radius: [10,10,8,8]
                                                            
                                orientation: 'vertical'

                                MDLabel:
                                    text:"Alugue qualquer veiculo                                       sem sair de casa!"
                                    theme_text_color: "Custom"
                                    font_style: "Caption"
                                    bold: True
                                    text_color: [71/200,73/200,82/200,2] 
                                    size_hint_y: None
                                    font_size: 15
                                    height: self.texture_size[1] 
                                    pos_hint: {"center_x":.53} 

                                Image:
                                    source: "Imagens/ARGF.png"                                 
                                    pos_hint: {"center_x":.5,"center_y":.8}

                                MDGridLayout:
                                    cols: 3
                                    adaptive_height: True   

                            TooltipMDIconButton:
                                id: l
                                icon: "arrow-left-circle"
                                pos_hint: {"center_x":.1,"center_y":.52}
                                tooltip_text: "Deslize imagem a esquerda"
                                tooltip_bg_color: [71/200,73/200,82/200,2]
                                user_font_size:"23sp"   
                                theme_text_color: "Custom"
                                text_color:1,1,1,1
                                on_release: app.esquerda()
                            
                            TooltipMDIconButton:
                                id: i
                                icon: "instagram"
                                pos_hint: {"center_x":.44,"center_y":.52}
                                user_font_size:"24sp"
                                theme_text_color: "Custom"
                                text_color:[71/200,73/200,82/200,2]
                                tooltip_text: "Instagram"
                                tooltip_bg_color:[71/200,73/200,82/200,2]
                                on_release: app.insta()

                            TooltipMDIconButton:
                                id: f
                                icon: "facebook"
                                pos_hint: {"center_x":.55,"center_y":.52}
                                user_font_size:"24sp"                                
                                theme_text_color: "Custom"
                                text_color:[71/200,73/200,82/200,2]
                                tooltip_text: "Facebook"
                                tooltip_bg_color:[71/200,73/200,82/200,2]
                                on_release: app.face()                                                  

                            TooltipMDIconButton:
                                id: r
                                icon: "arrow-right-circle"
                                pos_hint: {"center_x":.9,"center_y":.52}
                                tooltip_text: "Deslize imagem a direita"
                                tooltip_bg_color: [71/200,73/200,82/200,2]
                                user_font_size:"23sp"   
                                theme_text_color: "Custom"
                                text_color:1,1,1,1
                                on_release: app.direita()

                            FloatLayout:
                                MDCard:
                                    size_hint: .9, 0.28
                                    md_bg_color:[128/255,128/255,128/255,1]
                                    pos_hint: {"center_x":.5,"center_y":.32} 
                                    orientation: 'vertical' 

                                MDIconButton:
                                    id:fgbbb                                
                                    icon: "star-outline"
                                    user_font_size: "26dp"
                                    theme_text_color:"Custom"
                                    text_color: 1,1,1,1
                                    pos_hint: {"center_x":0.3,"center_y":.40}
                                    on_release: app.rotoo()

                                MDIconButton:
                                    id: fggg
                                    icon: "star-outline"
                                    user_font_size: "26dp"
                                    theme_text_color:"Custom"
                                    text_color: 1,1,1,1
                                    pos_hint: {"center_x":0.5,"center_y":.40}
                                    on_release: app.rotoo()

                                MDIconButton:
                                    id: fgaaa
                                    icon: "star-outline"
                                    user_font_size: "26dp"
                                    theme_text_color:"Custom"
                                    text_color: 1,1,1,1
                                    pos_hint: {"center_x":0.7,"center_y":.40}
                                    on_release: app.rotoo()

                                MDLabel:
                                    text: "3 000kz /dia"
                                    theme_text_color: "Custom" 
                                    bold: True
                                    font_size: 16
                                    text_color:1,1,1,1
                                    pos_hint: {"center_x":0.6,"center_y":.29}

                                MDLabel:
                                    text: "Toyota 2020 Manual"
                                    theme_text_color: "Custom" 
                                    font_size: 14
                                    text_color: 1,1,1,1
                                    pos_hint: {"center_x":0.6,"center_y":.23}

                            MDFillRoundFlatIconButton:
                                id: botta
                                size: 45,35
                                icon: "car-multiple"
                                text: "Frotas Veiculos"  
                                theme_text_color: "Custom"
                                text_color:1,1,1,1
                                font_style: "Subtitle1"
                                line_color: [71/200,73/200,82/200,2]
                                icon_color: 1, 0, 0, 1
                                pos_hint: {"center_x":.5,"center_y":0.1}
                                on_press:
                                    screen_manager.current = "screen2"                                

                        MDFloatLayout:
                            md_bg_color: 1,1,1, .2

                            MDCard:                             
                                size_hint: .9, 0.67
                                height:30
                                pos_hint: {"center_x":.5,"center_y":.63}
                                radius: [10,10,8,8]
                                                            
                                orientation: 'vertical'

                                MDLabel:
                                    text:"Alugue qualquer veiculo                                       sem sair de casa!"
                                    theme_text_color: "Custom"
                                    font_style: "Caption"
                                    bold: True
                                    text_color: [71/200,73/200,82/200,2] 
                                    size_hint_y: None
                                    font_size: 15
                                    height: self.texture_size[1] 
                                    pos_hint: {"center_x":.53} 

                                Image:
                                    id: card67
                                    source: "Imagens/plo.png"                                 
                                    pos_hint: {"center_x":.5,"center_y":.8} 

                                MDGridLayout:
                                    cols: 3
                                    adaptive_height: True         

                            TooltipMDIconButton:
                                id: lefo
                                icon: "arrow-left-circle"
                                pos_hint: {"center_x":.1,"center_y":.52}
                                tooltip_text: "Deslize imagem a esquerda"
                                tooltip_bg_color: [71/200,73/200,82/200,2]
                                user_font_size:"23sp"   
                                theme_text_color: "Custom"
                                text_color:1,1,1,1
                                on_release: app.esquerda()
                            
                            TooltipMDIconButton:

                                id: ins
                                icon: "instagram"
                                pos_hint: {"center_x":.44,"center_y":.52}
                                user_font_size:"24sp"
                                theme_text_color: "Custom"
                                text_color:[71/200,73/200,82/200,2]
                                tooltip_text: "Instagram"
                                tooltip_bg_color:[71/200,73/200,82/200,2]
                                on_release: app.insta()

                            TooltipMDIconButton:
                                id: fac
                                icon: "facebook"
                                pos_hint: {"center_x":.55,"center_y":.52}
                                user_font_size:"24sp"                                
                                theme_text_color: "Custom"
                                text_color:[71/200,73/200,82/200,2]
                                tooltip_text: "Facebook"
                                tooltip_bg_color:[71/200,73/200,82/200,2]
                                on_release: app.face()

                            FloatLayout:
                                MDCard:
                                    size_hint: .9, 0.28
                                    md_bg_color:[128/255,128/255,128/255,1]
                                    pos_hint: {"center_x":.5,"center_y":.32} 
                                    orientation: 'vertical' 
                                
                                MDIconButton:
                                    id:fgbbbb                                
                                    icon: "star-outline"
                                    user_font_size: "26dp"
                                    theme_text_color:"Custom"
                                    text_color: 1,1,1,1
                                    pos_hint: {"center_x":0.3,"center_y":.40}
                                    on_release: app.rotooo()

                                MDIconButton:
                                    id: fgggg
                                    icon: "star-outline"
                                    user_font_size: "26dp"
                                    theme_text_color:"Custom"
                                    text_color: 1,1,1,1
                                    pos_hint: {"center_x":0.5,"center_y":.40}
                                    on_release: app.rotooo()

                                MDIconButton:
                                    id: fgaaaa
                                    icon: "star-outline"
                                    user_font_size: "26dp"
                                    theme_text_color:"Custom"
                                    text_color: 1,1,1,1
                                    pos_hint: {"center_x":0.7,"center_y":.40}
                                    on_release: app.rotooo()
                                    
                                MDLabel:
                                    text: "8 000kz /dia"
                                    theme_text_color: "Custom" 
                                    bold: True
                                    font_size: 16
                                    text_color:1,1,1,1
                                    pos_hint: {"center_x":0.6,"center_y":.29}

                                MDLabel:
                                    text: "Mercedes 2019 Automático"
                                    theme_text_color: "Custom" 
                                    font_size: 14
                                    text_color: 1,1,1,1
                                    pos_hint: {"center_x":0.6,"center_y":.23}

                            MDFillRoundFlatIconButton:
                                id: botar
                                size: 45,35
                                icon: "car-multiple"
                                text: "Frotas Veiculos"  
                                theme_text_color: "Custom"
                                text_color:1,1,1,1
                                font_style: "Subtitle1"
                                line_color: [71/200,73/200,82/200,2]
                                icon_color: 1, 0, 0, 1
                                pos_hint: {"center_x":.5,"center_y":0.1}
                                on_press:
                                    screen_manager.current = "screen2"                               

                    MDToolbar:                                          
                        icon: 'access-point'
                        mode: "end"
                        #type: "bottom"
                        radius: [20,20,0,0] 
                        height: 45

                        MDLabel:
                            id: lo
                            text: "   "  
                                                            
                        TooltipMDIconButton:
                            id: lei
                            icon: "help-circle"
                            theme_text_color: "Custom"
                            text_color: 1,1,1,1
                            user_font_size:"25sp" 
                            tooltip_text: "Quem Somos?"
                            tooltip_text_color: 1,1,1,1
                            tooltip_bg_color: [71/200,73/200,82/200,2]                            
                            pos_hint: {"center_x":0.2, "center_y":0.5}
                            on_release: app.icoo()                            
 
                        MDIconButton:
                            id: lop
                            icon: "car-info"
                            pos_hint: {"center_x":.1,"center_y":0.5}
                            user_font_size:"24sp" 
                            theme_text_color: "Custom"                           
                            text_color:[71/200,73/200,82/200,2]  
                            on_release: app.show_bottom_sheet()

                        MDLabel:
                            id: lo
                            text: "Sobre Rent!"
                            font_style: "Subtitle1" 
                            theme_text_color: "Custom"
                            text_color:1,1,1,1
                            font_size: 15                          
                            pos_hint: {"center_x":.3,"center_y":0.5}      
                                                                                         
            Screen:
                name: "screen1"
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '5dp' 

                    MDToolbar:
                        title: 'Cliente'
                        elevation: 1
                        left_action_items: [["shield-account",lambda x: None]]                         
                        height: 38

                        TooltipMDIconButton:
                            icon: "close-circle"
                            theme_text_color: "Custom"
                            text_color: 1,1,1,1
                            user_font_size:"24sp" 
                            tooltip_bg_color: [71/200,73/200,82/200,2]   
                            tooltip_text:"Fechar"                         
                            pos_hint: {"center_x":0.2, "center_y":0.5}       
                            on_release: screen_manager.current = "menu"   

                    MDFloatLayout:       

                        MDCard:                               
                            size_hint: 0.9, 0.85
                            radius: [10,10,15,15]
                            orientation: 'vertical'
                            spacing: '8dp'
                            padding: '10dp'
                            pos_hint: {"center_x":.5,"center_y":.5}

                        MDIconButton:
                            id: icoi                               
                            icon: "account-circle"
                            user_font_size:"37sp" 
                            theme_text_color: "Custom"
                            text_color:[71/200,73/200,82/200,2] 
                            pos_hint: {"center_x":.5,"center_y":.93}

                        MDTextField:
                            id: nome
                            hint_text: "Insira o seu nome...."
                            icon_left: "account-edit"
                            icon_left_color:1,1,1,1
                            size_hint_x:.75
                            size_hint_y: None
                            font_size: 15
                            hint_text_color:  1,1,1,1
                            cursor_color: 1,1,1,1
                            pos_hint: {"center_x":.5,"center_y":.78}

                        MDIconButton:
                            icon: "account-edit"
                            theme_text_color: "Custom" 
                            text_color: [71/200,73/200,82/200,2]
                            pos_hint: {"center_x":.85,"center_y":.79}       

                        MDTextField:
                            id: age
                            hint_text: "Idade.."
                            size_hint_x:.75
                            size_hint_y: None
                            font_size: 15
                            max_text_length: 3                           
                            hint_text_color:  1,1,1,1
                            cursor_color: 1,1,1,1
                           # on_focus: if self.focus:app.icoo()
                            pos_hint: {"center_x":.5,"center_y":.68}

                        MDIconButton:
                            icon: "account"
                            theme_text_color: "Custom" 
                            text_color: [71/200,73/200,82/200,2]
                            pos_hint: {"center_x":.85,"center_y":.69}   

                        MDTextField:
                            id: tele
                            hint_text: "Telefone +244"
                            size_hint_x:.75
                            size_hint_y: None
                            font_size: 15
                            max_text_length: 9  
                            hint_text_color:  1,1,1,1
                            cursor_color: 1,1,1,1
                            pos_hint: {"center_x":.5,"center_y":.58}

                        MDIconButton:
                            icon: "phone"
                            theme_text_color: "Custom" 
                            text_color: [71/200,73/200,82/200,2]
                            pos_hint: {"center_x":.85,"center_y":.59}   

                        MDTextField:
                            id: email
                            hint_text: "Email"
                            size_hint_x:.75
                            size_hint_y: None
                            font_size: 15
                            hint_text_color:  1,1,1,1
                            cursor_color: 1,1,1,1
                            pos_hint: {"center_x":.5,"center_y":.48}

                        MDIconButton:
                            icon: "email-edit"
                            theme_text_color: "Custom" 
                            text_color: [71/200,73/200,82/200,2]
                            pos_hint: {"center_x":.85,"center_y":.49}   

                        MDTextField:
                            id: pais
                            hint_text: "Pais"
                            size_hint_x:.75
                            size_hint_y: None
                            font_size: 15
                            hint_text_color:  1,1,1,1
                            cursor_color: 1,1,1,1
                            pos_hint: {"center_x":.5,"center_y":.38}

                        MDIconButton:
                            icon: "home-account"
                            theme_text_color: "Custom" 
                            text_color: [71/200,73/200,82/200,2]
                            pos_hint: {"center_x":.85,"center_y":.39}                               
                        
                        MDTextField:
                            id: morada
                            hint_text: "Endereço"
                            size_hint_x:.75
                            size_hint_y: None
                            font_size: 15
                            hint_text_color:  1,1,1,1
                            cursor_color: 1,1,1,1
                            pos_hint: {"center_x":.5,"center_y":.28}

                        MDIconButton:
                            icon: "home-edit"
                            theme_text_color: "Custom" 
                            text_color: [71/200,73/200,82/200,2]
                            pos_hint: {"center_x":.85,"center_y":.29}   

                        MDRoundFlatIconButton:
                            text: "Guardar Dados"
                            icon: "content-save-move"
                            user_font_size: "26dp"
                            pos_hint: {"center_x":.50,"center_y":.18}
                            on_release: app.guardar()

            Screen:
                name: "screen2"
                BoxLayout:
                    orientation: "vertical"
                    MDToolbar:
                        title: 'Rentcar'
                        elevation: 10
                        left_action_items: [["shield-car",lambda x: None]]                        
                        height: 38

                        TooltipMDIconButton:
                            id:cli
                            icon: "clipboard-text-search"
                            theme_text_color: "Custom"
                            text_color: 1,1,1,1
                            user_font_size:"23sp" 
                            tooltip_bg_color: [71/200,73/200,82/200,2]                            
                            pos_hint: {"center_x":0.1, "center_y":0.5}  
                            tooltip_text:"Consultar"     
                            on_release: 
                                screen_manager.current = "screen3"
                                app.star_second()
                                app.tree_janela()

                        TooltipMDIconButton:
                            icon: "close-circle"
                            theme_text_color: "Custom"
                            text_color: 1,1,1,1
                            user_font_size:"23sp" 
                            tooltip_bg_color: [71/200,73/200,82/200,2] 
                            tooltip_text: "Fechar"                           
                            pos_hint: {"center_x":0.2, "center_y":0.5}       
                            on_release: screen_manager.current = "menu"                       
                    MDTabs:
                        id: log
                        Tab:
                            text: "Veiculos Ligeiros"
                            background_color:[0/255,128/255,128/255,1]
                            ScrollView:
                                MDList:
                                    CardItem:
                                        MDCard:
                                            size_hint_y: None
                                            height: 125
                                            spacing: "10dp"
                                            padding: "8dp"
                                            elevation:1
                                            focus_behavior: True
                                            ripple_behavior: True

                                            Widget:
                                                size_hint_x:.9

                                            MDBoxLayout:
                                                orientation: "vertical"
                                                
                                                MDLabel:
                                                    text: "Suzuki"       
                                                    bold: True
                                                    font_sytle: "H6"
                                                    theme_text_color: "Custom"
                                                    font_size: 16
                                                    text_color: [128/255,128/255,128/255,1]
                                                    adaptive_hight: True                                                  
                                                    
                                                MDLabel:
                                                    text: "Preto"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True
                                                                                                                                                                        
                                                MDLabel:
                                                    text: "Automático"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True
                                                    
                                                MDLabel:
                                                    text: "Gasolina"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True  
                                                    
                                                MDLabel:
                                                    text: "Jimmy Sierra/2020"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True                                                                                        

                                        MDRelativeLayout:
                                            md_bg_color: [0/255,128/255,128/255,1]
                                            radius: [10,10,10,10]
                                            size_hint_y: None
                                            #height: root.height - dp(24)  
                                            x: STANDARD_INCREMENT *2 - root.width - STANDARD_INCREMENT 
                                            y: dp(10)
                                            Image:
                                                source:"Imagens/suz.png"
                                                size_hint_x:None
                                                width:STANDARD_INCREMENT *2
                                                x: root.width - self.width + STANDARD_INCREMENT

                                    CardItem:
                                        MDCard:
                                            size_hint_y: None
                                            height: 125
                                            spacing: "12dp"
                                            focus_behavior: True
                                            ripple_behavior: True
                                            elevation:0

                                            Widget:
                                                size_hint_x:.9

                                            MDBoxLayout:
                                                orientation: "vertical"
                                                MDLabel:
                                                    text: ""       
                                                    bold: True
                                                    font_sytle: "H6"
                                                    theme_text_color: "Custom"
                                                    font_size: 16
                                                    text_color: [128/255,128/255,128/255,1]
                                                    adaptive_hight: True
                                                MDLabel:
                                                    text: "Ranger Rover"       
                                                    bold: True
                                                    font_sytle: "H6"
                                                    theme_text_color: "Custom"
                                                    font_size: 16
                                                    text_color: [128/255,128/255,128/255,1]
                                                    adaptive_hight: True                                                  
                                                    
                                                MDLabel:
                                                    text: "Branco"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True
                                                                                                                                                                        
                                                MDLabel:
                                                    text: "Manual"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True
                                                    
                                                MDLabel:
                                                    text: "Gasóleo"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True  
                                                    
                                                MDLabel:
                                                    text: "revoque 2.0/2019"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True                                                                                        

                                        MDRelativeLayout:
                                            md_bg_color: [0/255,128/255,128/255,1]
                                            radius: [10,10,10,10]
                                            size_hint_y: None
                                            #height: root.height - dp(24)  
                                            x: STANDARD_INCREMENT *2 - root.width - STANDARD_INCREMENT 
                                            y: dp(10)
                                            Image:
                                                source:"Imagens/ran.png"
                                                size_hint_x:None
                                                width:STANDARD_INCREMENT *2
                                                x: root.width - self.width + STANDARD_INCREMENT
                                    CardItem:
                                        MDCard:
                                            size_hint_y: None
                                            height: 125
                                            spacing: "12dp"
                                            focus_behavior: True
                                            ripple_behavior: True
                                            elevation:0

                                            Widget:
                                                size_hint_x:.9

                                            MDBoxLayout:
                                                orientation: "vertical"
                                                MDLabel:
                                                    text: ""       
                                                    bold: True
                                                    font_sytle: "H6"
                                                    theme_text_color: "Custom"
                                                    font_size: 16
                                                    text_color: [128/255,128/255,128/255,1]
                                                    adaptive_hight: True
                                                MDLabel:
                                                    text: "Suzuki"       
                                                    bold: True
                                                    font_sytle: "H6"
                                                    theme_text_color: "Custom"
                                                    font_size: 16
                                                    text_color: [128/255,128/255,128/255,1]
                                                    adaptive_hight: True                                                  
                                                    
                                                MDLabel:
                                                    text: "Vermelho"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True
                                                                                                                                                                        
                                                MDLabel:
                                                    text: "Automático"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True
                                                    
                                                MDLabel:
                                                    text: "Gasolina"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True  
                                                    
                                                MDLabel:
                                                    text: "Capournd/2018"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True 

                                        MDRelativeLayout:
                                            md_bg_color: [0/255,128/255,128/255,1]
                                            radius: [10,10,10,10]
                                            size_hint_y: None
                                            #height: root.height - dp(24)  
                                            x: STANDARD_INCREMENT *2 - root.width - STANDARD_INCREMENT 
                                            y: dp(10)
                                            Image:
                                                source:"Imagens/suzi.png"
                                                size_hint_x:None
                                                width:STANDARD_INCREMENT *2
                                                x: root.width - self.width + STANDARD_INCREMENT
                                                
                                    CardItem:
                                        MDCard:
                                            size_hint_y: None
                                            height: 125
                                            spacing: "12dp"
                                            focus_behavior: True
                                            ripple_behavior: True
                                            elevation:0
                                            
                                            Widget:
                                                size_hint_x:.9

                                            MDBoxLayout:
                                                orientation: "vertical"
                                                MDLabel:
                                                    text: ""       
                                                    bold: True
                                                    font_sytle: "H6"
                                                    theme_text_color: "Custom"
                                                    font_size: 16
                                                    text_color: [128/255,128/255,128/255,1]
                                                    adaptive_hight: True
                                                MDLabel:
                                                    text: "Jeep"       
                                                    bold: True
                                                    font_sytle: "H6"
                                                    theme_text_color: "Custom"
                                                    font_size: 16
                                                    text_color: [128/255,128/255,128/255,1]
                                                    adaptive_hight: True                                                  
                                                    
                                                MDLabel:
                                                    text: "Branco"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True
                                                                                                                                                                        
                                                MDLabel:
                                                    text: "Manual"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True
                                                    
                                                MDLabel:
                                                    text: "Gasolina"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True  
                                                    
                                                MDLabel:
                                                    text: "Compass/2017"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True 

                                        MDRelativeLayout:
                                            md_bg_color: [0/255,128/255,128/255,1]
                                            radius: [10,10,10,10]
                                            size_hint_y: None
                                            #height: root.height - dp(24)  
                                            x: STANDARD_INCREMENT *2 - root.width - STANDARD_INCREMENT 
                                            y: dp(10)
                                            Image:
                                                source:"Imagens/kia.png"
                                                size_hint_x:None
                                                width:STANDARD_INCREMENT *2
                                                x: root.width - self.width + STANDARD_INCREMENT

                                    CardItem:
                                        MDCard:
                                            size_hint_y: None
                                            height: 125
                                            spacing: "12dp"
                                            focus_behavior: True
                                            ripple_behavior: True
                                            elevation:0

                                            Widget:
                                                size_hint_x:.9

                                            MDBoxLayout:
                                                orientation: "vertical"
                                                MDLabel:
                                                    text: ""       
                                                    bold: True
                                                    font_sytle: "H6"
                                                    theme_text_color: "Custom"
                                                    font_size: 16
                                                    text_color: [128/255,128/255,128/255,1]
                                                    adaptive_hight: True
                                                MDLabel:
                                                    text: "Mercedes"       
                                                    bold: True
                                                    font_sytle: "H6"
                                                    theme_text_color: "Custom"
                                                    font_size: 16
                                                    text_color: [128/255,128/255,128/255,1]
                                                    adaptive_hight: True                                                  
                                                    
                                                MDLabel:
                                                    text: "Branco"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True
                                                                                                                                                                        
                                                MDLabel:
                                                    text: "Manual"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True
                                                    
                                                MDLabel:
                                                    text: "Gasoleo"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True  
                                                    
                                                MDLabel:
                                                    text: "Ilux/2016"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True 

                                        MDRelativeLayout:
                                            md_bg_color: [0/255,128/255,128/255,1]
                                            radius: [10,10,10,10]
                                            size_hint_y: None
                                            #height: root.height - dp(24)  
                                            x: STANDARD_INCREMENT *2 - root.width - STANDARD_INCREMENT 
                                            y: dp(10)
                                            Image:
                                                source:"Imagens/mer.png"
                                                size_hint_x:None
                                                width:STANDARD_INCREMENT *2
                                                x: root.width - self.width + STANDARD_INCREMENT                                                      
  
                                    CardItem:
                                        MDCard:
                                            size_hint_y: None
                                            height: 125
                                            spacing: "12dp"
                                            focus_behavior: True
                                            ripple_behavior: True
                                            elevation:0
                                            
                                            Widget:
                                                size_hint_x:.9

                                            MDBoxLayout:
                                                orientation: "vertical"
                                                MDLabel:
                                                    text: ""       
                                                    bold: True
                                                    font_sytle: "H6"
                                                    theme_text_color: "Custom"
                                                    font_size: 16
                                                    text_color: [128/255,128/255,128/255,1]
                                                    adaptive_hight: True
                                                MDLabel:
                                                    text: "Wolskgan"       
                                                    bold: True
                                                    font_sytle: "H6"
                                                    theme_text_color: "Custom"
                                                    font_size: 16
                                                    text_color: [128/255,128/255,128/255,1]
                                                    adaptive_hight: True                                                  
                                                    
                                                MDLabel:
                                                    text: "Castanho"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True
                                                                                                                                                                        
                                                MDLabel:
                                                    text: "Automatico"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True
                                                    
                                                MDLabel:
                                                    text: "Gasolina"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True  
                                                    
                                                MDLabel:
                                                    text: "T-Cross/2020"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True 

                                        MDRelativeLayout:
                                            md_bg_color: [0/255,128/255,128/255,1]
                                            radius: [10,10,10,10]
                                            size_hint_y: None
                                            #height: root.height - dp(24)  
                                            x: STANDARD_INCREMENT *2 - root.width - STANDARD_INCREMENT 
                                            y: dp(10)
                                            Image:
                                                source:"Imagens/branco.png"
                                                size_hint_x:None
                                                width:STANDARD_INCREMENT *2
                                                x: root.width - self.width + STANDARD_INCREMENT

                                    CardItem:
                                        MDCard:
                                            size_hint_y: None
                                            height: 125
                                            spacing: "12dp"
                                            focus_behavior: True
                                            ripple_behavior: True
                                            elevation:0
                                            
                                            Widget:
                                                size_hint_x:.9

                                            MDBoxLayout:
                                                orientation: "vertical"

                                                MDLabel:
                                                    text: ""       
                                                    bold: True
                                                    font_sytle: "H6"
                                                    theme_text_color: "Custom"
                                                    font_size: 16
                                                    text_color: [128/255,128/255,128/255,1]
                                                    adaptive_hight: True
                                                    
                                                MDLabel:
                                                    text: "Jeep"       
                                                    bold: True
                                                    font_sytle: "H6"
                                                    theme_text_color: "Custom"
                                                    font_size: 16
                                                    text_color: [128/255,128/255,128/255,1]
                                                    adaptive_hight: True                                                  
                                                    
                                                MDLabel:
                                                    text: "Branco"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True
                                                                                                                                                                        
                                                MDLabel:
                                                    text: "Manual"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True
                                                    
                                                MDLabel:
                                                    text: "Gasolina"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True  
                                                    
                                                MDLabel:
                                                    text: "Wrangler/2016"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True 

                                        MDRelativeLayout:
                                            md_bg_color: [0/255,128/255,128/255,1]
                                            radius: [10,10,10,10]
                                            size_hint_y: None
                                            #height: root.height - dp(24)  
                                            x: STANDARD_INCREMENT *2 - root.width - STANDARD_INCREMENT 
                                            y: dp(10)
                                            Image:
                                                source:"Imagens/jeep1.png"
                                                size_hint_x:None
                                                width:STANDARD_INCREMENT *2
                                                x: root.width - self.width + STANDARD_INCREMENT
                                                                                                                         
                        Tab:
                            text: "Veiculos Pesados"  
                            background_color:[0/255,128/255,128/255,1]
                            ScrollView:
                                MDList:
                                    CardItem:
                                        MDCard:
                                            size_hint_y: None
                                            height: 125
                                            spacing: "10dp"
                                            padding: "8dp"
                                            focus_behavior: True
                                            ripple_behavior: True                                            
                                            elevation:1
                                            
                                            Widget:
                                                size_hint_x:.9

                                            MDBoxLayout:
                                                orientation: "vertical"
                                                
                                                MDLabel:
                                                    text: "Toyota"       
                                                    bold: True
                                                    font_sytle: "H6"
                                                    theme_text_color: "Custom"
                                                    font_size: 16
                                                    text_color: [128/255,128/255,128/255,1]
                                                    adaptive_hight: True                                                  
                                                    
                                                MDLabel:
                                                    text: "Branco"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True
                                                                                                                                                                        
                                                MDLabel:
                                                    text: "Automático"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True
                                                    
                                                MDLabel:
                                                    text: "Gasoleo"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True  
                                                    
                                                MDLabel:
                                                    text: "Coaster/2020"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True                                                                                        

                                        MDRelativeLayout:
                                            md_bg_color: [0/255,128/255,128/255,1]
                                            radius: [10,10,10,10]
                                            size_hint_y: None
                                            #height: root.height - dp(24)  
                                            x: STANDARD_INCREMENT *2 - root.width - STANDARD_INCREMENT 
                                            y: dp(10)
                                            Image:
                                                source:"Imagens/toyo.png"
                                                size_hint_x:None
                                                width:STANDARD_INCREMENT *2
                                                x: root.width - self.width + STANDARD_INCREMENT

                                    CardItem:
                                        MDCard:
                                            size_hint_y: None
                                            height: 125
                                            spacing: "12dp"
                                            focus_behavior: True
                                            ripple_behavior: True
                                            elevation:1
                                            
                                            Widget:
                                                size_hint_x:.9

                                            MDBoxLayout:
                                                orientation: "vertical"
                                                MDLabel:
                                                    text: ""       
                                                    bold: True
                                                    font_sytle: "H6"
                                                    theme_text_color: "Custom"
                                                    font_size: 16
                                                    text_color: [128/255,128/255,128/255,1]
                                                    adaptive_hight: True
                                                MDLabel:
                                                    text: "Mercedes"       
                                                    bold: True
                                                    font_sytle: "H6"
                                                    theme_text_color: "Custom"
                                                    font_size: 16
                                                    text_color: [128/255,128/255,128/255,1]
                                                    adaptive_hight: True                                                  
                                                    
                                                MDLabel:
                                                    text: "Branco"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True
                                                                                                                                                                        
                                                MDLabel:
                                                    text: "Automático"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True
                                                    
                                                MDLabel:
                                                    text: "Gasolina"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True  
                                                    
                                                MDLabel:
                                                    text: "Benz/2020"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True 

                                        MDRelativeLayout:
                                            md_bg_color: [0/255,128/255,128/255,1]
                                            radius: [10,10,10,10]
                                            size_hint_y: None
                                            #height: root.height - dp(24)  
                                            x: STANDARD_INCREMENT *2 - root.width - STANDARD_INCREMENT 
                                            y: dp(10)
                                            Image:
                                                source:"Imagens/merc.png"
                                                size_hint_x:None
                                                width:STANDARD_INCREMENT *2
                                                x: root.width - self.width + STANDARD_INCREMENT                                                

                                    CardItem:
                                        MDCard:
                                            size_hint_y: None
                                            height: 125
                                            spacing: "12dp"
                                            focus_behavior: True
                                            ripple_behavior: True
                                            elevation:1
                                            
                                            Widget:
                                                size_hint_x:.9

                                            MDBoxLayout:
                                                orientation: "vertical"
                                                MDLabel:
                                                    text: ""       
                                                    bold: True
                                                    font_sytle: "H6"
                                                    theme_text_color: "Custom"
                                                    font_size: 16
                                                    text_color: [128/255,128/255,128/255,1]
                                                    adaptive_hight: True
                                                MDLabel:
                                                    text: "Toyota"       
                                                    bold: True
                                                    font_sytle: "H6"
                                                    theme_text_color: "Custom"
                                                    font_size: 16
                                                    text_color: [128/255,128/255,128/255,1]
                                                    adaptive_hight: True                                                  
                                                    
                                                MDLabel:
                                                    text: "Cinza"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True
                                                                                                                                                                        
                                                MDLabel:
                                                    text: "Automático"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True
                                                    
                                                MDLabel:
                                                    text: "Gasolina"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True  
                                                    
                                                MDLabel:
                                                    text: "Hiace/2018"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True                                                                                        

                                        MDRelativeLayout:
                                            md_bg_color: [0/255,128/255,128/255,1]
                                            radius: [10,10,10,10]
                                            size_hint_y: None
                                            #height: root.height - dp(24)  
                                            x: STANDARD_INCREMENT *2 - root.width - STANDARD_INCREMENT 
                                            y: dp(10)
                                            Image:
                                                source:"Imagens/toyohia.png"
                                                size_hint_x:None
                                                width:STANDARD_INCREMENT *2
                                                x: root.width - self.width + STANDARD_INCREMENT

                                    CardItem:
                                        MDCard:
                                            size_hint_y: None
                                            height: 125
                                            spacing: "12dp"
                                            focus_behavior: True
                                            ripple_behavior: True
                                            elevation: 1
                                            
                                            Widget:
                                                size_hint_x:.9

                                            MDBoxLayout:
                                                orientation: "vertical"
                                                MDLabel:
                                                    text: ""       
                                                    bold: True
                                                    font_sytle: "H6"
                                                    theme_text_color: "Custom"
                                                    font_size: 16
                                                    text_color: [128/255,128/255,128/255,1]
                                                    adaptive_hight: True
                                                MDLabel:
                                                    text: "Toyota"       
                                                    bold: True
                                                    font_sytle: "H6"
                                                    theme_text_color: "Custom"
                                                    font_size: 16
                                                    text_color: [128/255,128/255,128/255,1]
                                                    adaptive_hight: True                                                  
                                                    
                                                MDLabel:
                                                    text: "Branco"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True
                                                                                                                                                                        
                                                MDLabel:
                                                    text: "Automático"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True
                                                    
                                                MDLabel:
                                                    text: "Gasoleo"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True  
                                                    
                                                MDLabel:
                                                    text: "Hiace/2015"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True 

                                        MDRelativeLayout:
                                            md_bg_color: [0/255,128/255,128/255,1]
                                            radius: [10,10,10,10]
                                            size_hint_y: None
                                            #height: root.height - dp(24)  
                                            x: STANDARD_INCREMENT *2 - root.width - STANDARD_INCREMENT 
                                            y: dp(10)
                                            Image:
                                                source:"Imagens/tor.png"
                                                size_hint_x:None
                                                width:STANDARD_INCREMENT *2
                                                x: root.width - self.width + STANDARD_INCREMENT                                                       
  
                                    CardItem:
                                        MDCard:
                                            size_hint_y: None
                                            height: 125
                                            spacing: "12dp"
                                            focus_behavior: True
                                            ripple_behavior: True
                                            elevation: 1
                                            
                                            Widget:
                                                size_hint_x:.9

                                            MDBoxLayout:
                                                orientation: "vertical"
                                                MDLabel:
                                                    text: ""       
                                                    bold: True
                                                    font_sytle: "H6"
                                                    theme_text_color: "Custom"
                                                    font_size: 16
                                                    text_color: [128/255,128/255,128/255,1]
                                                    adaptive_hight: True
                                                MDLabel:
                                                    text: "Toyota"       
                                                    bold: True
                                                    font_sytle: "H6"
                                                    theme_text_color: "Custom"
                                                    font_size: 16
                                                    text_color: [128/255,128/255,128/255,1]
                                                    adaptive_hight: True                                                  
                                                    
                                                MDLabel:
                                                    text: "Cinza"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True
                                                                                                                                                                        
                                                MDLabel:
                                                    text: "Manual"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True
                                                    
                                                MDLabel:
                                                    text: "Gasoleo"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True  
                                                    
                                                MDLabel:
                                                    text: "Hiace/2016"       
                                                    font_sytle: "Caption"
                                                    theme_text_color: "Hint"
                                                    font_size: 14
                                                    adaptive_hight: True 

                                        MDRelativeLayout:
                                            md_bg_color: [0/255,128/255,128/255,1]
                                            radius: [10,10,10,10]
                                            size_hint_y: None
                                            #height: root.height - dp(24)  
                                            x: STANDARD_INCREMENT *2 - root.width - STANDARD_INCREMENT 
                                            y: dp(10)
                                            Image:
                                                source:"Imagens/topl.png"
                                                size_hint_x:None
                                                width:STANDARD_INCREMENT *2
                                                x: root.width - self.width + STANDARD_INCREMENT
 
            Screen:
                name: "screen3"
                BoxLayout: 
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Rentcar'
                        elevation: 10
                        left_action_items: [["shield-car",lambda x: None]]                        
                        height: 38           

                        TooltipMDIconButton:
                            id: act
                            icon: "update"
                            theme_text_color: "Custom"
                            text_color: 1,1,1,1
                            user_font_size: "24sp"    
                            tooltip_text: "Actualizar"                          
                            pos_hint: {"center_x":0.1, "center_y":0.5}       
                            on_release: 
                                app.star_second()
                                app.tree_janela()                                                           

                        TooltipMDIconButton:
                            icon: "close-circle"
                            theme_text_color: "Custom"
                            text_color: 1,1,1,1
                            user_font_size:"24sp"    
                            tooltip_text: "Fechar"                        
                            pos_hint: {"center_x":0.2, "center_y":0.5}       
                            on_release: screen_manager.current = "screen2"        

                    MDTabs:
                        Tab:
                            icon: "close-circle"
                            text: "Veiculos Dísponiveis"
                            FloatLayout:     
                                MDCard:
                                    id: veiculoe
                                    size_hint: .98, 0.87
                                    radius:[18,18,18,18]         
                                    pos_hint: {'center_x':0.5,'center_y':.54} 

                                MDFillRoundFlatIconButton:
                                    id: nm
                                    text: "Efectuar Pedido"
                                    icon: "clipboard-edit"
                                    pos_hint: {"center_x":.5,"center_y":.1}     
                                    on_release: 
                                        screen_manager.current = "screen7"     
                        Tab:
                            text: "Taxas Pagamento"    
                            FloatLayout:   
                                MDCard:
                                    id: tax
                                    size_hint: .98, 0.87
                                    radius:[18,18,18,18]        
                                    pos_hint: {'center_x':0.5,'center_y':.54} 

                                MDFillRoundFlatIconButton:
                                    id: nm
                                    text: "Efectuar Pedido"
                                    icon: "clipboard-edit"
                                    pos_hint: {"center_x":.5,"center_y":.1}     
                                    on_release: 
                                        screen_manager.current = "screen7"     
         
            Screen:
                name: "screen7"
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '5dp'
                    MDTabs:
                        Tab:
                            text:"Efectuar Pedido"         
                        FloatLayout:
                            padding:'4dp'
                            spacing:'4dp'

                            TooltipMDIconButton:
                                icon: "close-circle"
                                user_font_size: "24sp"
                                theme_text_color: "Custom"
                                text_color: 1,1,1,1
                                tooltip_text: "Sair"
                                pos_hint: {"center_x":.88,"center_y":.95}  
                                on_release: app.stop()

                            MDIconButton:
                                icon: "arrow-left"
                                user_font_size: "24sp"
                                theme_text_color: "Custom"
                                text_color: 1,1,1,1
                                pos_hint: {"center_x":.1,"center_y":.95}   
                                on_release: screen_manager.current = "screen3"                               

                            MDTextField:
                                id: nome1
                                hint_text: "Insira o seu email"
                                icon_right: "email"
                                icon_right_color:self.theme_cls.primary_color                              
                                size_hint_x: .80
                                font_size: 14
                                pos_hint: {"center_x":.5,"center_y":.83}  

                            MDTextField:
                                id: marca
                                hint_text: "Marca"
                                size_hint_x: .80
                                font_size: 14
                                icon_right: "car-back"
                                icon_right_color:self.theme_cls.primary_color                                     
                                pos_hint: {"center_x":.5,"center_y":.74}                       

                            MDTextField:
                                id: modelo
                                hint_text: "Modelo"
                                size_hint_x: .40
                                font_size: 14
                                icon_right: "car-multiple"
                                icon_right_color:self.theme_cls.primary_color                                  
                                pos_hint: {"center_x":.3,"center_y":.65}                      

                            MDTextField:
                                id: cor
                                hint_text: "Cor"
                                size_hint_x: .33
                                font_size: 14
                                icon_right: "format-color-highlight"
                                icon_right_color:self.theme_cls.primary_color                                  
                                pos_hint: {"center_x":.74,"center_y":.65}
                                
                            MDTextField: 
                                id: yt
                                hint_text: "Data de Aluguel"
                                size_hint_x: .80
                                font_size: 14
                                disabled: True
                                pos_hint: {"center_x":.5,"center_y":.56}   

                            MDIconButton:
                                id: rtt
                                icon: "calendar-clock"
                                theme_text_color: "Custom"
                                text_color: self.theme_cls.primary_color
                                pos_hint: {"center_x":.83,"center_y":.58}  
                                on_press: app.aluga() 

                            MDTextField:
                                id: tg
                                hint_text: "Data de Prazo"
                                size_hint_x: .80
                                font_size: 14
                                disabled:True
                                pos_hint: {"center_x":.5,"center_y":.47}  

                            MDIconButton:
                                id: rttt                        
                                icon: "calendar-clock"
                                theme_text_color: "Custom"
                                text_color: self.theme_cls.primary_color
                                pos_hint: {"center_x":.83,"center_y":.49} 
                                on_press: app.prazo()   

                            MDTextField:
                                id: hora
                                hint_text: "Hora"                        
                                size_hint_x: .40
                                font_size: 14
                                disabled:True
                                pos_hint: {"center_x":.3,"center_y":.38}  

                            MDIconButton:
                                id: rt
                                icon: "clock"
                                theme_text_color: "Custom"
                                text_color: 29/255, 161/255, 242/255, 1  
                                pos_hint: {"center_x":.48,"center_y":.40}  
                                on_press: app.ho()                              

                            MDTextField:
                                id: endereco
                                hint_text: "Endereço da entrega"                           
                                size_hint_x: .80
                                font_size: 14
                                icon_right: "map-marker-radius"
                                icon_right_color:self.theme_cls.primary_color                                 
                                pos_hint: {"center_x":.5,"center_y":.29}                           

                            MDTextField:
                                id: dia
                                hint_text: "Dias"
                                size_hint_x: .33
                                font_size: 15
                                icon_right: "calendar-month"
                                icon_right_color:self.theme_cls.primary_color                                   
                                pos_hint: {"center_x":.74,"center_y":.38}  

                            MDTextField:
                                id: form
                                hint_text: "Pagamento.."                           
                                size_hint_x: .80
                                disabled: True
                                icon_right: "sack"
                                icon_right_color:self.theme_cls.primary_color                                  
                                font_size: 14
                                pos_hint: {"center_x":.5,"center_y":.20}   

                            MDFillRoundFlatButton:
                                text: "Confirmar aluguel"         
                                pos_hint: {'center_x': 0.5, 'center_y': .1} 
                                on_release: 
                                    app.aluguel()
                                                                                            
"""

firebase = firebase.FirebaseApplication('https://rent-car-banco-dados-default-rtdb.firebaseio.com/')

class Tab(FloatLayout, MDTabsBase):
    pass    
class Content(BoxLayout):
    pass
class RentCar(MDApp):

    url = 'https://rent-7a542-default-rtdb.firebaseio.com/.json'
    def build(self):

        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.accent_palette = "Yellow"
        screen = Builder.load_string(janelas) 

        ani = Animation(text_color =  (1,1,1,1)) + Animation(text_color = self.theme_cls.primary_color)
        ani.repeat=True
        ani.start(screen.ids.rt)

        aniw = Animation(text_color =  (1,1,1,1)) + Animation(text_color = self.theme_cls.primary_color)
        aniw.repeat=True         
        aniw.start(screen.ids.rtt)

        animplu = Animation(text_color = (1,1,1,1)) + Animation(text_color = (1,1,1, .2))
        animplu.repeat=True
        animplu.start(screen.ids.act) 

        aniq = Animation(text_color =  (1,1,1,1)) + Animation(text_color = self.theme_cls.primary_color)
        aniq.repeat=True        
        aniq.start(screen.ids.rttt)

        animt = Animation(text_color =  (1,1,1,1)) + Animation(text_color = (128/255,128/255,128/255,1))
        animt.repeat=True
        animt.start(screen.ids.l)   

        animpu = Animation(text_color =  (1,1,1,1)) + Animation(text_color = (128/255,128/255,128/255,1))
        animpu.repeat=True
        animpu.start(screen.ids.r)               

        anim = Animation(text_color =  (1,1,1,1)) + Animation(text_color = (128/255,128/255,128/255,1))
        anim.repeat=True
        anim.start(screen.ids.yordania)   

        animp = Animation(text_color =  (1,1,1,1)) + Animation(text_color = (128/255,128/255,128/255,1))
        animp.repeat=True
        animp.start(screen.ids.lefo) 

        animtp = Animation(text_color =  (1,1,1,1)) + Animation(text_color = (128/255,128/255,128/255,1))
        animtp.repeat=True
        animtp.start(screen.ids.lefro) 

        animpl = Animation(text_color =  (1,1,1,1)) + Animation(text_color = (128/255,128/255,128/255,1))
        animpl.repeat=True
        animpl.start(screen.ids.rigp)                 

        anima = Animation(text_color =  (1,1,1,1)) + Animation(text_color = (0,0,0,1))
        anima.repeat=True
        anima.start(screen.ids.bottta)

        animoa = Animation(text_color =  (1,1,1,1)) + Animation(text_color = (0,0,0,1))
        animoa.repeat=True
        animoa.start(screen.ids.botaa) 

        animoai = Animation(text_color =  (1,1,1,1)) + Animation(text_color = (0,0,0,1))
        animoai.repeat=True
        animoai.start(screen.ids.botta)         

        animoao = Animation(text_color =  (1,1,1,1)) + Animation(text_color = (0,0,0,1))
        animoao.repeat=True       
        animoao.start(screen.ids.botar)

        nimwaa = Animation(text_color =  (1,1,1,1)) + Animation(text_color = (1,1,1,  .2))
        nimwaa.repeat=True
        nimwaa.start(screen.ids.cli)

        animaea = Animation(text_color =  (1,1,1,1)) + Animation(text_color = (1,1,1,  .2))
        animaea.repeat=True
        animaea.start(screen.ids.lo)    

        animaau = Animation(text_color =  (1,1,1,1)) + Animation(text_color = (1,1,1,  .2))
        animaau.repeat=True
        animaau.start(screen.ids.lop)              

        nimaa = Animation(text_color =  (1,1,1,1)) + Animation(text_color = (1,1,1,  .2))
        nimaa.repeat=True
        nimaa.start(screen.ids.lei) 

        animar = Animation(text_color =  ([71/200,73/200,82/200,2])) + Animation(text_color = (1,1,1,  .2)) + Animation(text_color = (128/255,128/255,128/255,1))
        animar.repeat=True
        animar.start(screen.ids.al2)        

        animaea = Animation(size_hint = (.9, 0.67),duration=1,t='in_out_back')
        animaea.start(screen.ids.card29)          

        return screen

    i=1
    def rotooo(self):
        self.i += 1
        if self.i%2 == 0:
            self.root.ids.fgggg.icon = "star"
            self.root.ids.fgggg.text_color = [255/255,215/255,0/255,1]
            self.root.ids.fgaaaa.icon = "star"
            self.root.ids.fgaaaa.text_color = [255/255,215/255,0/255,1]
            self.root.ids.fgbbbb.icon = "star"
            self.root.ids.fgbbbb.text_color = [255/255,215/255,0/255,1]
            toast("Obrigada pelas estrelas!")
        else:
            self.root.ids.fgggg.icon = "star-outline"
            self.root.ids.fgggg.text_color = 1,1,1,1
            self.root.ids.fgaaaa.icon = "star-outline"
            self.root.ids.fgaaaa.text_color = 1,1,1,1
            self.root.ids.fgbbbb.icon = "star-outline"
            self.root.ids.fgbbbb.text_color = 1,1,1,1
            
    def rotoo(self):
        self.i += 1
        if self.i%2 == 0:
            self.root.ids.fggg.icon = "star"
            self.root.ids.fggg.text_color = [255/255,215/255,0/255,1]
            self.root.ids.fgaaa.icon = "star"
            self.root.ids.fgaaa.text_color = [255/255,215/255,0/255,1]
            self.root.ids.fgbbb.icon = "star"
            self.root.ids.fgbbb.text_color = [255/255,215/255,0/255,1]
            toast("Obrigada pelas estrelas!")
        else:
            self.root.ids.fggg.icon = "star-outline"
            self.root.ids.fggg.text_color = 1,1,1,1
            self.root.ids.fgaaa.icon = "star-outline"
            self.root.ids.fgaaa.text_color = 1,1,1,1
            self.root.ids.fgbbb.icon = "star-outline"
            self.root.ids.fgbbb.text_color = 1,1,1,1
            
    def roto(self):
        self.i += 1
        if self.i%2 == 0:
            self.root.ids.fgg.icon = "star"
            self.root.ids.fgg.text_color = [255/255,215/255,0/255,1]
            self.root.ids.fgaa.icon = "star"
            self.root.ids.fgaa.text_color = [255/255,215/255,0/255,1]
            self.root.ids.fgbb.icon = "star"
            self.root.ids.fgbb.text_color = [255/255,215/255,0/255,1]
            toast("Obrigada pelas estrelas!")
        else:
            self.root.ids.fgg.icon = "star-outline"
            self.root.ids.fgg.text_color = 1,1,1,1
            self.root.ids.fgaa.icon = "star-outline"
            self.root.ids.fgaa.text_color = 1,1,1,1
            self.root.ids.fgbb.icon = "star-outline"
            self.root.ids.fgbb.text_color = 1,1,1,1
    
    def rot(self):
        self.i += 1
        if self.i%2 == 0:
            self.root.ids.fg.icon = "star"
            self.root.ids.fg.text_color = [255/255,215/255,0/255,1]
            self.root.ids.fga.icon = "star"
            self.root.ids.fga.text_color = [255/255,215/255,0/255,1]
            self.root.ids.fgb.icon = "star"
            self.root.ids.fgb.text_color = [255/255,215/255,0/255,1]
            toast("Obrigada pelas estrelas!")
        else:
            self.root.ids.fg.icon = "star-outline"
            self.root.ids.fg.text_color = 1,1,1,1
            self.root.ids.fga.icon = "star-outline"
            self.root.ids.fga.text_color = 1,1,1,1
            self.root.ids.fgb.icon = "star-outline"
            self.root.ids.fgb.text_color = 1,1,1,1

    def relatorio(self):
        nome = self.root.ids.nome1.text
        dat = self.root.ids.dia.text
        end = self.root.ids.endereco.text
        mc = self.root.ids.marca.text
        md = self.root.ids.modelo.text
        h = self.root.ids.hora.text
        t = self.root.ids.tg.text
        y = self.root.ids.yt.text
        c = self.root.ids.cor.text
        j = self.root.ids.form.text
        
        senh = self.dialog.content_cls.ids.senha.text
        if senh is "":
            toast("Preencha a senha")
            
        elif senh!="2727":
            toast("Senha incorrecta senhor")
            senh = self.dialog.content_cls.ids.senha.text = ""
        else:
            #criar o pdf
            self.c = canvas.Canvas("cliente.pdf")
            self.c.setFont("Helvetica-Bold", 18)
            self.c.drawString(245,765,'Rent Car')
            
            self.c.setFont("Helvetica",14)
            self.c.drawString(191,743,'Projecto Nova Vida / Rua 70')
            
            self.c.setFont("Helvetica",14)
            self.c.drawString(210,723,'NIF: 00239040932384')
            
            self.c.setFont("Helvetica",14)
            self.c.drawString(230,705,'Data: '+y)
            
            self.c.setFont("Helvetica",14)
            self.c.drawString(225,689,'Luanda / Angola')
            
            self.c.rect(55, 670, 480, 3, fill=True, stroke=False)
            
            self.c.setFont("Helvetica-Bold", 14)
            self.c.drawString(55,630,'Email:')
            
            self.c.setFont("Helvetica", 12)
            self.c.drawString(110,630,nome)
            
            self.c.setFont("Helvetica-Bold",14)
            self.c.drawString(55,590,'Marca: ')

            self.c.setFont("Helvetica", 12)
            self.c.drawString(110,590,mc)
            
            self.c.setFont("Helvetica-Bold", 14)
            self.c.drawString(55,550,'Modelo: ')
            
            self.c.setFont("Helvetica", 12)
            self.c.drawString(120,550,md)
            
            self.c.setFont("Helvetica-Bold",14)
            self.c.drawString(55,512,'Cor: ')

            self.c.setFont("Helvetica", 12)
            self.c.drawString(100,512,c)

            self.c.setFont("Helvetica-Bold", 14)
            self.c.drawString(55,472,'Data de Aluguel: ')
            
            self.c.setFont("Helvetica", 12)
            self.c.drawString(173,472,y)
            
            self.c.setFont("Helvetica-Bold",14)
            self.c.drawString(55,432,'Data de Prazo: ')

            self.c.setFont("Helvetica", 12)
            self.c.drawString(162,432,t)

            self.c.setFont("Helvetica-Bold",14)
            self.c.drawString(55,390,"Hora: ")

            self.c.setFont("Helvetica",12)
            self.c.drawString(100,390,h)

            self.c.setFont("Helvetica-Bold",14)
            self.c.drawString(55,350,"Dias: ")

            self.c.setFont("Helvetica",12)
            self.c.drawString(100,350,dat)

            self.c.setFont("Helvetica-Bold",14)
            self.c.drawString(55,310,"Endereço de entrega: ")

            self.c.setFont("Helvetica",12)
            self.c.drawString(205,310,end)

            self.c.setFont("Helvetica-Bold",14)
            self.c.drawString(55,110,"IBAN: ")

            self.c.setFont("Helvetica",12)
            self.c.drawString(100,110,"00056086943920338")

            self.c.setFont("Helvetica-Bold",14)
            self.c.drawString(410,110,"TOTAL: ")

            self.c.setFont("Helvetica",12)
            self.c.drawString(489,110,j+"00kz")
            
            self.c.rect(55,90,480,3, fill=True, stroke=False)

            self.c.setFont("Helvetica-Bold",14)
            self.c.drawString(217,50,"Obrigado pela preferência!")
            
            self.c.rect(30,23,535,800, fill=False, stroke=True)
            #chamar o pdf
            self.c.showPage()
            #salvar o pdf
            self.c.save()
            #faz exibir e chamar o arquivo
            webbrowser.open("cliente.pdf")        

    def star_second(self):
        threading.Thread(target=self.load_data).start()

    def load_data(self):
        request = requests.get(f'https://rent-car-banco-dados-default-rtdb.firebaseio.com/Veiculos/.json')
        gravar = json.loads(request.content.decode())

        cols = ["Modelo"]
        values = []
        count = 0

        for trip, data in gravar.items():
            lista = []
            lista.append(trip)

            for key, info in data.items():
                lista.append(info)
                if count == 0:
                    cols.append(key)

            count +=1
            values.append(lista)

        self.veicu_table(cols,values)

    @mainthread
    def veicu_table(self,cols,values):
        self.root.ids.veiculoe.clear_widgets()
        self.cli = MDDataTable(pos_hint = {"center_x":0.5,"center_y":.50},
                            rows_num=100,
                            size_hint = (.98,0.99),
                            column_data = [
                                (col,dp(24)) for col in cols                                                            
                            ],
                            row_data = values
                            )
        self.root.ids.veiculoe.add_widget(self.cli)

    def tree_janela(self):
        threading.Thread(target=self.janela_load).start()

    def janela_load(self):
        request = requests.get(f'https://rent-car-banco-dados-default-rtdb.firebaseio.com/Taxas/.json')
        pegar = json.loads(request.content.decode())
    
        cols = ["Modelo"]
        cont = 0
        values = []
            
        for trip, data in pegar.items() :
            lista = []
            lista.append(trip)
            for key, info in data.items():
                lista.append(info)
                if cont == 0:
                    cols.append(key)
            cont +=1
            values.append(lista)

        self.taxas_table(cols,values)

    @mainthread
    def taxas_table(self, cols, values):
        self.root.ids.tax.clear_widgets()
        self.taxs = MDDataTable(pos_hint = {"center_x":0.5,"center_y":.50},
                            rows_num=100,
                            size_hint = (.98, 0.99),
                            column_data = [
                                (col,dp(25)) for col in cols
                            ],
                            row_data = values
                        )
        self.root.ids.tax.add_widget(self.taxs)    

    def guardar(self):
        name = self.root.ids.nome.text
        agee = self.root.ids.age.text
        fone = self.root.ids.tele.text    
        email = self.root.ids.email.text
        pas = self.root.ids.pais.text
        rua = self.root.ids.morada.text    

        if name is "" or agee is "" or fone is "" or email is "" or pas is "" or rua is "":
            toast(" Por favor preencha todo formulário "+name)
            return 0

        elif len(name)<3:
            toast("Por favor digite um nome existente")

        elif agee in ("0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17"):
            toast("Menor de idade não é permitido")

        elif re.search("[a-zA-Z]", agee):
            toast("Idade inválido")
            return 0

        elif len(agee)>3:
            toast(" Idade inválida "+name)
            return 0

        elif re.search("[a-zA-Z]", fone):
            toast(" Número de telefone inválido "+name)
            return 0

        elif len(fone)>9 or len(fone)<9:
            toast(" Número do telefone incorrecto "+name)

            return 0

        elif not re. match(r"[^@]+@[^@]+\.[^@]+", email):
            toast(" Email inválido senhor/a "+name)
            return

        elif len(pas)<3:
            toast("Por favor digite corretamente o seu país senhor/a ")
            return 0         

        else:
            cldo = MDIconButton(icon="thumb-up",on_release=self.sair)
            self.dialog = MDDialog(title="Rent Car",text="Dados cadastrado com sucesso senhor/a "+name,size_hint=(0.8,0.7),buttons=[cldo])
            self.dialog.open()
            valor = randint(0,100)
            gravar = firebase.put('/Cliente',valor,{"Nome":name,"Idade":agee,"Telefone":fone,"Morada":rua,"Email":email,"Pais":pas})        
            
            email_from = "clienterentcar@gmail.com"
            email_to = "rentcarluanda2021@gmail.com"
            senha = "cliente123@"
            mensagem = '''
Novo cliente acessado no sistema, actualize a janela cliente do sistema para saber e conferir o cliente.
            '''
            mensa = "Cliente: "+email
            Subjecto="Cliente Novo"
            
            server = smtplib.SMTP("smtp.gmail.com", 587)

            server.starttls()

            server.login(email_from,senha)
            
            message = 'Subject: {}\n\n\n{}{}'.format(Subjecto,mensa,mensagem)
            server.sendmail(email_from,email_to,message)
            
            print("Enviado com sucesso")

    def aluguel(self):
        nome = self.root.ids.nome1.text
        dat = self.root.ids.dia.text
        end = self.root.ids.endereco.text
        mc = self.root.ids.marca.text
        md = self.root.ids.modelo.text
        h = self.root.ids.hora.text
        t = self.root.ids.tg.text
        y = self.root.ids.yt.text
        c = self.root.ids.cor.text
        j = self.root.ids.form.text
        
        result = 0
        valor = randint(0,100)

        if nome is "" or  dat is "" or end is "" or h is "" or c is "" or t is "" or y is "" or md is "" or  mc is "":            
            toast("Preencha o formulário correctamente!")

        elif not re. match(r"[^@]+@[^@]+\.[^@]+", nome):
            toast("Email incorrecto senhor/a")
            
        elif mc not in ("Jeep", "Mercedes","Wolsgkan","Suzuki","Ranger Rover","Corola","Toyota"):
            toast("Marca não encontrado")

        elif md not in ("T-Cross", "Jimmy Sierra","Capournd","Ilux","Benz","Coaster","Hiace","Revoque 2.0","revoque 2.0","Compass","Renange","Hiace"):
            toast("Modelo não encontrado")            

        elif re.search("[a-zA-Z]", dat) or len(dat)>2:
            toast("Formato do dia inválido")         
        else:
            if md == "Benz" or md == "Ilux" and mc == "Mercedes":
                result = float(dat)*6.000
                self.root.ids.form.text = str(result)
                gravar = firebase.put('/Pedidos',valor,{"Email":nome,"Data de Prazo":y,"Data de aluguel":t,"Hora":h,"Cor":c,"Endereço":end,"Modelo":md,"Marca":mc,"Dias":dat})
                clo = MDIconButton(icon="thumb-up",on_press=self.responder)                
                self.dialog = MDDialog(title="Rent Car",text="Confirmar o aluguel do veiculo "+mc+" no valor de "+str(result)+"00kz",size_hint=(0.8,0.7),buttons=[clo])
                self.dialog.open()
            elif md == "Coaster" or md == "Hiace" and mc == "Toyota":
                result = float(dat)*5.000
                self.root.ids.form.text = str(result)
                gravar = firebase.put('/Pedidos',valor,{"Email":nome,"Data de Prazo":y,"Data de aluguel":t,"Hora":h,"Cor":c,"Endereço":end,"Modelo":md,"Marca":mc,"Dias":dat})
                clo = MDIconButton(icon="thumb-up",on_press=self.responder)
                self.dialog = MDDialog(title="Rent Car",text="Confirmar o aluguel do veiculo "+mc+" no valor de "+str(result)+"00kz",size_hint=(0.8,0.7),buttons=[clo])
                self.dialog.open()
            elif md == "Revoque 2.0" or md == "revoque 2.0" and mc == "Ranger Rover":
                result = float(dat)*7.000
                self.root.ids.form.text = str(result)
                gravar = firebase.put('/Pedidos',valor,{"Email":nome,"Data de Prazo":y,"Data de aluguel":t,"Hora":h,"Cor":c,"Endereço":end,"Modelo":md,"Marca":mc,"Dias":dat})
                clo = MDIconButton(icon="thumb-up",on_press=self.responder)
                self.dialog = MDDialog(title="Rent Car",text="Confirmar o aluguel do veiculo "+mc+" no valor de "+str(result)+"00kz",size_hint=(0.8,0.7),buttons=[clo])
                self.dialog.open()
            elif md == "Jimmy Sierra" and mc == "Suzuki":
                result = float(dat)*6.000
                self.root.ids.form.text = str(result)
                gravar = firebase.put('/Pedidos',valor,{"Email":nome,"Data de Prazo":y,"Data de aluguel":t,"Hora":h,"Cor":c,"Endereço":end,"Modelo":md,"Marca":mc,"Dias":dat})
                clo = MDIconButton(icon="thumb-up",on_press=self.responder)
                self.dialog = MDDialog(title="Rent Car",text="Confirmar o aluguel do veiculo "+mc+" no valor de "+str(result)+"00kz",size_hint=(0.8,0.7),buttons=[clo])
                self.dialog.open()
            elif md == "Capournd" and mc == "Ranger Rover":
                result = float(dat)*5.000
                self.root.ids.form.text = str(result)
                gravar = firebase.put('/Pedidos',valor,{"Email":nome,"Data de Prazo":y,"Data de aluguel":t,"Hora":h,"Cor":c,"Endereço":end,"Modelo":md,"Marca":mc,"Dias":dat})
                clo = MDIconButton(icon="thumb-up",on_press=self.responder)
                self.dialog = MDDialog(title="Rent Car",text="Confirmar o aluguel do veiculo "+mc+" no valor de "+str(result)+"00kz",size_hint=(0.8,0.7),buttons=[clo])
                self.dialog.open()
            elif md == "T-Cross" and mc == "Woslkgan":
                result = float(dat)*4.000
                self.root.ids.form.text = str(result)
                gravar = firebase.put('/Pedidos',valor,{"Email":nome,"Data de Prazo":y,"Data de aluguel":t,"Hora":h,"Cor":c,"Endereço":end,"Modelo":md,"Marca":mc,"Dias":dat})
                clo = MDIconButton(icon="thumb-up",on_press=self.responder)
                self.dialog = MDDialog(title="Rent Car",text="Confirmar o aluguel do veiculo "+mc+" no valor de "+str(result)+"00kz",size_hint=(0.8,0.7),buttons=[clo])
                self.dialog.open()
            elif md == "Wrangler" or md == "Compass" or md == "Renange" or md == "Revonque" and mc == "Jeep":
                result = float(dat)*3.000
                self.root.ids.form.text = str(result)
                gravar = firebase.put('/Pedidos',valor,{"Email":nome,"Data de Prazo":y,"Data de aluguel":t,"Hora":h,"Cor":c,"Endereço":end,"Modelo":md,"Marca":mc,"Dias":dat})
                clo = MDIconButton(icon="thumb-up",on_press=self.responder)
                self.dialog = MDDialog(title="Rent Car",text="Confirmar o aluguel do veiculo "+mc+" no valor de "+str(result)+"00kz",size_hint=(0.8,0.7),buttons=[clo])
                self.dialog.open()                
            else:
                toast("Este modelo ou marca não faz parte")
                
    def responder(self, *args):
        self.dialog = MDDialog(
            title = "Cartão",
            size_hint_x=(0.9),
            type = "custom",
            content_cls = Content()
        )
        self.dialog.open()    
                    
    def check(self, checkbox, value):
        if value:
            self.theme_cls.theme_style = 'Dark'
            self.root.ids.switch.thumb_color_down = 1,1,1,1
            self.root.ids.lefo.text_color =  1,1,1,1 
            self.root.ids.rigp.text_color =  1,1,1,1 
            self.root.ids.yordania.text_color =  1,1,1,1 
            self.root.ids.fac.text_color =  1,1,1,1 
            self.root.ids.ins.text_color =  1,1,1,1     
            self.root.ids.fact.text_color =  1,1,1,1 
            self.root.ids.inst.text_color =  1,1,1,1  
            self.root.ids.f.text_color =  1,1,1,1 
            self.root.ids.facc.text_color =  1,1,1,1 
            self.root.ids.i.text_color =  1,1,1,1              
            self.root.ids.inss.text_color =  1,1,1,1  
            self.root.ids.icoi.text_color =  1,1,1,1            

        else:
            self.theme_cls.theme_style = 'Light'
            self.root.ids.switch.thumb_color_down =  0,0,0,1                 
            self.root.ids.lefo.text_color =  [71/200,73/200,82/200,2] 
            self.root.ids.rigp.text_color =  [71/200,73/200,82/200,2] 
            self.root.ids.yordania.text_color =  [71/200,73/200,82/200,2] 
            self.root.ids.fac.text_color =  [71/200,73/200,82/200,2] 
            self.root.ids.ins.text_color =  [71/200,73/200,82/200,2]  
            self.root.ids.fact.text_color =  [71/200,73/200,82/200,2] 
            self.root.ids.inst.text_color =  [71/200,73/200,82/200,2] 
            self.root.ids.f.text_color =  [71/200,73/200,82/200,2]
            self.root.ids.facc.text_color =  [71/200,73/200,82/200,2]
            self.root.ids.i.text_color =  [71/200,73/200,82/200,2] 
            self.root.ids.inss.text_color =  [71/200,73/200,82/200,2]     
            self.root.ids.icoi.text_color =  [71/200,73/200,82/200,2]               

    def show_bottom_sheet(self):
        self.custom = MDCustomBottomSheet(screen=Factory.CustomSheet())  
        self.custom.open()        

    def face(self):
        self.snackbar = Snackbar(text="Facebook: Rent Car Luanda!",height=12)
        self.snackbar.open()
        webbrowser.open("www.facebook.com")

    def insta(self):
        self.snackbar = Snackbar(text="Instagram: rent_car_luanda")
        self.snackbar.open()
        webbrowser.open_new("www.instagram.com")

    def whats(self):
        self.snackbar = Snackbar(text="WhatsApp: 992419634/915918858")
        self.snackbar.open()
        webbrowser.open_new("www.whatssap.com")

    def direita(self):    
        self.snackbar = Snackbar(text="Arraste a imagem a direita")
        self.snackbar.open()

    def esquerda(self):    
        self.snackbar = Snackbar(text="Arraste a imagem a esquerda")
        self.snackbar.open()  

    def icoo(self):
        fecharr = MDIconButton(icon="thumb-up",on_release=self.sair)
        self.dialog = MDDialog(title="Quem Somos?",text="Rent Car Luanda é uma empresa de alguel de veiculos localizada somente em Angola, apostamos num serviço de excelência, permitindo aos nossos clientes uma viagem sem preocupação e com segurança, de modo a sastifazer as necessidades e desejos dos nossos clientes.     Obrigado!",size_hint=(0.9, 0.10),buttons = [fecharr])
        self.dialog.open()

    def usu(self):
        ok = MDIconButton(icon="thumb-up",on_release=self.sair)
        self.dialog = MDDialog(title="Rent Car",text="Dados guardados com sucesso Senhor/a",size_hint =(0.9,.70),buttons=[ok])
        self.dialog.open()
        
    def saire(self):
        self.dialog.dismiss()     

    def sair(self,obj):
        self.dialog.dismiss()        
    
    def sairR(self,obj):
        self.dialog.dismiss()

    def prazo(self):
        date_dialog = MDDatePicker(radius = [7,7,7,7],callback=self.data,year=2021,month=4,day=4)
        date_dialog.open()
    def data(self,date):
        self.root.ids.tg.text = date.strftime("%d/%m/%y")

    def aluga(self):
        alug = MDDatePicker(callback=self.alugar,year=2021,month=4,day=1)
        alug.open()
    def alugar(self,date):
        self.root.ids.yt.text = date.strftime("%d/%m/%y")

    def ho(self):
        hrd = MDTimePicker()
        hrd.bind(time=self.timi)
        hrd.open()
    def timi(self,instance,time):
        self.root.ids.hora.text = time.strftime("%H:%M")

    def intro(self):
        self.root.ids.nome1.text = self.root.ids.nome.text


RentCar().run()
