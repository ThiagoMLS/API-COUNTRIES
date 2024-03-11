import json
import sys 

import requests

URL_ALL = "https://restcountries.com/v2/all"
URL_NAME = "https://restcountries.com/v2/name"

def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
        
    except Exception as error:
        print("Erro ao fazer a requisição em:",url)
        print(error)


def parsing(texto_da_resposta):
    try:
        return json.loads(texto_da_resposta) # PARSING DE JSON PARA PYTHON

    except Exception as error:
        print("Erro ao fazer parsing")
        print(error)


def contagem_de_paises():
    resposta = requisicao(URL_ALL)
    
    if resposta:
        lista_de_paises = parsing(resposta)

        if lista_de_paises:
            return len(lista_de_paises)


def listar_paises(lista_de_paises):
    for pais in lista_de_paises:
        print(pais["name"])


def mostrar_populacao(nome_do_pais):
    resposta = requisicao(f"{URL_NAME}/{nome_do_pais}")
    
    if resposta:
        lista_de_paises = parsing(resposta)

        if lista_de_paises:

            for pais in lista_de_paises:
                print(f"{pais['name']} : {pais['population']} habitantes")

    else:
        print("País não encontrado")


def mostrar_moedas(nome_do_pais):
    resposta = requisicao(f"{URL_NAME}/{nome_do_pais}")
    
    if resposta:
        lista_de_paises = parsing(resposta)

        if lista_de_paises:

            for pais in lista_de_paises:
                print(">>> Moedas do",pais["name"],":")
                moedas =  pais['currencies']

                for moeda in moedas:
                    print(f"-- {moeda['name']} - {moeda['code']}")

    else:
        print("País não encontrado")


def mostrar_capital(nome_do_pais):
    resposta = requisicao(f"{URL_NAME}/{nome_do_pais}")
    
    if resposta:
        lista_de_paises = parsing(resposta)

        if lista_de_paises:

            for pais in lista_de_paises:
                print(f"{pais['name']} : {pais['capital']}")

    else:
        print("País não encontrado")


def ler_nome_do_pais():
    try:
        nome_do_pais = argumento2 = sys.argv[2]
        return nome_do_pais
    except:
        print("É preciso passar o nome do país")


if __name__ == "__main__":

    if len(sys.argv) == 1:
        print("--"*5,"Bem-vindo ao sistema de países","--"*5)
        print("Uso: python paises.py <ação> <nome_do_país>")
        print("Ações disponíveis: contagem, moeda, populacao, capital")
    
    else:
        argumento1 = sys.argv[1]

        if argumento1 == "contagem":
            numero_de_paises = contagem_de_paises()
            print(f"Existem {numero_de_paises} países no mundo todo.")

        elif argumento1 == "moeda":
            pais = ler_nome_do_pais()
            if pais:
                mostrar_moedas(pais)

        elif argumento1 == "populacao":
            pais = ler_nome_do_pais()
            if pais:
                mostrar_populacao(pais)

        elif argumento1 == "capital":
            pais = ler_nome_do_pais()
            if pais:
                mostrar_capital(pais)

        else:
            print("Argumento inválido")

    