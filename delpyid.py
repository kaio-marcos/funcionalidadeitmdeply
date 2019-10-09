
class Adicionaid():
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

	def adicionarid(self):
		f = open(self.arquivo, encoding="UTF-8")
		a = open('IDadiconada' + self.arquivo, 'w', encoding="UTF-8")
		contador = 0
		for x in f:
			contador = contador + x.count('id=" "')
			y = x.replace('id=" "', 'id="' + str(contador) + '"')
			a.write(y)
		f.close()