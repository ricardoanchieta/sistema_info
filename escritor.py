import csv
import re

def tratamento(string):
  string_nova = re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ. ]', '', string)
  return string_nova

# 1. abrir o arquivo
with open('netflix/netflix_titles.csv', encoding='utf-8') as arquivo_referencia:

  # 2. ler a tabela
    tabela = csv.reader(arquivo_referencia, delimiter=',')
    cont = 1
  # 3. navegar pela tabela
    #string_velha = '11/22/63: A Novel.txt'
    #string_nova = re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ. ]', '', string_velha)
    #print(string_nova)
    
    
    for l in tabela:
        col1 = l[0]
        col1 = tratamento(col1)
        nome = l[2]
        string_velha = nome
        string_nova = re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ. ]', '', string_velha)
        col2 = l[1]
        col2 = tratamento(col2)
        col4 = l[3]
        col4 = tratamento(col4)
        col5 = l[4]
        col5 = tratamento(col5)
        col6 = l[5]
        col6 = tratamento(col6)
        col7 = l[6]
        col7 = tratamento(col7)
        col8 = l[7]
        col8 = tratamento(col8)
        col9 = l[8]
        col9 = tratamento(col9)
        col10 = l[9]
        col10 = tratamento(col10)
        print(nome)
        print(l[0] + ', ' + l[1] + ', ' + l[2]  + ', ' + l[3] + ', ' + l[4] + ', ' + l[5] + ', ' + l[6])
        arquivo = open(string_nova +'.txt', 'w')
        arquivo.write(col1+'\n')
        arquivo.write(col2+'\n')
        arquivo.write(string_nova+'\n')
        arquivo.write(col4+'\n')
        arquivo.write(col5+'\n')
        arquivo.write(col6+'\n')
        arquivo.write(col7+'\n')
        arquivo.write(col8+'\n')
        arquivo.write(col9+'\n')
        arquivo.write(col10+'\n')
        print("Contador:")
        print(cont)
        cont = cont +1
        arquivo.close()
    
   
  #print(tabela[1][1])

#with open('bestsellers with categories.csv') as csv_file:
#    
#    csv_reader = csv.reader(csv_file, delimiter=',')

    #csv_reader.__next__()

#    for row in csv_reader:
#        print( row[0] + ', ' + row[1] + ', ' + row[2] )
#        break