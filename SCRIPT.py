import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()  # Set the theme for seaborn plots

# Determine the data path: local if available, remote otherwise
data_path ='https://raw.githubusercontent.com/Bruuno1701/Projeto-DECD/main/'

# Load the dataset, presumably service orders based on the file name
service_orders_df = pd.read_csv(data_path + '15-ordens-de-servico.csv', index_col=False, sep=';')

# Display the first few rows of the dataframe to verify it's loaded correctly
print(service_orders_df.head())
