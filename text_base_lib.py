import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from wordcloud import WordCloud
from wordcloud import STOPWORDS
import matplotlib.pyplot as plt

data = pd.read_csv(r'website_dataset.csv')

tfidf = TfidfVectorizer(analyzer='word',
                        token_pattern=r'\w{1,}',
                        ngram_range=(1, 3),
                        stop_words='english')

data['details'] = data['details'].fillna('')

tfidf_matrix = tfidf.fit_transform(data['details'])

tfidf_matrix.shape

similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

indices = pd.Series(data.index, index=data['name']).drop_duplicates()
