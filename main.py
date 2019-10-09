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
        x = str(input("1 SELECIONE A OPÇÃO: "))
        x = x.lower()
        if(x == 'break'):
            stop(x)
        elif(x == 'b'):
            sleepbye()
            print('.....ok\n')
            print(' ________________________________________')
            print('|----------------------------------------|')
            print('|-------WELCOME TO APP THE ITM-----------|')
            print('|--------------Option: A-----------------|')
            print('|-----!!Digite o nome do arquivo!!-------|')
            print('|------------com sua extensão------------|')
            print('|------Ex: arquivo.txt // arquivo.svg----|')
            print('|----------------------------------------|')
            print('|----------!Continuar???[y/n]!-----------|')
            try:
                x = str(input("DESEJA CONTINUAR: "))
                x = x.lower()
                if(x == 'y'):
                    sleepbye()
                    print('\n')
                    arquivo = str(input("Digite o nome do arquivo: "))
                    if(arquivo != str(None)):
                        remocao = deply.Removetags(arquivo)
                        sleepbye()
                        print('\n')
                        if(remocao.get_consultarquivo() != FileNotFoundError):
                            print('\n.....ok\n')
                            sleepbye()
                            if(remocao.get_consultaconteudo() == None):
                                print('Houve um erro')
                            else:
                                remocao.removertags()
                                print('\nOperação realiza com sucesso!')
                        else:
                            print('Desculpe, Arquivo não encontrado')
                    else:
                        print('Erro')
                        stop(x)
                        pass
                elif(x != 'y'):
                    print('Operação cancelada')
                    x = 'break'
                    stop(x)
            except KeyboardInterrupt:
                print("Operação interrompida")
            except UnboundLocalError:
                print("Operação interrompida")
        if(x == 'd'):
                print(' ________________________________________')
                print('|----------------------------------------|')
                print('|-------WELCOME TO APP THE ITM-----------|')
                print('|--------------Option: D-----------------|')
                print('|----------------------------------------|')
                print('|1° Adicione um arquivo txt ou svg-------|')
                print('|2° O nome do arquivo deve ser simples---|')
                print('|3° Seram criados novos arquivos com as f|')
                print('|unções executadas-----------------------|')
                print('|4º O arquivo removidos mostra as tags qu|')
                print('|e foram removidas-----------------------|')
                print('|----------------------------------------|')
                print('|--------!Digit: Break para sair!--------|')
                print('|----------------------------------------|\n')
    except KeyboardInterrupt:
        print("Operação interrompida")
    except UnboundLocalError:
        print("Operação interrompida")

def stop(x): 
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
