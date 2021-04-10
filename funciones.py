"""
Funciones
mejora de imagen y 
"""

import numpy as np
import matplotlib.pyplot as plt 
from skimage import filters, color, io
import math

def convertir(ima_path):
    ima = io.imread(ima_path)
    size=ima.shape
    if len(size)==3:
        ima=np.uint8(color.rgb2gray(ima)*255)
    elif len(size)==2:
        ima=ima
    else:
        print("Ingrese una imagen valida")
    return ima

def histograma(ima):
    histo=np.zeros(256)
    for i in range(ima.shape[0]):
        for j in range(ima.shape[1]):
            valor=int(ima[i,j])
            histo[valor]=histo[valor]+1
    return(histo)


### mejoras
def histEcu(ima):
    histo=histograma(ima)
    pro=histo/(ima.shape[0]*ima.shape[1])
    a=0
    ecua=np.zeros(256)
    for i in range(256):
        a=pro[i]+a
        ecua[i]=a

    salida=np.zeros((ima.shape[0],ima.shape[1]))
    for i in range(ima.shape[0]):
        for j in range(ima.shape[1]):
            valor=int(ima[i,j])
            salida[i,j]=(255)*ecua[valor]
    return (salida)

def ecDosPuntos(ima, r1, s1, r2, s2):
    salida=np.zeros((ima.shape[0],ima.shape[1]))
    for i in range (ima.shape[0]):
        for j in range (ima.shape[1]):
            pixel=int(ima[i,j])
            if(pixel<=r1):
                salida[i,j]= (s1/r1)*pixel
            elif (r1<pixel and pixel<=r2):
                salida[i,j]=((s2-s1)/(r2-r1)) * (pixel-r1) + s1
            else:
                salida[i,j]=((255-s2)/(255-r2)) * (pixel-r2) + s2  
    return salida

def unsharp_ima(ima):
    cantidad=1.0
    sig=1.0
    umbral=0.0
    # unsharp2=unsharp_ima(imagen,can,sig,umb)
    pB=filters.gaussian(ima, sigma=sig,mode='constant')
    A=(cantidad+1)*ima - cantidad*pB
    B=np.maximum(A,np.zeros(A.shape))
    C=np.minimum(B,255*np.ones(A.shape))
    unsharp=C.round()
    if umbral>0:
        D=np.absolute(ima-pB)<umbral
        np.copyto(unsharp,ima,where=D)
    return unsharp


