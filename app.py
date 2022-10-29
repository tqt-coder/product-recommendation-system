from msilib.schema import tables
import streamlit as st
import json
import time
import text_base_lib as lib
# import sys
# sys.path.insert(
#     1, 'C:/Users/tranq/Documents/Semeter1_2022_2023/Semeter1_2022_2023/TLCN/product-recommend-system')


with open(r'titles2.json', 'r+', encoding='utf-8') as f:
    product_titles = json.load(f)


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


if __name__ == '__main__':

    products = [title[0] for title in product_titles]
    st.header('Product Recommendation System By Text Similarity')
    product_select = st.selectbox(
        'Select product:', ['--Select--'] + products)
    if product_select == '--Select--':
        st.write('Select a item')
    else:
        n = st.number_input('Number of items:',
                            min_value=5, max_value=20, step=1)
        table = recommandation(product_select, n+1)
        for item, link in table:
            st.markdown(f"[{item}]({link})")
