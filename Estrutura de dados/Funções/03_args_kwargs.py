# *args // recebe valores como uma tupla
# **kwargs // recebe valores como um dicionário


def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)


exibir_poema(
    "Zen of Python",
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",
    autor="Tim Peters",
    ano=1999,
)

def exibir_informacoes_anime(nome_anime, *personagens, **avaliacao):
    lista_personagens = "\n".join(personagens)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in avaliacao.items()])
    mensagem = f"{nome_anime}\n\n{lista_personagens}\n\n{meta_dados}"
    print(mensagem)

exibir_informacoes_anime(
     # (nome_anime)
    "One Piece",

    # (tupla *personagens)
    "Monkey D. Luffy", 
    "Roronoa Zoro",
    "Nami",
    "Usopp",
    "Sanji Vinsmoke",
    "Tony Tony Chopper",
    "Nico Robin",
    "Franky",
    "Brook",
    "Jinbe",
    "Gol D. Roger",
    "Portgas D. Ace",
    "Trafalgar D. Water Law",
    "Eustass Kid",
    "Charlotte Katakuri",
    "Boa Hancock",
    "Marshall D. Teach (Barba Negra)",
    "Buggy",
    "Shanks",
    "Dracule Mihawk",

    #(dicionário, pois tem chave e valor **avaliacao)
    pontuacao = "10,0",
    avaliacao = "Muito Bom!"
)


exibir_informacoes_anime(
     # (nome_anime)
    "Naruto",

    # (tupla *personagens)
    "Uzumaki Naruto",
    "Uchiha Sasuke",
    "Haruno Sakura",
    "Hatake Kakashi",
    "Hyuga Hinata",
    "Gaara",
    "Rock Lee",
    "Tenten",
    "Hyuga Neji",
    "Inuzuka Kiba",
    "Akimichi Choji",
    "Yamanaka Ino",
    "Nara Shikamaru",
    "Aburame Shino",
    "Temari",
    "Kankuro",
    "Orochimaru",
    "Tsunade",
    "Jiraiya",
    "Minato Namikaze",

    #(dicionário, pois tem chave e valor **avaliacao)
    pontuacao = "9,0",
    avaliacao = "Bom!"
)
