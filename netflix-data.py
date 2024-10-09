import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

df = pd.read_csv('netflix_titles.csv')
df.drop_duplicates(inplace=True)
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

df['year_added'] = df['date_added'].dt.year

df['duration_num'] = df['duration'].str.extract(r'(\d+)').astype(float)

type_counts = df['type'].value_counts()
plt.figure(figsize=(6, 6))
type_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=["#66c2a5", "#fc8d62"])
plt.title('Proporção de Filmes e Séries')
plt.ylabel('')
plt.show()

plt.figure(figsize=(14, 7))
sns.countplot(data=df, x='release_year', hue='type', palette='Set2', order=sorted(df['release_year'].dropna().unique()))
plt.title('Distribuição de Filmes e Séries por Ano de Lançamento')
plt.xlabel('Ano de Lançamento')
plt.ylabel('Quantidade')
plt.xticks(rotation=90)
plt.show()

yearly_additions = df.groupby(['year_added', 'type']).size().unstack()
yearly_additions.plot(kind='bar', stacked=True, figsize=(14, 7), color=["#66c2a5", "#fc8d62"])
plt.title('Adições de Filmes e Séries ao Longo do Tempo')
plt.xlabel('Ano de Adição')
plt.ylabel('Número de Títulos')
plt.legend(title='Tipo de Conteúdo')
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='rating', hue='rating', palette='viridis', order=df['rating'].value_counts().index, legend=False)
plt.title('Distribuição das Classificações (Ratings)')
plt.xlabel('Classificação')
plt.ylabel('Quantidade')
plt.xticks(rotation=45)
plt.show()

rating_type = pd.crosstab(df['rating'], df['type'])
rating_type.plot(kind='bar', stacked=True, figsize=(12, 7), color=["#66c2a5", "#fc8d62"])
plt.title('Distribuição de Ratings por Tipo de Conteúdo')
plt.xlabel('Classificação')
plt.ylabel('Número de Títulos')
plt.legend(title='Tipo de Conteúdo')
plt.xticks(rotation=45)
plt.show()

filmes = df[df['type'] == 'Movie']
series = df[df['type'] == 'TV Show']

plt.figure(figsize=(12, 6))
sns.histplot(filmes['duration_num'], kde=True, color='blue', label='Filmes')
sns.histplot(series['duration_num'], kde=True, color='green', label='Séries')
plt.title('Distribuição de Duração: Filmes vs Séries')
plt.xlabel('Duração (minutos ou temporadas)')
plt.legend()
plt.show()
