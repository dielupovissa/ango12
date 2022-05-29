# this script calculate chances for angofoot12

import random
def intProb(text):
    
    while True:
        str = input(text)
        try:
            pr = float(str)
            if pr <=1 and pr>=0:
                return pr
            else: print("escreva um valor entre 0 e 1")
        except ValueError:
            print("Por favor escreva um numero")

def text(np, nj):
    
    if np == 0: return ' jogo '+str(nj)+' Vence a equipa de casa:'
    
    if np == 1: return '\n jogo '+str(nj)+' jogo acaba empatado:'
    
    if np == 2: return '\n jogo '+str(nj)+' Vence a equipa de fora:'

def cumSum(x):
    
    return [[cSum(x,i,j)for i in range(3)] for j in range(13)]
def cSum(x,i,j):
    sum = 0
    if i == 0: return x[j][0]
    for n in range(i+1):
        sum = sum + x[j][i-n]
    return sum

def resJog(sx,jg):
    cum1 =0
    cum2 = 0
    cum3 = 0
    for i in range(100):
        t = random.random()
        if t < sx[jg][0]:
            #print('1 ')
            cum1 = cum1 +1
    
        elif t < sx[jg][1]:
            #print('x ')
            cum2 = cum2 + 1
        else:
            #print('2 ')
            cum3 = cum3 + 1
    if cum1 > cum2 and cum1 > cum3: return '1'
    elif cum2 > cum1 and cum2 > cum3: return 'x'
    else: return '2'

    
x = [[intProb(text(np, nj)) for np in range(3)] for nj in range(13)]

sx = cumSum(x)

for i in range(13):
    print(resJog(sx,i))

