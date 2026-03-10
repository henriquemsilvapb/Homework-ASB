import sys
import requests

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

#Analisa os argumentos passados diretamente pela linha de comandos

def analisar_arg(args):
    if len(args) != 2:
        print("Usage: python fetch_sequences.py <database> <query>", file=sys.stderr)
        sys.exit(1)
    return args

#Recebe "database" e "query" e devolve um dicionario json 

def esearch(database, query):
    url = BASE_URL + "esearch.fcgi"
    params = {
        "db": database,
        "term": query,
        "usehistory": "y",
        "retmode": "json",
    }
    resposta = requests.get(url, params=params)
    data = resposta.json()
    resultado = data["esearchresult"]
    webenv = resultado["webenv"]
    query_key = resultado["querykey"]
    return webenv, query_key

#Transforma esse mesmo dicionario em um Ficheiro Fasta , De modo a ser lido transformamos em txt 

def efetch(database, webenv, query_key):
    url = BASE_URL + "efetch.fcgi"
    params = {
        "db": database,
        "query_key": query_key,
        "WebEnv": webenv,
        "rettype": "fasta"
    }
    resposta = requests.get(url, params=params)
    return resposta.text

if __name__ == "__main__":
    database, query = analisar_arg(sys.argv[1:])
    webenv, query_key = esearch(database, query)

    print(efetch(database, webenv, query_key))