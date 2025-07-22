# [Projeto em Construção] | [Work in progress]

# 📊 Análise de Lucro de Plantações no Stardew Valley / Profit Analysis of Stardew Valley Crops

Este projeto tem como objetivo analisar os dados das plantações do jogo **Stardew Valley**, identificando as culturas mais lucrativas, os tempos de crescimento e o retorno médio por dia de cada plantação.

This project aims to analyze crop data from **Stardew Valley**, identifying the most profitable crops, growth times, and average daily returns for each crop.

---

## 🔍 Fonte dos Dados / Data Sources

Os dados principais de plantações foram obtidos do repositório [/DS-Stardew-Valley-Crops-Profit](https://github.com/Cecax27/DS-Stardew-Valley-Crops-Profit), a partir do arquivo `crops_preprocessed_data.csv`.
Além disso, foram usados dados complementares de informações específicas por estação, crescimento e colheita múltipla, coletados no dataset do Kaggle:
[Stardew Valley Spring Crop Info](https://www.kaggle.com/datasets/shinomikel/stardew-valley-spring-crop-info)

The main crop dataset was obtained from the repository [/DS-Stardew-Valley-Crops-Profit](https://github.com/Cecax27/DS-Stardew-Valley-Crops-Profit), using the file `crops_preprocessed_data.csv`.  
Additional seasonal and crop-specific information was collected from the Kaggle dataset:  
[Stardew Valley Spring Crop Info](https://www.kaggle.com/datasets/shinomikel/stardew-valley-spring-crop-info)

---

## 📌 Objetivos da Análise / Analysis Goals

- Calcular o lucro total de cada plantação.
- Determinar o lucro por dia de crescimento.
- Identificar as culturas mais rentáveis por estação. 
- Visualizar os resultados com gráficos e tabelas. [em andamento]

--

- Calculate total profit for each crop  
- Determine profit per growth day  
- Identify the most profitable crops per season  
- Visualize results using graphs and tables [in progress]

---

## 🚀 Como executar / How to run

1. Clone o repositório / Clone the repository:  
   ```bash
   git clone https://github.com/adriacode/stardew_crops_analysis.git
   ```

2. Instale as dependências / Install the dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Execute os notebooks na pasta /notebooks 
   Run the notebooks in the /notebooks folder

## 🛠️ Tecnologias Utilizadas / Technologies Used

- Python 3.10+  
- Pandas  
- Matplotlib  
- Seaborn  
- Jupyter Notebook  
