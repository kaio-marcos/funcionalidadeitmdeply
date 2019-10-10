import re
def removertags(arquivo):
    count = 0
    #tags_removidas = open('removidos.txt', 'w')
    planta = open('planta_certa.txt', 'a', encoding='UTF-8') 

    arqui = open(arquivo)
    #for i in arqui:
    #    #print(i)
    #    txt = i
    #    z = re.sub("\n", "", str(txt))
    #    planta.write(z)
    
    for i in arqui:
        txt = i
        z = re.sub("<path.+?>", "", str(txt))
        planta.write(z)

    arqui.close()
    #planta.close()

removertags('planta_nova.txt')