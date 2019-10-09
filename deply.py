import re

class Removetags():
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def removertags(self):
        count = 0
        tags_removidas = open('removidos.txt', 'w')
        planta = open('planta_nova.svg', 'w', encoding='UTF-8')
        with open(self.arquivo, 'r', encoding='UTF-8') as arquivo_svg:
            for i in arquivo_svg:
                count = count + 1
                print(i)
                x = i
                z = re.search("<tspan.+?>", x)
                tags_removidas.write(z.group() + '\n')
                x = re.sub("<tspan.+?>", "", x)
                z = re.search("</tspan>", x)
                tags_removidas.write(z.group() + '\n')
                x = re.sub("</tspan>", "", x)
                planta.write(x)
            print(count)
            arquivo_svg.close()
            planta.close()
