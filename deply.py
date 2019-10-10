import re

class Removetags():
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def set_tag(self, tag):
        self.tag = tag
        
    def removertags(self):
        count = 0
        tags_removidas = open('removidos.txt', 'w')
        planta = open('planta_nova.svg', 'w', encoding='UTF-8')
        with open(self.arquivo, 'r', encoding='UTF-8') as arquivo_svg:
            for i in arquivo_svg:
                count = count + 1
                print(i)
                x = i
                z = re.search(f"<{self.tag}.+?>", x)
                tags_removidas.write(z.group() + '\n')
                x = re.sub(f"<{self.tag}.+?>", "", x)
                z = re.search(f"</{self.tag}>", x)
                tags_removidas.write(z.group() + '\n')
                x = re.sub(f"</{self.tag}>", "", x)
                planta.write(x)
            arquivo_svg.close()
            planta.close()


remocao = Removetags('teste.svg')
remocao.set_tag('text')
remocao.removertags()