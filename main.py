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

    t = random.random()
    if t < sx[jg][0]: return '1'
                
    elif t < sx[jg][1]: return 'x'
            
    else: return '2'
        

    
x = [[intProb(text(np, nj)) for np in range(3)] for nj in range(13)]

sx = cumSum(x)
texRes = open('result.txt','w')


for jg in range(10):
    for i in range(13):
        texRes.write(resJog(sx,i)+'\t')
    texRes.write('\n')

texRes.close()

