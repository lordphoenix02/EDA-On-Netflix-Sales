# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
df1 = pd.read_csv('netflix_titles.csv')
df2 = pd.read_csv('Netflix TV Shows and Movies.csv')

# Prepare and merge data
df2_selected = df2[['title', 'release_year', 'age_certification', 'runtime', 'imdb_score', 'imdb_votes']]
merged_df = pd.merge(df1, df2_selected, on=['title', 'release_year'], how='left')
merged_df['date_added'] = pd.to_datetime(merged_df['date_added'], errors='coerce')
clean_df = merged_df.dropna(subset=['type', 'title', 'release_year', 'listed_in'])

# Set theme
sns.set(style='whitegrid')

# Top 10 Genres
genre_series = clean_df['listed_in'].str.split(', ').explode()
top_genres = genre_series.value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_genres.values, y=top_genres.index, palette='plasma')
plt.title('Top 10 Genres on Netflix')
plt.xlabel('Number of Titles')
plt.ylabel('Genre')
plt.tight_layout()
plt.show()

# Release Year Trend
yearly_counts = clean_df['release_year'].value_counts().sort_index()

plt.figure(figsize=(12, 6))
sns.lineplot(x=yearly_counts.index, y=yearly_counts.values, marker='o', linewidth=2.5)
plt.title('Number of Netflix Titles Released Per Year')
plt.xlabel('Release Year')
plt.ylabel('Number of Titles')
plt.tight_layout()
plt.show()

# IMDb Score Distribution
plt.figure(figsize=(10, 6))
sns.histplot(clean_df['imdb_score'].dropna(), bins=20, kde=True, color='coral')
plt.title('Distribution of IMDb Scores')
plt.xlabel('IMDb Score')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# Runtime Distribution (Movies Only)
movies = clean_df[clean_df['type'] == 'Movie']
plt.figure(figsize=(10, 6))
sns.histplot(movies['runtime'].dropna(), bins=30, kde=True, color='skyblue')
plt.title('Distribution of Movie Runtimes')
plt.xlabel('Runtime (minutes)')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# Content Ratings Breakdown
rating_counts = clean_df['rating'].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=rating_counts.values, y=rating_counts.index, palette='viridis')
plt.title('Top 10 Content Ratings')
plt.xlabel('Number of Titles')
plt.ylabel('Rating')
plt.tight_layout()
plt.show()
