from utils import *
import pandas as pd
import numpy as np
import os
import pickle

os.makedirs(RESOURCE_PATH['THREAD_EMBEDDINGS_FOLDER'], exist_ok=True)

emb, dim = load_embeddings("./mdl.tsv")

posts_df = pd.read_csv('tagged_posts.tsv', sep='\t')
counts_by_tag = posts_df.groupby('tag').size()

for tag, count in counts_by_tag.items():
    tag_posts = posts_df[posts_df['tag'] == tag]

    # YOUR CODE HERE #############
    tag_post_ids = [post_id for post_id in tag_posts['post_id']]

    tag_vectors = np.zeros((count, dim), dtype=np.float32)
    for i, title in enumerate(tag_posts['title']):
        tag_vectors[i, :] = question_to_vec(
            title, emb, dim)  # YOUR CODE HERE #############

    # Dump post ids and vectors to a file.
    filename = os.path.join(
        RESOURCE_PATH['THREAD_EMBEDDINGS_FOLDER'], os.path.normpath('%s.pkl' % tag))
    pickle.dump((tag_post_ids, tag_vectors), open(filename, 'wb'))
