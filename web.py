from turtle import title
from flask import Flask, render_template, request
from msilib.schema import tables
import streamlit as st
import json
import time
import text_base_lib as lib

with open(r'titles2.json', 'r+', encoding='utf-8') as f:
    product_titles = json.load(f)
app = Flask(__name__)
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


def recommandation(title, len):
    index = lib.indices[title]
    similarity_scores = list(enumerate(lib.similarity_matrix[index]))
    sorted_similarity_scores = sorted(
        similarity_scores, key=lambda x: x[1], reverse=True)
    top_items_scores = sorted_similarity_scores[1:len]

    top_items_indices = []
    for i in top_items_scores:
        top_items_indices.append(str(i[0]))

    table = list()
    for j in top_items_indices:
        table.append([lib.data['name'][int(j)], lib.data['URL'][int(j)]])
    return table


@app.route('/')
def homePage():
    return render_template("./index.html", listProducts=products, category=genres)


@app.route('/recommendation', methods=['POST'])
def resutl():
    title = request.form['title']
    quantity = request.form['quantity']
    if title != None and quantity != None:
        table = recommandation(title, int(quantity) + 1)
        str = ""
        for item, link in table:
            str = str + f"[{item}]({link})"
        return str
    else:
        return render_template("./index.html", listProducts=products, category=genres)


if __name__ == '__main__':
    app.run(debug=True)
