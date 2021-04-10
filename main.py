"""
App mejora de imagen
"""
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
# from kivy.uix.slider import Slider
# from kivy.core.image import Image as CoreImage
# from kivy.uix.image import Image
# from kivy.uix.camera import Camera
# from kivy.graphics.texture import Texture
# import matplotlib.pyplot as plt
# from skimage import filters, color, io
# import numpy as np
# import math
import funciones
# import tempfile

# import io
import os
import cv2


"""
android

"""

# from android.storage import primary_external_storage_path
# primary_ext_storage=primary_external_storage_path()

import certifi
os.environ['SSL_CERT_FILE'] = certifi.where()


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    ima_input = ObjectProperty(None)
    img = ObjectProperty(None)
    cancel = ObjectProperty(None)
    path=ObjectProperty(None)


class Root(FloatLayout):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    ima_input = ObjectProperty(None)
    img = ObjectProperty(None)
    contador = 1


    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Cargar", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Guardar", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()
        
    def reload(self):
        path=self.path + "/" + str(self.contador) +"apoyo.jpg"
        cv2.imwrite(path,self.ima)
        self.ids.img.source=path
        os.remove(path)
        self.contador=self.contador+1

    def load(self,filename,path):
        try:
            file=filename[0]
            self.imaG=funciones.convertir(file)
            self.ima=self.imaG
            self.ids.ima_input.source = file
            self.path=path
            self.reload()
        except:
            pass
        
        self.dismiss_popup()      
        
    def save(self,path,text):
        if self.contador==1:
            print("ingrese una imagen")
        else:
            dire=os.path.join(path,text)
            cv2.imwrite(dire,self.ima)
            self.path=path
            self.dismiss_popup()

    def ecualizar(self):
        if self.contador==1:
            print("ingrese una imagen")
        else:
            self.ima=funciones.histEcu(self.imaG)
            self.reload()
        
    def dosPuntos(self,r1,s1,r2,s2):
        if self.contador==1:
            print("ingrese una imagen")
        else:
            self.ima=funciones.ecDosPuntos(self.imaG,r1,s1,r2,s2)
            self.reload()

    def unsharp(self):
        if self.contador==1:
            print("ingrese una imagen")
        else:
            self.ima=funciones.unsharp_ima(self.imaG)
            self.reload()
        
    
            

class main(App):
    pass


Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('SaveDialog', cls=SaveDialog)


if __name__ == '__main__':
    main().run()