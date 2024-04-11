capacidade_atual, aumento_percentual = map(int, input().split())

# TODO: Calcule a nova capacidade do disco de Mithril
def calcular_capacidade(capacidade, percentual):
    nova_capacidade = capacidade + ((percentual / 100) * capacidade)

    return int(nova_capacidade)

# TODO: Imprima a nova capacidade

print(calcular_capacidade(capacidade_atual, aumento_percentual))
