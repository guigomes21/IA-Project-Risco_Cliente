
# Análise de Risco do Cliente

## Introdução

Este projeto visa realizar a análise de risco de clientes usando uma base de dados pronta ou criando uma nova através de um script Python inclusivo. O projeto emprega o algoritmo C4.5 para conduzir análises, realizar cálculos, e construir uma árvore de decisão para avaliar o risco associado a cada cliente.

## Instalação da Área de Execução

Para rodar este projeto, é necessário ter a versão mais recente do Python instalada na sua máquina. Além disso, algumas bibliotecas específicas são requeridas:

- `pandas`
- `joblib`
- `scikit-learn`
- `openpyxl` (opcional, caso seja necessário trabalhar com arquivos .xlsx)

Você pode instalar todas as dependências necessárias executando o seguinte comando no terminal:

```bash
pip install pandas joblib scikit-learn openpyxl
```

## Execução

Para executar o projeto, siga os passos abaixo:

1. **Geração da Base de Dados**: Caso não possua uma base de dados em formato .xlsx, execute o arquivo `gerar_base.py`. Este script gerará uma nova base de dados .xlsx para uso posterior na análise de risco.

2. **Geração do Modelo**: Em seguida, execute o arquivo `gerar_modelo.py` para gerar um modelo a partir da base de dados (criada ou pré-existente). Este modelo será utilizado nas análises subsequentes.

3. **Análise de Risco**: Finalmente, execute o arquivo `risco_banco.py`. Este script integra todas as informações e realiza a análise de risco. Você terá a opção de usar uma base de dados existente, gerar dados automaticamente, ou inserir os valores manualmente.

Sinta-se à vontade para explorar e utilizar os scripts fornecidos para a análise de risco do cliente.

## Colaboradores

- **Guilherme Oliveira Silva Gomes** | gosg@ic.ufal.br
- **Higor de Lima Gomes** | hlg@ic.ufal.br

Agradecemos o seu interesse no nosso projeto. Esperamos que ele seja útil na sua análise de risco do cliente. Caso tenha dúvidas ou sugestões, não hesite em nos contatar.