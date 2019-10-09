
class Adicionaid():
	def __init__(self, arquivo):
		self.arquivo = arquivo
	
	def adicionarid(self):
		f = open(self.arquivo, encoding="UTF-8")
		a = open('IDadiconada' + self.arquivo, 'w', encoding="UTF-8")
		contador = 0
		for x in f:
			contador = contador + x.count('id=" "')
			y = x.replace('id=" "', 'id="' + str(contador) + '"')
			a.write(y)
		f.close()