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
    return render_template("./login.html")


@app.route('/recommendation', methods=['POST'])
def resutl():
    title = request.form['title']
    quantity = request.form['quantity']

    table = recommandation(title, int(quantity) + 1)
    a = ""
    for item, link in table:
        a = a + f"[{item}]({link})"
    return a


if __name__ == '__main__':
    app.run(debug=True)
