import re

class Removetags():
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def set_tag(self, tag):
        self.tag = tag
        
    def removertags(self):
        count = 0
        tags_removidas = open('removidos.txt', 'w')
        planta = open(r'planta_nova.svg', 'w', encoding='UTF-8')
        with open(self.arquivo, 'r', encoding='UTF-8') as arquivo_svg:            
            arqui = open(arquivo_svg, 'w', encoding='UTF-8')
            for i in arquivo_svg:
                count = count + 1
                #print(i)
                x = i
                #z = re.search(f"<{self.tag}.+?>", x)
                #x = re.sub(f"<{self.tag}.+?/>", "", x)
                #tags_removidas.write(z.group() + '\n')
                #z = re.search(f"</{self.tag}>", x)
                #tags_removidas.write(z.group() + '\n')

            z = re.sub("<path.+?/>", "", arqui)
            #x = re.sub(f"</{self.tag}>", "", x)
            planta.write(z.group())
            arquivo_svg.close()
            planta.close()


remocao = Removetags('MESSEJANA2.txt')
remocao.set_tag('path')
remocao.removertags()