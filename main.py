import deply, delpyid, deplyarchives
import time
def main():
    print(' ________________________________________')
    print('|----------------------------------------|')
    print('|-------WELCOME TO APP THE ITM-----------|')
    print('|------------Select option---------------|')
    print('|- A = Adicionar IDs em plantas----------|')
    print('|- B = Remover Tags de plantas-----------|')
    print('|- C = Remover os arquivos criados-------|')
    print('|- D = Ler instruções -------------------|')
    print('|----------------------------------------|')
    print('|--------!Digit: Break para sair!--------|')
    print('|--------------k410----------------------|')
    print('|----------------------------------------|')
    x = str(input("SELECIONE A OPÇÃO: "))
    x = x.lower()
    print(x)
    while(x == 'break'):
        try:
            sleepbye()
            break
        except KeyboardInterrupt:
            sleepbye()
            break

    #captura = 'captura'
    #arquivo = 'teste.svg'
    #remocao = deply.Removetags(arquivo)
    #remocao.removertags()

    #remocaoarquivo = deplyarchives.Removerarqui(captura, arquivo)
    #remocaoarquivo.removerarquivos()

    #adicionaid = delpyid.Adicionaid(arquivo)
    #adicionaid.adicionarid()
def progress_bar(done):
    print("\rCarregando: [{0:10s}] {1:.1f}%".format('#' * int(done * 10), done * 20),end='')

def sleepbye():
    for n in range(21):
        progress_bar(n/20)
        time.sleep(0.1)

main()
