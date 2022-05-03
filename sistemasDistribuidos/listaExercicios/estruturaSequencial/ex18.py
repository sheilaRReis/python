# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade 
# de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do 
# arquivo usando este link (em minutos).
def ex18():
    invalid_value = True
    file_size = 0
    internet_speed = 0

    while(invalid_value):
        try:
            file_size = float(input("Digite o tamanho do arquivo (em MB): ").strip().replace(",", "."))
            internet_speed = float(input("Digite a velocidade do link de Internet (em Mb): ").strip().replace(",", "."))
            invalid_value = False
        except(ValueError):
            invalid_value = True
            print("Valor inválido! Tente novamente.")

    file_size_mb = file_size*8
    print(f"O download do arquivo será feito em {file_size_mb/internet_speed} segundos")

