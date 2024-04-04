import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()  # Set the theme for seaborn plots

# Determine the data path: local if available, remote otherwise
data_path ='https://raw.githubusercontent.com/Bruuno1701/Projeto-DECD/main/'

# Load each CSV file into its own DataFrame with a unique variable name
ordens_de_servico_df = pd.read_csv(data_path + '15-ordens-de-servico.csv', index_col=False, sep=';')
contadores_de_energia_df = pd.read_csv(data_path + '21-contadores-de-energia.csv', index_col=False, sep=';')
diagrama_de_carga_por_instalacao_df = pd.read_csv(data_path + '22-diagrama-de-carga-por-instalacao.csv', index_col=False, sep=';')
consumos_faturados_por_municipio_ultimos_10_anos_df = pd.read_csv(data_path + '3-consumos-faturados-por-municipio-ultimos-10-anos.csv', index_col=False, sep=';')

# Display the first few rows of each dataframe to verify they're loaded correctly
print(ordens_de_servico_df.head())
print(contadores_de_energia_df.head())
print(diagrama_de_carga_por_instalacao_df.head())
print(consumos_faturados_por_municipio_ultimos_10_anos_df.head())


