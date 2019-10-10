
class Consulta():
    def __init__ (self, arquivo):
        self.arquivo = arquivo
    
    def set_tag(self, tag):
        self.tag = tag

    def get_consutararquivo(self):
        try:
            verificacao = self.arquivo
            entrada = open(verificacao, 'r', encoding='UTF-8')
            print("o arquivo ta aqui")
            entrada.close()
            return self.arquivo
        except FileNotFoundError:
            print("o arquivo n ta aqui")
        
    
    def get_consultaconteudo(self):
        verificacao = self.arquivo
        entrada = open(verificacao, 'r', encoding='UTF-8')
        cont = 0

        for i in entrada:
            abertag = i.count(f"<{self.tag}")
            fechatag = i.count(f"</{self.tag}>")
        if(abertag >= 1 or fechatag >= 1):
            tags = True
        else:
            print("\n Parece que a tag iformada é inexistente :( pfv verifique e tente novamente")
            return
        if(tags == True):
            pass

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
        return self.arquivo

consultar = Consulta("teste.svg")
consultar.set_tag("tspan")
consultar.get_consutararquivo()
consultar.get_consultaconteudo()