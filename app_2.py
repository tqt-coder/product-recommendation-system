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
    genres = ['Accessories',
              'After Sun Care',
              'Aftershave',
              'Anti-Aging',
              'BB & CC Cream',
              'BB & CC Creams',
              'Bath & Body',
              'Bath & Shower',
              'Bath Soaks & Bubble Bath',
              'Beauty Supplements',
              'Blemish & Acne Treatments',
              'Blotting Papers',
              'Blush',
              'Body Lotions & Body Oils',
              'Body Mist & Hair Mist',
              'Body Moisturizers',
              'Body Products',
              'Body Sprays & Deodorant',
              'Body Sunscreen',
              'Body Wash & Shower Gel',
              'Bronzer',
              'Brush Cleaners',
              'Brush Sets',
              'Candles',
              'Candles & Home Scents',
              'Cellulite & Stretch Marks',
              'Cheek Palettes',
              'Cleansing Brushes',
              'Cologne',
              'Cologne Gift Sets',
              'Color Care',
              'Color Correct',
              'Concealer',
              'Conditioner',
              'Contour',
              'Curling Irons',
              'Curls & Coils',
              'Decollete & Neck Creams',
              'Deodorant & Antiperspirant',
              'Deodorant for Men',
              'Diffusers',
              'Dry Shampoo',
              'Exfoliators',
              'Eye Brushes',
              'Eye Cream',
              'Eye Creams & Treatments',
              'Eye Masks',
              'Eye Palettes',
              'Eye Primer',
              'Eye Sets',
              'Eyebrow',
              'Eyelash Curlers',
              'Eyeliner',
              'Eyeshadow',
              'Face Brushes',
              'Face Masks',
              'Face Oils',
              'Face Primer',
              'Face Serums',
              'Face Sets',
              'Face Sunscreen',
              'Face Wash',
              'Face Wash & Cleansers',
              'Face Wipes',
              'Facial Cleansing Brushes',
              'Facial Peels',
              'Facial Rollers',
              'False Eyelashes',
              'For Body',
              'For Face',
              'Foundation',
              'Fragrance',
              'Hair',
              'Hair Accessories',
              'Hair Brushes & Combs',
              'Hair Dryers',
              'Hair Masks',
              'Hair Oil',
              'Hair Primers',
              'Hair Products',
              'Hair Removal',
              'Hair Removal & Shaving',
              'Hair Spray',
              'Hair Straighteners & Flat Irons',
              'Hair Styling & Treatments',
              'Hair Styling Products',
              'Hair Thinning & Hair Loss',
              'Hand Cream & Foot Cream',
              'High Tech Tools',
              'Highlighter',
              'Holistic Wellness',
              'Leave-In Conditioner',
              'Lid Shadow Brush',
              'Lip Balm & Treatment',
              'Lip Balms & Treatments',
              'Lip Brushes',
              'Lip Gloss',
              'Lip Liner',
              'Lip Plumper',
              'Lip Sets',
              'Lip Stain',
              'Lip Sunscreen',
              'Lip Treatments',
              'Lipstick',
              'Liquid Lipstick',
              'Lotions & Oils',
              'Makeup',
              'Makeup & Travel Cases',
              'Makeup Bags & Travel Cases',
              'Makeup Palettes',
              'Makeup Removers',
              'Mascara',
              'Mini Size',
              'Mirrors & Sharpeners',
              'Mists & Essences',
              'Moisturizer & Treatments',
              'Moisturizers',
              'Nail',
              'Night Creams',
              'Perfume',
              'Perfume Gift Sets',
              'Powder Brush',
              'Rollerballs & Travel Size',
              'Scalp & Hair Treatments',
              'Scrub & Exfoliants',
              'Self Tanners',
              'Setting Spray & Powder',
              'Shampoo',
              'Shampoo & Conditioner',
              'Shaving',
              'Sheet Masks',
              'Skincare',
              'Skincare Sets',
              'Spa Tools',
              'Sponges & Applicators',
              'Sunscreen',
              'Teeth Whitening',
              'Tinted Moisturizer',
              'Toners',
              'Tweezers & Eyebrow Tools',
              'Value & Gift Sets',
              'Wellness',
              'no category']

    products = [title[0] for title in product_titles]
    st.header('Product Recommendation System')
    apps = ['--Select--', 'Product based', 'Category based']
    app_options = st.selectbox('Select application:', apps)

    if app_options == 'Product based':
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
            for item, link in table:
                # Displays item title with link to imdb
                st.markdown(f"[{item}]({link})")
    elif app_options == apps[2]:
        options = st.multiselect('Select category:', genres)
        if options:
            imdb_score = st.slider('IMDb score:', 1, 10, 8)
            n = st.number_input('Number of products:',
                                min_value=5, max_value=20, step=1)
            test_point = [1 if genre in options else 0 for genre in genres]
            test_point.append(imdb_score)
            table = knn(test_point, n)
            for item, link in table:
                # Displays item title with link to imdb
                st.markdown(f"[{item}]({link})")

        else:
            st.write("This is a simple Movie Recommender application. "
                     "You can select the genres and change the IMDb score.")

    else:
        st.write('Select option')
