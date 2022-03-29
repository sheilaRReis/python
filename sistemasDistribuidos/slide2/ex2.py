# Faça um programa que:
# Solicite ao usuário que digite a unidade e nome de um diretório qualquer (path);
# Solicite ao usuário que digite uma palavra;
# Verifique em todos os arquivos texto (.txt) quais as linhas contêm a palavra. Todas as linhas localizadas 
# devem ser salvas em um novo arquivo texto com o nome FIND_GERAL, contendo o seguinte :

# <Palavra localizada>

# [<Nome do arquivo original 1>][<nº linha>]<linha de texto>
# [<Nome do arquivo original 2>][<nº linha>]<linha de texto>
# [<Nome do arquivo original N>][<nº linha>]<linha de texto>
import os
absolutePath = ''
invalidInput = True
fileName     = ''
listLinhas = list()

while(invalidInput):
    absolutePath = input("Digite o caminho do diretório: ").strip()
    searchWord   = input("Digite a palavra que deseja procurar no arquivo: ").strip().casefold()
    if(len(absolutePath)<1):
        print("Favor informar o caminho do diretório!")
        invalidInput = True

    if(len(searchWord)<1):
        print("Favor informar a palavra que será pesquisada nos arquivos do diretório informado!")
        invalidInput = True
    if(len(absolutePath)>0 and len(searchWord)>0):
        invalidInput = False
if len(absolutePath)>0:
    if not absolutePath.endswith("/"):
        absolutePath = "{}\\".format(absolutePath)
        listFiles    = list()
        try:
            listFiles = os.listdir(absolutePath)
        except OSError:
            print("Nao foi possivel abrir o diretório informado!")
        if(len(listFiles)>0):
            for txt_file in listFiles:
                error_flag = False
                if txt_file.endswith(".txt"):
                    try:
                        file        = open("{}{}".format(absolutePath,txt_file))
                    except FileNotFoundError:
                        print("Não foi possível abrir o diretório informado \nCaminho informado: {}".format(absolutePath))
                        error_flag = True
                        continue
                    if not error_flag:
                        linhas     = file.readlines()
                        file.close()
                        countLines = 0
                        for linha in linhas:
                            linha = linha.replace("\n","")
                            countLines+=1
                            if(searchWord in linha.casefold()):    
                                listLinhas.append("[{}][{}][{}]\n".format(txt_file, countLines, linha))
    if(len(listLinhas)>0):
        report_file = open("{}FIND_GERAL.txt".format(absolutePath),"w",encoding='utf-8')

        for linha in listLinhas:
            report_file.write(linha)
        report_file.close()