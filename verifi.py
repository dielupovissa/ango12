
def lineConv(line):
    str = line.rsplit('\t')
    ss =''
    for i in str:
        ss = ss + i
    st = ss.removesuffix('\n')
    
    return st

def compare(res, line):
    if len(res) == len(line):
        #print('******************************************************')
        cont = 0
        for i in range(len(res)):
            if res[i] == line[i]:
                #print('#')
                cont = cont +1
        return cont

texRes = open('result.txt','r')
strVen = input('o jogo 1:')
for i in range(2,13,1):
    strVen = strVen + input('\n o jogo'+str(i)+':')

for line in texRes:
    ss = lineConv(line)
    flg = compare(strVen,ss)
    
    match flg:
        case 12: 
            print('Vencedor')
            print(ss)
        case 11: 
            print('Segundo lugar')
            print(ss)
        case 10: 
            print('Terceiro lugar')
            print(ss)
        case _: 
            pass

print(strVen)
texRes.close()

