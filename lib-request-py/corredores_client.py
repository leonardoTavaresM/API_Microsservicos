import requests
from pprint import pprint 


# faça uma função usando a biblioteca requests
# que acessa a URL /corredores do servidor de corredoes
# via GET, e devolve uma lista de todos os corredores


def todos_corredores():
  url = 'http://localhost:5000/corredores'
  #conectar na URL usando o verbo GET
  response = requests.get(url)
  json = response.json()
  return json



# faça uma função usando a biblioteca requests
# que acessa a URL /corredores do servidor de corredoes
# via POST, enviando um dicionário de um novo corredor.
# Um corredor tem os campos "nome", "tempo" e "id"

def adiciona_corredores(nome, tempo, id):
  url = 'http://localhost:5000/corredores'
  body = { "nome": nome, "tempo": tempo, "id": id }
  r = requests.post(url, json = body)
  print('response', r.Response)
  if r:
    return True
  else:
    return False
  



# faça uma função usando a biblioteca requests
# que acessa a URL /corredores/maior_tempo do servidor
# de corredoes
# via GET, e retorne o nome do corredor
# mais lento

def corredor_mais_lento():
  url = 'http://localhost:5000/corredores/maior_tempo'
  #conectar na URL usando o verbo GET
  response = requests.get(url)
  json = response.json()
  return json["nome"]
  


# faça uma função usando a biblioteca requests
# que acessa a URL /corredores/maior_tempo do servidor
# de corredoes
# via DELETE, causando a remoção dos dados do corredor
# mais lento.
# Infelizmente o servidor tem um bug no caso em que a lista
# de corredores está vazia, mas vamos tratar esse bug
# no nosso cliente

def deleta_corredor_mais_lento():
  url = 'http://localhost:5000/corredores/maior_tempo'
  #conectar na URL usando o verbo GET
  r = requests.delete(url)

  if r.status_code == 500:
    return "Não é possivel remover de uma lista vazia"
  
  return True

# porque a funcionalidade anterior consiste em um erro
# de design no servidor corredores?

# a função DELETE devia ser IDENPOTENTE


# faça uma função usando a biblioteca requests
# que acessa a URL /corredores/ID do servidor
# de corredores, onde ID é um código numérico.
# O acesso ocorrerá via GET,
# sua função deve retornar o nome do corredor em questão
# o o seu melhor tempo, em uma tupla


def corredor_por_id(id):
  url = f"http://localhost:5000/corredores/{id}"
  r = requests.get(url)
  json = r.json()
  if r.status_code == 404:
    return "corredor nao existe"
  nome = json['corredor']['nome']
  tempo = json['corredor']['tempo']
  
  return (nome, tempo)



#como eu trataria o erro 404 e informaria o meu usuário?


# faça uma função usando a biblioteca requests
# que acessa a URL /corredores/ID do servidor
# de corredores, onde ID é um código numérico.
# O acesso ocorrerá via DELETE,
# causando a remoção dos dados do corredor
# mais lento

def deleta_mais_lento_por_id(id):
  url = f"http://localhost:5000/corredores/{id}"
  r = requests.get(url)
 
  if r.status_code == 404:
    return "corredor nao existe"

  return True

# faça uma função usando a biblioteca requests
# que acessa a URL /corredores/ID do servidor
# de corredores, onde ID é um código numérico.
# O acesso ocorrerá via PUT,
# e você deverá enviar um dicionário com o novo tempo,
# para atualizar
# o tempo atual do corredor. O tempo deverá ser menor
# do que o tempo atual, caso contrário, o servidor
# lançará um erro, que você deve tratar


def adiciona_corredores(id, tempo):
  url = f'http://localhost:5000/corredores/{id}'
  body = { "tempo": tempo,  }
  r = requests.post(url, json = body)
  print('response', r.Response)
  if r.status_code == 400:
    return 'Tempo de envio é maior do que o tempo atual'
  if r.status_code == 404:
    return 'Corredor não encontrado'
  return 'ok'
  
