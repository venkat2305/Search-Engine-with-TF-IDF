
def load_vocab():
    vocab = {}
    with open('tf_idf_implementation/tf-idf/vocab.txt', 'r') as f:
        vocab_terms = f.readlines()
    with open('tf_idf_implementation/tf-idf/idf-values.txt', 'r') as f:
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
    with open('tf_idf_implementation/tf-idf/documents.txt', 'r') as f:
        documents = f.readlines()
    documents = [document.strip().split() for document in documents]
    # print('number of documents: ', len(documents))
    return documents

def load_inverted_index():
    inverted_index = {}
    with open('tf_idf_implementation/tf-idf/inverted-index.txt', 'r') as f:
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
# ?
def get_tf_dictionary(term): # The get_tf_dictionary(term) function returns a dictionary containing the term frequency (TF) values for a given term across the documents
    tf_values = {} 
    if term in inverted_index:
        for document in inverted_index[term]: # term is present in the document, so it is present in the inverted index
            if document not in tf_values:   # The tf_values variable represents a dictionary that stores the term frequency (TF) values for a given term in the documents.
                tf_values[document] = 1
            else:
                tf_values[document] += 1
                
    for document in tf_values:
        tf_values[document] /= len(documents[int(document)])
    
    return tf_values

def get_idf_value(term):
    return vocab_idf_values[term]

def calculate_sorted_order_of_documents(query_terms):
    potential_documents = {} # The potential_documents dictionary aims to collect the potential documents that are relevant to the given query terms and assign a score to each document based on their TF-IDF values.
    for term in query_terms:
        if vocab_idf_values[term] == 0:
            continue
        tf_values_by_document = get_tf_dictionary(term)
        idf_value = get_idf_value(term)
        for document in tf_values_by_document:
            if document not in potential_documents:
                potential_documents[document] = tf_values_by_document[document] * idf_value
            potential_documents[document] += tf_values_by_document[document] * idf_value
    # divide the length of the query terms
    for document in potential_documents:
        potential_documents[document] /= len(query_terms)
    potential_documents = dict(sorted(potential_documents.items(), key=lambda item: item[1], reverse=True))
    print(potential_documents)



query_string = input('Enter your query: ')
query_terms = query_string.lower().strip().split()[1:]

print(query_terms)
print(calculate_sorted_order_of_documents(query_terms))