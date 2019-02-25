from PIL import Image
import numpy as np
import image_file as i

linhas = 20#60 #use 60 para a imagem completa
colunas = 80
dataArray = i.RGB565_1

# Monta o array da imagem a partir do formato RGB565             
#Monta o RGB
a=[0]*3
#Monta as Colunas
a=[a]*colunas
#Monta as Linhas
a=[a]*linhas
a = np.array(a, dtype=np.uint8)
#Algor√≠timo montado baseado nesse site:
#http://www.barth-dev.de/online/rgb565-color-picker/  
for x in range (0,linhas):
    for y in range (0,colunas):
        index = y+colunas*x
        pixel = dataArray[index]
        #invert byte order
        pixel = ((dataArray[index]&0xFF)<<8)|(dataArray[index]>>8)
        #separa as cores
        R = pixel&0b1111100000000000
        G = pixel&0b0000011111100000
        B = pixel&0b0000000000011111
        #shift para a posiÁ„o correta
        a[x,y,0] = R>>8
        a[x,y,1] = G>>3
        a[x,y,2] = B<<3

# Use PIL to create an image from the new array of pixels
new_image = Image.fromarray(a,"RGB")
new_image.save('new.png')
