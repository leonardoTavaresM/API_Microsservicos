dic = {
    "alimentos": {
        "pizzas": ["margueritta", "mussarella",
                   "frango com catupiry", "portuguesa"],
        "bolos": ("floresta negra",
                  "red velvet",
                  "de laranja", "dá vó"),
        "calorias": {
            "leite": 129, "fatia pizza": 320,
            "agua": 0, "maça": 95
        }
    },
    "linguagens": [
        {"nome": "javascript", "criacao": 1996,
         "paradigma": ["eventos", "funcional"]},
        {"nome": "python", "criacao": 1991,
         "paradigma": ["orientada a objetos", "estruturada"]},
        {"nome": "haskell", "criacao": 1990,
         "paradigma": ["funcional"]}
    ]
}

# Só se aprende fazendo. PAUSE O VIDEO E TENTE RESPONDER!
# Se possível, FAÇA JUNTO NO SEU COMPUTADOR

# 1. quantas chaves tem o dicionario dic?
# print("r1", len(dic))  # 2

# 2. dic['linguagens'] é uma tupla, um dicionário ou uma lista?
# print("r2", type(dic['linguagens']))  # lista

# 3. Como eu faço para mostrar todos os bolos?
# (escreva o código!) #dic['alimentos']['bolos']

# 4. Qual o tipo da lista de todos os bolos?
# print("r4", type(dic['alimentos']['bolos']))  # tuple

# 5. O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
# print("r5", dic["linguagens"]["javascript"]["criacao"]) #nao existe a chave javascript, e nao se pode acessar uma lista pelo valor,
# primeiro teria que colocar [0] e depois verificar se existe js = print("r5", dic["linguagens"]["javascript"]["criacao"])

# 6 O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
# ele da um False, pois vc esta verificanso se dictionary == string
# print("r6", dic["linguagens"][2] == "haskell")


# 7 O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
# False, pois mussarella esta na posição 1
# print("r7", dic["alimentos"]["pizzas"][2] == "mussarella")

# 8 O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
# False #print("r8", 1996 in dic['linguagens'][0].values())
# print("r8", 1996 in dic['linguagens'][0])

# 9 O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
# print("r9", "criacao" in dic['linguagens'][0])  # True #é chave


# 9 O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
# print("ex9b", "pudim" in dic["sobremesas"]["doces"]) # da erro, pois sobremesas nao existe, muito menos doces

# 10 Escreva uma função "mais velha" que
# recebe um dicionário como dic e
# retorna (isso é diferente de imprimir!) a linguagem de programação mais velha da nossa lista


def get_old_language(dic):
    lista_linguagens = dic['linguagens']
    ling_velha = lista_linguagens[0]
    for linguagem in lista_linguagens:
        if linguagem['criacao'] < ling_velha['criacao']:
            ling_velha = linguagem
        return ling_velha


# print(get_old_language(dic))


# 11 Escreva uma função que retorna uma lista (sem repetições) de paradigmas de linguagens de programação

def get_list_paradigms(dic):
    lista_linguagens = dic['linguagens']
    list = []

    for linguagem in lista_linguagens:
        lista_paradigmas = linguagem['paradigma']
        for paradigma in lista_paradigmas:
            if paradigma not in list:
                list.append(paradigma)
    return list


# print(get_list_paradigms(dic))


# dic = {
#     "musicas": [
#       {"nome": 'Hey Jude', 'banda': 'Beatles'},
#       {"nome": 'November Rain', 'banda': "Guns N' Roses"},
#       {"nome": 'How Deep Is Your Love', 'banda': 'Bee Gees'}
#     ],
#     "filmes": {
#         "X-men": ["Wolverine", "Xavier", "Tempestade", "Vampira", "Magneto", "Ciclope", "Gambit"],
#         "Avengers": ["Homem de Ferro", 'Hulk', "Thanos", "Capitão", "Thor", "Capitã Marvel", "Homem-Aranha"],
#         "Star Wars": ['Luke', "Leia", "C-3PO", "Darth Vader", "Obi-Wan", "Yoda", "R2-D2", "Han Solo", "Chewbacca"]
#     }
# }


# def func1(a, b, c, d):
#     for x in a:
#         if x[b] == d:
#             return x[c]
#     return 'naosei'


# print('1', dic["filmes"]["Star Wars"][2] == "Leia")
# print('2', "Han Solo" in dic["filmes"]["Star Wars"])
# # print('3', func1(dic, ["filmes"], ["musicas"], "Avengers", "Capitão América"))
# print('4', func1(dic["musicas"], "banda", "nome", "Hey Jude") == "Beatles")
# print('5', "Hey Jude" == dic["musicas"][0])
# # print('6', "Han Solo" in dic["jogos"]["Mortal Kombat II"])
# print('7', dic["filmes"]["X-men"][3] == "Vampira")
# print('8', "Thor" in dic["filmes"]["Avengers"])
# # print('9', dic[dic] + dic[dic[dic]])
# print('10', dic["musicas"][0]["banda"] == "Beatles")
# print('11', dic["musicas"][2]["nome"] == "How Deep Is Your Love")
# # print('4',"Chewbacca" in dic.filmes.Star Wars)
# # print('13', dic["musicas"]["Bee Gees"] == "How Deep Is Your Love")
# print('14', func1(dic["musicas"], "banda", "nome",
#       "Guns N' Roses") == "November Rain")
# print('15', "Super-homem" in dic["filmes"]["Avengers"])
# print('16', func1(dic["filmes"], 1, 2, "Homem de Ferro"))
# print('17', "November Rain" == dic["musicas"][1]["banda"])
# print('18', "Homem de Ferro" in dic["musicas"][2])
# # print('19', "Han Solo" in dic["jogos"]["Star Wars"])
# # print('20', "Hey Jude" in dic["musicas"]["Beatles"])
