import requests
import os

dictionary = {} #Criando dicionário para guardar todos os dados

url = 'https://timeapi.io/api/Time/current/zone?timeZone=America/Sao_Paulo' #salvando o site que tem a informação
resultado = requests.get(url)                #Pedindo a informação
temporario = resultado.text                  #pegando o texto no site
print(temporario)

#Filtragem Bruta e formatação da string para transformar em dicionário
temporario = temporario.replace('{', '')
temporario = temporario.replace('}', '')
temporario = temporario.replace('"', '')
html_page = temporario.split(',')            #divide a string para fazer cada item um ponto no dicionário

#Criação do dicionário
for i in html_page:
    temporario = i.split(':', 1)
    dictionary[temporario[0]] = temporario[1]
    #print(temp)

#formatação final
temporario = dictionary['dateTime']
Tempo = temporario.split('T')
Tempo[1] = Tempo[1].replace(Tempo[1][Tempo[1].find('.'):], '')

#Seta variáveis de saída
data = ano,mes,dia = Tempo[0].split('-')
horario = Tempo[1]

#Envia no prompt os horários finais
print(f'{dia}-{mes}-{ano}')
print(horario)

#Altera o horário
os.system("date %s" % f'{dia}-{mes}-{ano}')
os.system("time %s" % horario)
