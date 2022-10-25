import streamlit as st
import json
from Classifier import KNearestNeighbours
from operator import itemgetter

# Load data and movies list from corresponding JSON files
with open(r'data2.json', 'r+', encoding='utf-8') as f:
    data = json.load(f)
with open(r'titles2.json', 'r+', encoding='utf-8') as f:
    product_titles = json.load(f)


def knn(test_point, k):
    # Create dummy target variable for the KNN Classifier
    target = [0 for item in product_titles]
    # Instantiate object for the Classifier
    model = KNearestNeighbours(data, target, test_point, k=k)
    # Run the algorithm
    model.fit()
    # Distances to most distant movie
    max_dist = sorted(model.distances, key=itemgetter(0))[-1]
    # Print list of 10 recommendations < Change value of k for a different number >
    table = list()
    for i in model.indices:
        # Returns back movie title and imdb link
        table.append([product_titles[i][0], product_titles[i][2]])
    return table


if __name__ == '__main__':
    genres = ['Blouses',
              'Casual bottoms',
              'Chemises',
              'Dresses',
              'Fine gauge',
              'Intimates',
              'Jackets',
              'Jeans',
              'Knits',
              'Layering',
              'Legwear',
              'Lounge',
              'Outerwear',
              'Pants',
              'Shorts',
              'Skirts',
              'Sleep',
              'Sweaters',
              'Swim',
              'Trend']

    products = [title[0] for title in product_titles]
    st.header('Product Recommendation System')
    apps = ['--Select--', 'Product based', 'Category based']
    app_options = st.selectbox('Select application:', apps)

    if app_options == 'Movie based':
        product_select = st.selectbox(
            'Select product:', ['--Select--'] + products)
        if product_select == '--Select--':
            st.write('Select a item')
        else:
            n = st.number_input('Number of items:',
                                min_value=5, max_value=20, step=1)
            genres = data[products.index(product_select)]
            test_point = genres
            table = knn(test_point, n)
            for movie, link in table:
                # Displays movie title with link to imdb
                st.markdown(f"[{movie}]({link})")
    elif app_options == apps[2]:
        options = st.multiselect('Select category:', genres)
        if options:
            imdb_score = st.slider('IMDb score:', 1, 10, 8)
            n = st.number_input('Number of products:',
                                min_value=5, max_value=20, step=1)
            test_point = [1 if genre in options else 0 for genre in genres]
            test_point.append(imdb_score)
            table = knn(test_point, n)
            for movie, link in table:
                # Displays movie title with link to imdb
                st.markdown(f"[{movie}]({link})")

        else:
            st.write("This is a simple Movie Recommender application. "
                     "You can select the genres and change the IMDb score.")

    else:
        st.write('Select option')
