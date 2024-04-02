from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score, precision_score
from joblib import dump, load
import pandas as pd
import random

mapeamento_risco = {0: 'Baixo', 1: 'Moderado', 2: 'Alto'}

atributos = {
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

modelo = load('modelo.joblib')
encoder = load('encoder.joblib')

def predict_model(df):
    y_real = df['Risco'].map({'Alto': 2, 'Moderado': 1, 'Baixo': 0}).values
    df = df.drop('Risco', axis=1)
        
    dados_codificados = encoder.transform(df).toarray()
    y_pred = modelo.predict(dados_codificados)
        
    accuracy = accuracy_score(y_real, y_pred)
    precision = precision_score(y_real, y_pred, average='macro')
        
    print(f'Precision: {round(precision, 4)}\nAccuracy: {round(accuracy, 4)}')

def avaliar(nome_arquivo):
    try:
        dados_importados = pd.read_excel(nome_arquivo)
        predict_model(dados_importados)
    except Exception as e:
        print(f"Ocorreu um erro ao processar o arquivo: {e}")

def gerar_dados_aleatorios():
    dados_aleatorios = {}
    for atributo, opcoes in atributos.items():
        dados_aleatorios[atributo] = random.choice(opcoes)
    return dados_aleatorios

def teste_automatico():
    dados_teste = pd.DataFrame([gerar_dados_aleatorios() for _ in range(100)])
    predict_model(dados_teste)

def justificar_decisao(dados_codificados):
    feature_names = encoder.get_feature_names_out()
    classes = ["Baixo", "Moderado", "Alto"]
    node_indicator = modelo.decision_path(dados_codificados)
    leaf_id = modelo.apply(dados_codificados)

    feature = modelo.tree_.feature
    threshold = modelo.tree_.threshold
    node_index = node_indicator.indices[node_indicator.indptr[0]: node_indicator.indptr[1]]
    
    justificativas = []
    for node_id in node_index[:-1]:
        if leaf_id[0] == node_id:
            break
        else:
            nome_feature_codificada = feature_names[feature[node_id]]
            nome_atributo, valor_atributo = nome_feature_codificada.rsplit('_', 1)
            condicao = "não" if dados_codificados[0, feature[node_id]] <= threshold[node_id] else ""
            
            justificativa = f"{nome_atributo} {condicao} é {valor_atributo}"
            justificativas.append(justificativa.replace('_', ' '))
    
    predicao = modelo.predict(dados_codificados)[0]
    decisao_final = classes[predicao]

    justificativa_final = f"O risco foi classificado como '{decisao_final}' porque " + ", ".join(justificativas) + "."
    return justificativa_final

def coletar_dados_usuario():
    dados_usuario = {}
    for atributo, opcoes in atributos.items():
        if atributo == 'Risco':
            break
        print(f"\nQual o {atributo} do cliente:")
        for idx, opcao in enumerate(opcoes, start=1):
            print(f"{idx}. {opcao}")
        escolha = int(input("Selecione uma opção: ")) - 1
        dados_usuario[atributo] = opcoes[escolha]
    return dados_usuario

def simular_previsao(dados_usuario):
    dados_df = pd.DataFrame([dados_usuario])

    dados_codificados = encoder.transform(dados_df).toarray()

    risco_predito = modelo.predict(dados_codificados)

    risco_label = mapeamento_risco.get(risco_predito[0], "Indefinido")
    justificativa = justificar_decisao(dados_codificados)

    return risco_label, justificativa

def main():
    print("[1] Predizer manualmente\n[2] Gerar testes automáticos\n[3] Importar base de dados .xlsx\nSelecione uma opção: ")
    while True:
        try:
            opcao = int(input())
            if opcao not in [1, 2, 3]:
                raise ValueError
            break
        except ValueError:
            print("Opção inválida. Digite 1, 2 ou 3.")

    if opcao == 1:
        dados_usuario = coletar_dados_usuario()
        resultado = simular_previsao(dados_usuario)
        print(f"\nRisco predito: {resultado[0]}")
        print(resultado[1])
    elif opcao == 2:
        teste_automatico()
    elif opcao == 3:
        nome_arquivo = input("Digite o nome do arquivo (incluindo '.xlsx'): ")
        avaliar(nome_arquivo)

if __name__ == "__main__":
    main()