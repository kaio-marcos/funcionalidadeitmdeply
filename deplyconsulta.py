
class Consulta():
    def __init__ (self, arquivo):
        self.arquivo = arquivo
        self.lock = True

    def set_tag(self, tag):
        self.tag = tag
        self.lock = False

    def get_consutararquivo(self):
        try:
            verificacao = self.arquivo
            entrada = open(verificacao, 'r', encoding='UTF-8')
            print("Arquivo....ok")
            entrada.close()
            return self.arquivo
        except FileNotFoundError:
            self.lock = True
            print("Situação: o arquivo não está na pasta raiz")
            return
        
    
    def get_consultaconteudo(self):
        if(self.lock == True):
            print("\nImpossivel realizar a operação: consulta conteudo")
            return
        else:
            pass
        verificacao = self.arquivo
        entrada = open(verificacao, 'r', encoding='UTF-8')
        cont = 0
        abretag = 0
        fechatag = 0
        lista = []
        for j in entrada:
            lista.append(j)
            abretag =+ lista.count(f"<{self.tag}")
            fechatag =+ lista.count(f"</{self.tag}>")
            cont =+ 1
            

        if(cont == 0):
            entrada.close()
            print("\nSituação: O arquivo pode estar corrompido ou vazio")
            return

        if(abretag >= 1 and fechatag >= 1):
            print("\nTag....ok")
        else:
            print("\nParece que a tag iformada é inexistente ou está sem fechamento pfv verifique e tente novamente")
            return
        return self.arquivo

consultar = Consulta("teste.svg")
consultar.set_tag("tspan")
consultar.get_consutararquivo()
consultar.get_consultaconteudo()