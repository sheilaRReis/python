# Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, 
# contendo um relatório dos endereços IP válidos e inválidos.
# Um endereço IPv4 possui o formato x.x.x.x, em que x é chamado de octeto e deve ser um valor decimal entre 0 e 255. 
# Os octetos são separados por pontos. Um endereço IPv4 deve conter três pontos e quatro octetos.

IPfile     = open("C:/Users/Sheila/dev/cursoExtensao_Python/python/sistemasDistribuidos/exerciciosArquivos/ips.txt")
linhas     = IPfile.readlines()
IPfile.close()
listIPs    = list()
validIPs   = list()
invalidIPs = list()
for linha in linhas:
    listIPs.append(linha.strip().replace("\n",""))

for ip_str in listIPs:
    checkValidIP = False
    ipNum        = 0
    if(ip_str.count('.')==3):
        ipSplit = (ip_str.split('.'))
        validOctCount = 0
        for i in range(0,len(ipSplit),1):
            try:
                ipNum = int(ipSplit[i])
            except ValueError:
                invalidIPs.append(ip_str)
                continue
            if(ipNum>0 and ipNum<256):
               validOctCount += 1
            else:
                invalidIPs.append(ip_str)
                continue
            if(validOctCount==len(ipSplit)):
               validIPs.append(ip_str)
               continue
    else:
        invalidIPs.append(ip_str)

report_file     = open("C:/Users/Sheila/dev/cursoExtensao_Python/python/sistemasDistribuidos/exerciciosArquivos/ipsReport.txt","w",encoding='utf-8')
list_file_lines = list()
list_file_lines.append("[Endereços válidos:]\n")
for ip in validIPs:
    list_file_lines.append("{}\n".format(ip))

list_file_lines.append("\n[Endereços inválidos:]\n")
for ip in invalidIPs:
    list_file_lines.append("{}\n".format(ip))

for linha in list_file_lines:
    report_file.write(linha)

report_file.close()