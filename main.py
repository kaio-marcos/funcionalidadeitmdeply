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
    print('|----------------------------------------|\n')
    try:
        x = str(input("SELECIONE A OPÇÃO: "))
        x = x.lower()
        print(x + '\n')
    except KeyboardInterrupt:
        print("Operação interrompida")
    except UnboundLocalError:
        print("Operação interrompida")
    
    try:
        while(x == 'break'):
            try:
                sleepbye()
                break
            except KeyboardInterrupt:
                sleepbye()
                break
    except UnboundLocalError:
        SystemExit


def progress_bar(num):
    print("\rCarregando: [{0:10s}] {1:.1f}%".format('#' * int(num * 10), num * 20),end='')


def sleepbye():
    for n in range(21):
        progress_bar(n/20)
        time.sleep(0.1)

#captura = 'captura'
#arquivo = 'teste.svg'
#remocao = deply.Removetags(arquivo)
#remocao.removertags()
#remocaoarquivo = deplyarchives.Removerarqui(captura, arquivo)
#remocaoarquivo.removerarquivos()
#adicionaid = delpyid.Adicionaid(arquivo)
#adicionaid.adicionarid()
main()
