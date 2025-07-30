import subprocess

def executar_notebook(caminho_notebook):
    cmd = [
        "jupyter", "nbconvert",
        "--to", "notebook",
        "--execute",
        "--inplace",  # salva no mesmo arquivo
        caminho_notebook
    ]
    subprocess.run(cmd, check=True)

# criar banco de dados
executar_notebook("notebooks/ETL/camada_bronze.ipynb")
executar_notebook("notebooks/ETL/camada_silver.ipynb")
executar_notebook("notebooks/ETL/camada_gold.ipynb")

# Treinar modelo de segmentação de clientes
executar_notebook("models/clusterizacao_cliente/feature_engineering.ipynb")
executar_notebook("models/clusterizacao_cliente/train.ipynb")
executar_notebook("models/clusterizacao_cliente/inference.ipynb")

# Treinar modelo de previsão de consumo
executar_notebook("models/previsao_consumo/feature_engineering.ipynb")
executar_notebook("models/previsao_consumo/train.ipynb")
executar_notebook("models/previsao_consumo/inference.ipynb")