# Uma biblioteca mantém uma lista de livros emprestados, onde cada item é representado por
# [titulo, usuario, dias_emprestado].
# Exemplo:
# [
#  ["Dom Casmurro", "Ana", 5],
#  ["1984", "Carlos", 12],
#  ["O Hobbit", "Marina", 3]
# ]
# O sistema precisa:
# 1. Listar apenas os livros que estão emprestados há mais de 7 dias.
# 2. Encontrar o livro emprestado há mais tempo.
# 3. Gerar uma lista apenas com os nomes dos usuários que têm livros emprestados.
# 4. Calcular a média de dias de empréstimo.


livros =[
    {
        "nome":"Dom Casmurro",
        "usuario" : "Ana",
        "dias_emprestados": 5
    },
    {
        "nome":"1984",
        "usuario":"Carlos",
        "dias_emprestados" : 12
    },
    {
        "nome": "O Hobbit",
        "usuario":"Mariana",
        "dias_emprestados":3
    }
]
emprestados = []
lista_dias = []
lista_usuario_ativos = []
soma=0
for i in livros:
    lista_dias.append(i["dias_emprestados"])
    if i["dias_emprestados"] > 0:
        lista_usuario_ativos.append(i["usuario"])
    if i["dias_emprestados"] > 7:
        emprestados.append(i["nome"])
maior_tempo_emprestado = max(lista_dias)
for i in livros:
    if i["dias_emprestados"] == maior_tempo_emprestado:
        livro_mais_tempo = i["nome"]
for i in livros:
    soma = soma + i["dias_emprestados"]
media = soma / len(livros)


print(f"Os livros emprestados a mais de 7 dias são :{emprestados}\n Os usuarios com algum livros emprestados são :{lista_usuario_ativos}\n O livro que está a mais tempo emprestado é {livro_mais_tempo}\n A média dos dias emprestados é {media} dias")