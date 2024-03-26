import requests


# faça uma função usando a biblioteca requests
# que acessa a URL /corredores do servidor de corredoes
# via GET, e devolve uma lista de todos os corredores


def todos_corredores():
  url = "http://127.0.0.1:5000/corredores"
  r = requests.get(url)
  json = r.json()
  return json

# faça uma função usando a lib request
# que acessa a URL / corredores do servidor de corredores
# via Post, enviando um dicionario de uym novo corredor
# Um corredor tem campos "nome", "tempo" e "id"

def adiciona_corredor(nome, tempo, id):
  url = "http://127.0.0.1:5000/corredores"

  body = {
    "id" : id,
    "nome" : nome,
    "tempo" : tempo
  }

  r = requests.post(url, json = body )
  if r: 
    return { "res": True, "corredor": body}
  
  return False

# faça uma função usando a lib requests
# que acessa a URL /corredores/maior_tempo do servidor
# de todos_corredores via GET, e retorne o nome do corredor mais lento

def corredor_mais_lento():
  url = "http://127.0.0.1:5000/corredores/maior_tempo"
  r = requests.get(url)
  json = r.json()
  nome = json["nome"]
  return nome

# faça uma função usando a biblioteca requests
# que acessa a URL /corredores/maior_tempo do servidor
# de corredoes
# via DELETE, causando a remoção dos dados do corredor
# mais lento.
# Infelizmente o servidor tem um bug no caso em que a lista
# de corredores está vazia, mas vamos tratar esse bug
# no nosso cliente


def deleta_mais_lento():
  url = "http://127.0.0.1:5000/corredores/maior_tempo"
  r = requests.delete(url)
  
  if r.status_code == 500:
    return "Não é possivel remover de uma lista vazia"
  
  return True

# porque a funcionalidade anterior consiste em um erro
# de design no servidor corredores?

# R: o verbo Delete devia ser iDEMPOTENTE
# deveria ser o caso que a segunda chamada nao causa novo efeito colateral
# IDEMPOTENTE significa que, quando eu chamo a primeira vez, ele deleta, na segunda, não


# faça uma função usando a biblioteca requests
# que acessa a URL /corredores/ID do servidor
# de corredores, onde ID é um código numérico.
# O acesso ocorrerá via GET,
# sua função deve retornar o nome do corredor em questão
# o o seu melhor tempo, em uma tupla

def busca_corredor(id):
  url = f"http://127.0.0.1:5000/corredores/{id}"

  r = requests.get(url)
  if r.status_code == 404:
    return "corredor nao existe"
  json = r.json()

  nome = json["corredor"]["nome"]
  tempo = json["corredor"]["tempo"]

  return (nome, tempo)

#como eu trataria o erro 404 e informaria o meu usuário?

# R: eu puxo o status da resposta, e se for 404, eu retorno ao usuario uma mensagem de erro


# faça uma função usando a biblioteca requests
# que acessa a URL /corredores/ID do servidor
# de corredores, onde ID é um código numérico.
# O acesso ocorrerá via DELETE,
# causando a remoção dos dados do corredor
# mais lento


def deleta_mais_lento_por_id(id):
  url = f"http://127.0.0.1:5000/corredores/{id}"

  r = requests.delete(url)
  if r.status_code == 404:
    return r.json()['status']
  
  return "ok"

# faça uma função usando a biblioteca requests
# que acessa a URL /corredores/ID do servidor
# de corredores, onde ID é um código numérico.
# O acesso ocorrerá via PUT,
# e você deverá enviar um dicionário com o novo tempo,
# para atualizar
# o tempo atual do corredor. O tempo deverá ser menor
# do que o tempo atual, caso contrário, o servidor
# lançará um erro, que você deve tratar

def atualiza_corredor(id, tempo):
  url = f"http://127.0.0.1:5000/corredores/{id}"

  r = requests.put(url, json = {"tempo": tempo })
  if r.status_code == 400:
    return r.json()['status']
  if r.status_code == 404:
    return r.json()['status']
  
  return "ok"