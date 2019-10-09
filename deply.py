import re, os

class Removetags():
    def __init__(self, arquivo):
        self.arquivo = arquivo
    
    def get_consultarquivo(self):
        return self.arquivo
    def get_consultaconteudo(self):
        try:
            verificacao = self.arquivo
            entrada = open(verificacao, 'r', encoding='UTF-8')
            cont = 0
            for j in entrada:
                cont = cont + 1
            if(cont == 0 or cont <= 1):
                entrada.close()
                print("\nO arquivo pode estar corrompido ou vazio")
                return
            if(entrada == None):
                entrada.close()
                print("O arquivo é inexistente")
                return
        except FileNotFoundError:
            print("\nO arquivo é inexistente")
            return
        return self.arquivo
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
            arquivo_svg.close()
            planta.close()
