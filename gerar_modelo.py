from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from joblib import dump


caminho_arquivo = 'dados.xlsx'
dados = pd.read_excel(caminho_arquivo)


df = pd.DataFrame(dados)


encoder = OneHotEncoder()
X = encoder.fit_transform(df.drop('Risco', axis=1))
y = df['Risco'].map({'Alto': 2, 'Moderado': 1, 'Baixo': 0}).values


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


dt_classifier = DecisionTreeClassifier(random_state=42)
dt_classifier.fit(X_train, y_train)


print(df)


dump(dt_classifier, 'modelo.joblib')
dump(encoder, 'encoder.joblib')