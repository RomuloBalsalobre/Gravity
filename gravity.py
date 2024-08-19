import time    
import os
x = 0
y = 0
reverte = False
teto = 0
taxa = 0
mapa = [[' ' for _ in range(40)] for _ in range(5)]

os.system('cls')

posicao = [y,x]
chao = 4

def desenha_mapa(posicao, limpar = False):
    for i in range(5):
        for j in range(40):
            if i == teto:
                mapa[i][j] = 'm'
            if i == chao:
                mapa[i][j] = 'm'
            elif i == posicao[0] and j == posicao[1]:
                mapa[i][j] = '*'
            if limpar:
                mapa[i][j] = ' '
            #else:
             #   mapa[i][j] = ' '
        mapas = str(mapa[i])
        mapas = mapas.replace('[','')
        mapas = mapas.replace(']','')
        mapas = mapas.replace(',','')
        mapas = mapas.replace('\'','')
        print(mapas)
                
while True:
    posicao[0]=y
    posicao[1]=x
    if y >= chao-1:
        reverte = True
        taxa += 1
    if y <= teto+1:
        reverte = False

    if reverte:
        y -= 1
    else:
        y += 1
    x += 1+taxa
    desenha_mapa(posicao)
    time.sleep(0.5)
    os.system('cls')
'''
    if x > 3 and x < 7:
        desenha_mapa(posicao)
        time.sleep(1)
        y -=1
        posicao[0]=y
        posicao[1]=x
        x += 1
      
    elif x >= 7:
        desenha_mapa(posicao)
        time.sleep(1)
        y +=1
        posicao[0]=y
        posicao[1]=x
        x += 1
        os.system('cls')
    else:
        desenha_mapa(posicao)
        time.sleep(1)
        y =x
        posicao[0]=y
        posicao[1]=x
        x += 1
        os.system('cls')
    print(posicao)'''