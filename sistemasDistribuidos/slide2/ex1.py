# Faça um programa que:
# Solicite ao usuário que digite o nome de um arquivo texto    xxxx (caminho completo) XXXX;
# Solicite ao usuário que digite uma palavra;
# Verifique em todo arquivo quais as linhas contêm a palavra. Todas as linhas localizadas devem ser salvas 
# em um novo arquivo texto com o nome FIND_<nome_arquivo_original>, contendo o seguinte :

# <Nome do arquivo original>
# <Palavra localizada>

# [<nº linha 1>]<linha de texto>
# [<nº linha 2>]<linha de texto>
# [<nº linha N>]<linha de texto>

absolutePath = "C:/Users/Sheila/dev/cursoExtensao_Python/python/sistemasDistribuidos/slide2/"
invalidInput = True
fileName     = ''
while(invalidInput):
    fileName     = input("Digite o nome do arquivo: ").strip()
    searchWord   = input("Digite a palavra que deseja procurar no arquivo: ").strip()
    if(len(fileName)<1):
        print("Favor informar o nome do arquivo")
        invalidInput = True

    if(len(searchWord)<1):
        print("Favor informar a palavra que será pesquisada no arquivo")
        invalidInput = True
    if(len(fileName)>0 and len(searchWord)>0):
        invalidInput = False
if len(fileName)>0:
    file       = open("{}{}".format(absolutePath,fileName))
    linhas     = file.readlines()
    listLinhas = list()
    for linha in linhas:
        if(searchWord in linha):    
            listLinhas.append(linha)

    report_file = open("{}FIND_{}".format(absolutePath, fileName),"w",encoding='utf-8')
        
    for linha in listLinhas:
        report_file.write(linha)