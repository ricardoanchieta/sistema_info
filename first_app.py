from logging import error
import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import time

from streamlit.type_util import data_frame_to_bytes
from acervo import acervo



def form(cont,acervo,result):
    with st.form(key="formis"):
        codigo, tipo, nome, autor = acervo.printDoc(result[cont])
        st.write("Codigo: " + codigo,"\n tipo: " + tipo, "\n nome: " + nome,"\n autor: " +autor)    
        botao_prox = st.form_submit_button(label='Proximo')
        if botao_prox:
            cont = cont + 1
            form(cont,acervo,result)

st.title('Busca em RicFlix')
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

pesquisa = acervo()
total = st.write('Acervo = ', pesquisa.quant_docs)
with st.form(key='my_form'):
    text_input = st.text_input(label='O que deseja assistir')
    submit_button = st.form_submit_button(label='Pesquisar')

    print(text_input)
    

count = 0

#if submit_button:
#    count += 1

#pesquisa = acervo()

if submit_button:
    st.text("O(s) arquivo(s) mais relevante(s) apareceram abaixo:")
    doc_DIR = pesquisa.doc_DIR
    data_DIR = pesquisa.data_DIR
    idf = pesquisa.IDF(text_input)
    if(idf == 0):
        st.write("Nenhum arquivo relevante encontrado, pesquise outra coisa !")
    else:
        docs_encontrados = 0
        cont = 0 
        max = 0
        cont2 = 0
        result = []
        vet_simi = []
        latest_iteration = st.empty()
        bar = st.progress(0)
        for arq in doc_DIR:
            simil = pesquisa.similaridadeUnidade(text_input,arq,idf)
            if simil > 0:
                if simil > max:
                    max = simil
                    result.insert(0,arq)
                    vet_simi.insert(0,simil)
                else:
                    result.append(arq)
                    vet_simi.append(simil)
                docs_encontrados=docs_encontrados+1
            # Update the progress bar with each iteration.
            latest_iteration.text(f'Procurando... {cont+1}')
            bar.progress(cont + 1)
            if(cont != 90):
                cont = cont + 1
            if(cont2 == pesquisa.quant_docs - 2):
                cont = 99
            cont2 = cont2 + 1
            print(arq)
        
    if(idf!=0):
        quant_docs = pesquisa.docsComTermo(text_input)
        st.write('Arquivos relacioandos encontrados = ', quant_docs)
        result2 = result
        cont = 0
        vetores = ["0","1","2","3","4"]
        for x in range(0,len(result2)):
            with st.form(key='my_form2'+ vetores[x]):
                codigo, tipo, nome, autor, elenco, pais,data_add,data_lanc,nota,duracao = pesquisa.printDoc(result2[x])
                st.write("Simililaridade = ", vet_simi[x],"\n Codigo: " + codigo,"\n Tipo: " + tipo, "\n Nome: " + nome,"\n Autor: " +autor,"\n Elenco: " + elenco,"\n País: "+ pais,"\n Data de Adição: " + data_add,"\n Data de Lançamento: " + data_lanc,"\n Avaliacao: "+ nota,"\n Duracao: "+duracao)
                botao_prox = st.form_submit_button(label='Ver no Netflix')
                if botao_prox:
                    st.text("Cancela pesquisa")
                if(cont == 4):
                    break
                cont = cont + 1
                
        print(text_input)

