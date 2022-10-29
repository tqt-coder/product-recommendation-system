import time
import text_base_lib as lib
import sys
sys.path.insert(
    1, 'C:/Users/tranq/Documents/Semeter1_2022_2023/Semeter1_2022_2023/TLCN/product-recommend-system')

start_time = time.time()


def recommandation(title, len):
    # title = 'Rosa Nobile'

    # Get the index corresponding to movie title
    index = lib.indices[title]

    # Get the cosine similarity scores
    similarity_scores = list(enumerate(lib.similarity_matrix[index]))

    # Sort the similarity scores in descending order
    sorted_similarity_scores = sorted(
        similarity_scores, key=lambda x: x[1], reverse=True)

    # Top-10 most similar movie scores
    top_items_scores = sorted_similarity_scores[1:len]

    # Get movie indices
    top_items_indices = []
    for i in top_items_scores:
        top_items_indices.append(str(i[0]))
    print(print(lib.data['name'].iloc[top_items_indices] +
                " ----0000--- " + lib.data['URL'].iloc[top_items_indices]))


print(recommandation('Rosa Nobile', 11))
print("--- %s seconds ---" % (time.time() - start_time))
