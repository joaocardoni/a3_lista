# Uma loja online registra o número de vendas de cada dia do mês em uma lista.
# • Exemplo: [10, 15, 20, 5, 0, 8, ...]
# O gerente precisa:
# 1. Calcular o total de vendas no mês.
# 2. Descobrir o dia com mais vendas e o dia com menos vendas.
# 3. Calcular a média de vendas por dia.
# 4. Listar os dias que tiveram vendas acima da média.

dias = {
    "1" : 10,
    "2" : 15,
    "3":20,
    "4":5,
    "5":0,
    "6":8
}


tamanho = len(dias)

chaves = list((dias.values()))
keys = []
for i in chaves:
    keys.append(int(i))
for i in keys:
    i = int(i)
soma=0
for i in keys:
    soma = soma + i
media = soma / (tamanho)
maior_venda = max(keys)
menor_venda = min(keys)
dia_maior_venda = 0
dia_menor_venda = 0

media = soma / tamanho
lista_maior_media = []
for i in range(tamanho):
    letra = str(i+1)
    print(letra)
    if dias[letra] == maior_venda:
        dia_maior_venda = i+1
    elif dias[letra] == menor_venda:
        dia_menor_venda = i+1
    if dias[letra] > media:
        lista_maior_media.append(i+1)


media = soma / tamanho


print(f"O total de vendas foram {soma} vendas\n O dia com maior venda foi {dia_maior_venda}\n o dia com menor venda foi {dia_menor_venda}\n a media de vendas foram {media}\n a lista de dias acima da media de vendas é: {lista_maior_media}")