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
plt.title('Proportion of Movies and Series')
plt.ylabel('') 
plt.show()

plt.figure(figsize=(14, 7))
sns.countplot(data=df, x='release_year', hue='type', palette='Set2', order=sorted(df['release_year'].dropna().unique()))
plt.title('Distribution of Movies and Series by Release Year')
plt.xlabel('Release Year')  
plt.ylabel('Count')  
plt.xticks(rotation=90)
plt.show()

yearly_additions = df.groupby(['year_added', 'type']).size().unstack()
yearly_additions.plot(kind='bar', stacked=True, figsize=(14, 7), color=["#66c2a5", "#fc8d62"])
plt.title('Additions of Movies and Series Over Time')
plt.xlabel('Year Added')  
plt.ylabel('Number of Titles')  
plt.legend(title='Content Type')
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='rating', hue='rating', palette='viridis', order=df['rating'].value_counts().index, legend=False)
plt.title('Distribution of Ratings')
plt.xlabel('Rating')  
plt.ylabel('Count')  
plt.xticks(rotation=45)
plt.show()

rating_type = pd.crosstab(df['rating'], df['type'])
rating_type.plot(kind='bar', stacked=True, figsize=(12, 7), color=["#66c2a5", "#fc8d62"])
plt.title('Distribution of Ratings by Content Type')
plt.xlabel('Rating')  
plt.ylabel('Number of Titles')  
plt.legend(title='Content Type')
plt.xticks(rotation=45)
plt.show()

filmes = df[df['type'] == 'Movie']
series = df[df['type'] == 'TV Show']

plt.figure(figsize=(12, 6))
sns.histplot(filmes['duration_num'], kde=True, color='blue', label='Movies')
sns.histplot(series['duration_num'], kde=True, color='green', label='Series')
plt.title('Duration Distribution: Movies vs Series')
plt.xlabel('Duration (minutes or seasons)')  
plt.legend()
plt.show()
