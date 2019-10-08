import os

class removeid:
    def __init__ (self, caminho, arquivo_caminho):
        self.caminho = f"C:\\Users\\ksilva\\Desktop\\{caminho}"
        self.arquivo_caminho = arquivo_caminho
    
    def removerid(self):
        cont = 0
        while(cont <= 1):
            dire = os.listdir(self.caminho)
            for file in dire:
                if file == self.arquivo_caminho:
                    os.remove(self.arquivo_caminho)
            print(dir)
        cont = cont + 1