import numpy as np

from python.utils.reader import read_file
from python.utils.data_clean import data_clean
from python.metadata.path import Path
from sentence_transformers import SentenceTransformer
from python.utils.distance_calculate import find_closest_sentences


def executor():
    text = read_file(Path.text)
    table_sentences = data_clean(text)

    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    embedding = model.encode(table_sentences['sentences'], 
                             batch_size=10, 
                             show_progress_bar=True)
    
    table_sentences['embedding'] = embedding.tolist()

    question = input('Into the question in spanish: ')

    question = np.array([question])

    question_embedding = model.encode(question)

    answers = find_closest_sentences(question_embedding, 
                                     table_sentences, 
                                    'embedding', 5)
    
    for i,j in enumerate(answers):
        print(f'Answer {i+1}: {j}')
        print('')
