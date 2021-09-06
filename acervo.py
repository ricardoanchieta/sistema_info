import os
import math


class acervo:
    def __init__(self):
        self.data_DIR = "./biblioteca/"
        self.quant_docs = len([name for name in os.listdir(self.data_DIR) if os.path.isfile(os.path.join(self.data_DIR, name))])
        self.doc_DIR = [self.data_DIR+name for name in os.listdir(self.data_DIR) if not name[0] == '.']

    #função q retornar a quantidade de vezes q o termo pesquisado aparece no arquivo
    def TF(self,arquivo,pesquisa):
        with open(arquivo) as f:
            ocorrencia = f.read().count(pesquisa)
        return ocorrencia

    #funcao q retorna o IDF  para o calculo de peso de um termo, recendo o quantidade de documentos q contem determinado peso
    def IDF(self,pesquisa):
        quantidade = self.docsComTermo(pesquisa)
        if(quantidade == 0):
            return 0
        idf = (self.quant_docs/quantidade)
        return idf

    #função que retorna a quantidade de documentos que tem o termo pesquisado
    def docsComTermo(self,pesquisa):
        cont = 0
        for arq in self.doc_DIR:
            #print(arq)
            if self.check(arq,pesquisa)==True:
                cont=cont+1
        return cont

    #função q mostra se o termo pesquisado esta presente em determinado documento
    def check(self,arquivo,pesquisa):
        with open(arquivo) as f:
            if pesquisa in f.read():
                return True
            else:
                return False

    #calculo o peso do numero
    def peso(self,idf,tf):
        peso = tf*idf
        return peso

    def printDoc(self,arquivo):
        f = open(arquivo, 'r')
        #print('-----------------------------------------')
        codigo = f.readline()
        tipo = f.readline()
        nome = f.readline()
        autor = f.readline()
        elenco = f.readline()
        pais = f.readline()
        data_add = f.readline()
        data_lanc =  f.readline()
        nota = f.readline()
        duracao = f.readline()
        #print('-----------------------------------------')
        return codigo, tipo, nome, autor, elenco, pais,data_add,data_lanc,nota,duracao

    #SIMILARIDADE
    def similaridadeUnidade(self,busca,arquivo,idf):
        tf = self.TF(arquivo,busca)
        #define peso do doc
        pesoDoc = self.peso(tf,idf)
        #define peso de busca
        pesoBusca = (0.5+(tf/2))*idf
   
        
        sim = (pesoBusca*pesoDoc)/(math.sqrt(math.pow(pesoBusca,2)) +math.sqrt(math.pow(pesoDoc,2)) ) 
        return sim


    


#isso aqui é só um test
if __name__ == "__main__":
    pessoa1 = acervo()
    #print(pessoa1.data_DIR)
    data_DIR = "./biblioteca/"    
    doc_DIR = [data_DIR+name for name in os.listdir(data_DIR) if not name[0] == '.']
    idf = pessoa1.IDF("Philippines")
    cont = 0

    result = []
    max = 0
    for arq in doc_DIR:
        simil = pessoa1.similaridadeUnidade("Philippines",arq,idf)
        if simil > 0:
            if simil > max:
                max = simil
                result.insert(0,arq)
            else:
                result.append(arq)
            cont=cont+1
    print(result)
    print(cont)
    print(max)
    pessoa1.printDoc(result[1])