from PIL import Image
import numpy as np
import image_file as i

# Monta o array da imagem a partir do formato RGB888_3valuesMatriz
a = np.array(i.RGB888_3valuesMatriz, dtype=np.uint8)
linhas = 60
colunas = 80

for x in range (0,linhas):
    for y in range (0,colunas):
        for z in range (0,3):
            if z == 0:
                a[x,y,z] = a[x][y][z]<<3
            elif z == 1:
                a[x,y,z] = a[x][y][z]<<2
            elif z == 2:
                a[x,y,z] = a[x][y][z]<<3

# Monta o array da imagem a partir do formato RGB565             
#Monta o RGB
b=[0]*3
#Monta as Colunas
b=[b]*colunas
#Monta as Linhas
b=[b]*linhas
b = np.array(b, dtype=np.uint8)
#Algorítimo montado baseado nesse site:
#http://www.barth-dev.de/online/rgb565-color-picker/  
for x in range (0,linhas):
    for y in range (0,colunas):
        index = y+colunas*x
        R = i.RGB565[index]&0b1111100000000000
        G = i.RGB565[index]&0b0000011111100000
        B = i.RGB565[index]&0b0000000000011111
        b[x,y,0] = R>>8
        b[x,y,1] = G>>3
        b[x,y,2] = B<<3

#Verificação do algorítimo
x = 3 #
y = 5 #
index = y+colunas*x
print(format(bin(i.RGB565[index])))
R = i.RGB565[index]&0b1111100000000000
print("R ",format(bin(R)))
G = i.RGB565[index]&0b0000011111100000
print("G ",format(bin(G)))
B = i.RGB565[index]&0b0000000000011111
print("B ",format(bin(B)))
b[x,y,0] = R>>8
b[x,y,1] = G>>3
b[x,y,2] = B<<3
print(format(i.RGB565[index],'04X'))
print(b[x][y])

# Use PIL to create an image from the new array of pixels
new_image = Image.fromarray(a,"RGB")
new_image.save('a_new.png')
new_image = Image.fromarray(b,"RGB")
new_image.save('b_new.png')
