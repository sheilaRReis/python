# A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. 
# Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e
# identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar
# o seguinte arquivo, chamado "usuarios.txt":
# alexandre       456123789
# anderson        1245698456
# antonio         123456456
# carlos          91257581
# cesar           987458
# rosemary        789456125
# Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere 
# um relatório, chamado "relatório.txt", no seguinte formato:

# ACME Inc.               Uso do espaço em disco pelos usuários
# ------------------------------------------------------------------------
# Nr.  Usuário        Espaço utilizado     % do uso

# 1    alexandre       434,99 MB             16,85%
# 2    anderson       1187,99 MB             46,02%
# 3    antonio         117,73 MB              4,56%
# 4    carlos           87,03 MB              3,37%
# 5    cesar             0,94 MB              0,04%
# 6    rosemary        752,88 MB             29,16%

# Espaço total ocupado: 2581,57 MB
# Espaço médio ocupado: 430,26 MB
# O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar 
# a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função 
# separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função,
# que será chamada pelo programa principal.
list_users        = list()
list_space_MB     = list()
list_percent_used = list()
list_file_lines   = list()
avarage_space     = 0
def readUsersFile():
    arq               = open("./exerciciosLista/usuarios.txt")
    linhas            = arq.readlines()

    for linha in linhas:
        list_users.append(linha[:15]) # pega do 1º ao 15º caracter
        list_space_MB.append(float(int(linha[16:].replace("\n",""))/1000000)) # pega do 16º ao fim da string

    sum = calcSum(list_space=list_space_MB)
    
    i=0
    for i in range(len(list_space_MB)):
        percent_used = list_space_MB[i]*100 / sum
        list_percent_used.append(format(percent_used, '.2f'))

    writeReportFile(sum, list_space_MB, list_users, list_percent_used)
    
  
def calcSum(list_space):
    sum = 0
    for i in range(len(list_space_MB)):
        sum += list_space_MB[i]
    return sum
    
def writeReportFile(sum, list_space, list_users, list_percent_used):
    list_file_lines.append("ACME Inc.               Uso do espaço em disco pelos usuários\n")
    list_file_lines.append("------------------------------------------------------------------------\n")
    list_file_lines.append("Nr.  Usuário        Espaço utilizado     % do uso\n")
    for i in range(len(list_space)):
        space_MB = format(list_space[i], '.2f')
        line = str(f"{i+1}    {list_users[i]}      {space_MB} MB           {list_percent_used[i]}%\n")
        list_file_lines.append(line)
    list_file_lines.append("Espaço total ocupado: {:.2f} \n".format(sum))
    list_file_lines.append("Espaço médio ocupado: {:.2f} \n".format(sum/len(list_users)))
    report_file = open("./exerciciosLista/relatório.txt","w",encoding='utf-8')
    
    for linha in list_file_lines:
        report_file.write(linha)
readUsersFile()