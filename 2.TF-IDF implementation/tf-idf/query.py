
def load_vocab():
    vocab = {}
    with open('tf-idf/vocab.txt', 'r') as f:
        vocab_terms = f.readlines()
    with open('tf-idf/idf-values.txt', 'r') as f:
        idf_values = f.readlines()
    for (term,idf_value) in zip(vocab_terms, idf_values):
        vocab[term.strip()] = int(idf_value.strip())
    # print('size of vocab: ' ,len(vocab))
    return vocab

# zip function : The zip() function is a built-in Python function that takes multiple iterables as input and returns an iterator that generates tuples containing elements from each of the input iterables. It aggregates the elements based on their positions, pairing the first elements together, the second elements together, and so on.

# list comprehension : List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list
# newlist = [expression for item in iterable if condition == True]
# the term "expression" refers to the operation or transformation that is applied to each element of the iterable.

def load_documents():
    documents = []
    with open('tf-idf/documents.txt', 'r') as f:
        documents = f.readlines()
    documents = [document.strip().split() for document in documents]
    # print('number of documents: ', len(documents))
    return documents

def load_inverted_index():
    inverted_index = {}
    with open('tf-idf/inverted-index.txt', 'r') as f:
        inverted_index_terms = f.readlines() # readlines() : returns a list containing each line in the file as a list item
        # print(inverted_index_terms)
        for row_num in range(0,len(inverted_index_terms),2):
            term = inverted_index_terms[row_num].strip()
            term_in_documents = inverted_index_terms[row_num+1].strip().split()
            inverted_index[term] = term_in_documents
    return inverted_index

vocab_idf_values = load_vocab()
documents = load_documents()
inverted_index = load_inverted_index()

# print(inverted_index['the'])










query_string = input('Enter your query: ')
query_terms = query_string.lower().strip().split()[1:]