import pandas as pd
import random

# Definindo as opções para cada atributo
opcoes = {
    'Historico_Credito': ['bom', 'medio', 'ruim'],
    'Renda_Mensal': ['baixa', 'media', 'alta'],
    'Emprego': ['estavel', 'instavel', 'desempregado'],
    'Divida_Existente': ['baixa', 'media', 'alta'],
    'Valor_Emprestimo': ['baixo', 'medio', 'alto'],
    'Prazo_Emprestimo': ['curto', 'medio', 'longo'],
    'Idade': ['jovem', 'adulto', 'idoso'],
    'Educacao': ['sem_formacao', 'graduacao', 'pos_graduacao'],
    'Finalidade_Emprestimo': ['investimento', 'consumo', 'educacao', 'emergencia'],
    'Tipo_Moradia': ['propria', 'alugada', 'com_familia'],
    'Risco': ['Alto', 'Moderado', 'Baixo']
}

# Gerando 50 solicitações com valores aleatórios
dados = []
for _ in range(50):
    solicitacao = {atributo: random.choice(valores) for atributo, valores in opcoes.items()}
    dados.append(solicitacao)

# Criando um DataFrame
df = pd.DataFrame(dados)

# Salvando a base de dados em um arquivo Excel
caminho_arquivo = 'dados.xlsx'
df.to_excel(caminho_arquivo, index=False)