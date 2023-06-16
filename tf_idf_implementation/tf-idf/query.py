import math

def load_vocab():
    vocab = {}
    with open('./vocab.txt', 'r') as f:
        vocab_terms = f.readlines()
    with open('./idf-values.txt', 'r') as f:
        idf_values = f.readlines()
    for (term,idf_value) in zip(vocab_terms, idf_values):
        vocab[term.strip()] = int(idf_value.strip())
    # print('size of vocab: ' ,len(vocab))
    # print(vocab)
    return vocab

def question_links():
    with open('../Qdata/Qindex.txt', 'r') as f:
        question_links = f.readlines()
        question_links = [link.strip() for link in question_links]  # Use 'link.strip()' instead of 'question_links.strip'
    return question_links


# zip function : The zip() function is a built-in Python function that takes multiple iterables as input and returns an iterator that generates tuples containing elements from each of the input iterables. It aggregates the elements based on their positions, pairing the first elements together, the second elements together, and so on.

# list comprehension : List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list
# newlist = [expression for item in iterable if condition == True]
# the term "expression" refers to the operation or transformation that is applied to each element of the iterable.

def load_documents():
    documents = []
    with open('./documents.txt', 'r') as f:
        documents = f.readlines()
    documents = [document.strip().split() for document in documents]
    # print('number of documents: ', len(documents))
    return documents

def load_inverted_index():
    inverted_index = {}
    with open('./inverted-index.txt', 'r') as f:
        inverted_index_terms = f.readlines() # readlines() : returns a list containing each line in the file as a list item
        # print(inverted_index_terms)
        for row_num in range(0,len(inverted_index_terms),2):
            term = inverted_index_terms[row_num].strip()
            term_in_documents = inverted_index_terms[row_num+1].strip().split()
            inverted_index[term] = term_in_documents
        # print(inverted_index)
    return inverted_index

vocab_idf_values = load_vocab()
documents = load_documents()
inverted_index = load_inverted_index()
question_links = question_links()

# print(inverted_index['the'])
# ?
def get_tf_dictionary(term): # The get_tf_dictionary(term) function returns a dictionary containing the term frequency (TF) values for a given term across the documents
    tf_values = {} # term frequency values of the term acroos each document
    if term in inverted_index:
        for doc_id in inverted_index[term]: # term is present in the document, so it is present in the inverted index
            if doc_id not in tf_values:   # The tf_values variable represents a dictionary that stores the term frequency (TF) values for a given term in the documents.
                tf_values[doc_id] = 1
            else:
                tf_values[doc_id] += 1
            # we are looping through all the documents in which term is present using inverted_index, so doucument 
    # print(tf_values)
    for doc_id in tf_values:
        tf_values[doc_id] /= len(documents[int(doc_id)])
    
    return tf_values

def get_idf_value(term):
    return math.log(len(documents)/vocab_idf_values[term])

def calculate_sorted_order_of_documents(query_terms):
    potential_documents = {} # The potential_documents dictionary aims to collect the potential documents that are relevant to the given query terms and assign a score to each document based on their TF-IDF values.
    
    for term in query_terms:
        if vocab_idf_values[term] == 0:
            continue
        tf_values_by_document = get_tf_dictionary(term)
        idf_value = get_idf_value(term)
        # print(term,tf_values_by_document,idf_value)

        # calculation of tf-idf scores and storing the {document + score(avg of tf-idf)} in potential_documents
        for doc_id in tf_values_by_document:
            if doc_id not in potential_documents:
                potential_documents[doc_id] = tf_values_by_document[doc_id] * idf_value
            potential_documents[doc_id] += tf_values_by_document[doc_id] * idf_value

    # divide the length of the query terms
    # print(potential_documents)

    #calculating the avg score of document for query terms
    for document in potential_documents:
        potential_documents[document] /= len(query_terms)

    #sorting the potential_documents by the score of the documents
    potential_documents = dict(sorted(potential_documents.items(), key=lambda item: item[1], reverse=True))
    
    # for document_index in potential_documents:
    #     print('Document: ', documents[int(document_index)], ' Score: ', potential_documents[document_index])

    return potential_documents  

# print("Numbet of documents: ", len(documents))

query_string = input('Enter your query: ')
query_terms = query_string.lower().strip().split()[1:]

# print(query_terms)
potential_documents = calculate_sorted_order_of_documents(query_terms)

# print(question_links)

# print the top 15 documents related to query terms along with their scores and question link
for document_index in list(potential_documents.keys())[:15]:  # Iterate over the top 15 documents
    print('Question:', question_links[int(document_index)] , 'Score:', potential_documents[document_index] )


























# The vocab_idf_values is a dictionary where the terms are used as keys, and the corresponding values represent the total number of times each term occurs across all the documents.

# The documents list consists of sublists, where each sublist contains the individual words of a document.

# The inverted_index is a dictionary where the terms are used as keys, and the corresponding values are lists of document ids in which the term is present.

# The tf_values is a dictionary where the document IDs are used as keys, and the values represent the number of times a term is present in each document.

# To achieve this, we iterate through the list of inverted_index[term], which contains all the document IDs in which the term is present. We then map the tf_value[doc_#] for each term.

# For each term, we increment the key value by 1 when the document is present, so that tf[doc1] increases by 1.