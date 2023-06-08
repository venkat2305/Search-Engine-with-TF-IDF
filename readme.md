# To do
1. explore the problems and create index file, qdata file , and files for data from questions
2. Your code looks good! Here are a few things you might want to consider:

    - You could use a more efficient way to calculate the TF-IDF values. Currently, you are looping over each document in the corpus for each term in the query. A more efficient approach would be to use a hash table to store the term frequencies for each document.
    - You could also use a more efficient way to sort the potential documents. Currently, you are using the sorted() function, which is a O(n log n) operation. A more efficient approach would be to use a heap data structure, which can sort a list of elements in O(n) time.

updated code based on 2
```
import math

def load_vocab():
    vocab = {}
    with open('tf_idf_implementation/tf-idf/vocab.txt', 'r') as f:
        vocab_terms = f.readlines()
    with open('tf_idf_implementation/tf-idf/idf-values.txt', 'r') as f:
        idf_values = f.readlines()
    for (term, idf_value) in zip(vocab_terms, idf_values):
        vocab[term.strip()] = int(idf_value.strip())
    return vocab

def load_documents():
    documents = []
    with open('tf_idf_implementation/tf-idf/documents.txt', 'r') as f:
        documents = f.readlines()
    documents = [document.strip().split() for document in documents]
    return documents

def load_inverted_index():
    inverted_index = {}
    with open('tf_idf_implementation/tf-idf/inverted-index.txt', 'r') as f:
        inverted_index_terms = f.readlines()
        for row_num in range(0, len(inverted_index_terms), 2):
            term = inverted_index_terms[row_num].strip()
            term_in_documents = inverted_index_terms[row_num + 1].strip().split()
            inverted_index[term] = term_in_documents
    return inverted_index

vocab_idf_values = load_vocab()
documents = load_documents()
inverted_index = load_inverted_index()

def get_tf_dictionary(term):
    tf_values = {}
    if term in inverted_index:
        for document in inverted_index[term]:
            tf_values[document] = documents[int(document)].count(term)
    return tf_values

def get_idf_value(term):
    return vocab_idf_values[term]

def calculate_sorted_order_of_documents(query_terms):
    potential_documents = {}
    for term in query_terms:
        if vocab_idf_values[term] == 0:
            continue
        tf_values_by_document = get_tf_dictionary(term)
        idf_value = get_idf_value(term)
        for document in tf_values_by_document:
            potential_documents[document] = tf_values_by_document[document] * idf_value
    # divide the length of the query terms
    for document in potential_documents:
        potential_documents[document] /= len(query_terms)
    potential_documents = dict(sorted(potential_documents.items(), key=lambda item: item[1], reverse=True))
    return potential_documents

query_string = input('Enter your query: ')
query_terms = query_string.lower().strip().split()[1:]

print(query_terms)
print(calculate_sorted_order_of_documents(query_terms))
```