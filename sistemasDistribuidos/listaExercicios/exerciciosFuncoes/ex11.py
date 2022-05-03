# Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma
# string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data 
# seja inválida.
import datetime

def getValidDate():
    invalid_date_input     = True
    while(invalid_date_input):
        input_date = input("Favor informar a data, no formato DD/MM/AAAA:").strip()
        if(len(input_date)<8):
            print("Data inválida! Tente novamente!")
            invalid_date_input = True
        else:
            if(input_date.count("/")==2):
                invalid_day_input      = False
                invalid_month_input    = False
                invalid_year_input     = False
                split = input_date.split("/")
                input_day   = int(split[0])
                input_month = int(split[1])
                input_year  = int(split[2])
                    
                if(input_day<1 or input_day>31):
                    print("Dia inválido! Tente novamente")
                    invalid_day_input = True
               
                if(input_month<1 or input_month>12):
                    print("Mês inválido! Tente novamente")
                    invalid_month_input = True

                if(input_year<1 or input_year>9999):
                    print("Ano inválido! Tente novamente")
                    invalid_year_input = True

                invalid_date_input = invalid_day_input or invalid_month_input or invalid_year_input
            else:
                print("Data inválida! Tente novamente!")
                invalid_date_input = True
        if not invalid_date_input:
            valid_date = ''
            try:
                valid_date = datetime.date(year=input_year,month=input_month,day=input_day)
            except(ValueError):
                print("Data inválida! Tente novamente!")
                invalid_date_input = True
            
    return valid_date

def printMonth(month):
    match month:
        case 1:
            print("Janeiro",end=" de ")
        case 2:
            print("Fevereiro",end=" de ")
        case 3:
            print("Março",end=" de ")
        case 4:
            print("Abril",end=" de ")
        case 5:
            print("Maio",end=" de ")
        case 6:
            print("Junho",end=" de ")
        case 7:
            print("Julho",end=" de ")
        case 8:
            print("Agosto",end=" de ")
        case 9:
            print("Setembro",end=" de ")
        case 10:
            print("Outubro",end=" de ")
        case 11:
            print("Novembro",end=" de ")
        case 12:
            print("Dezembro",end=" de ")

def main():
    valid_date = getValidDate()
    if(valid_date!=''):
        day        = valid_date.day
        month      = valid_date.month
        year       = valid_date.year
        print(day,end=" de ")
        printMonth(month=month)
        print(year)

main()