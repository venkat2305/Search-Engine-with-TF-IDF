# read index.txt and and prepare documents , vocab , idf 

with open('tf_idf_implementation/Qdata/index.txt','r') as f:
    lines = f.readlines()
    # print(lines[1])

# preprocess
# 1. remove stop words , punctuations , special characters
# 2. convert text to lower case
# 3. tokenization
# 4. stemming

# lower(),strip() methods can be used only on strings, we cannot use them on lists
# but slice can be used on string , lists and tuple
# [1:] its a slice notation, prints everything except the first element
# [1:3] prints elements from index 1 to index 2
# [:3] prints elements from index 0 to index 2

# string.split(separator, maxsplit) : separator is the delimiter by which the string is split into parts. If the separator is not specified then any white space is a separator. Maxsplit is the number of splits to be made. Default value is -1 which means all occurrences. 
# string.strip(characters) : characters is the set of characters to be removed from the string. If the characters are not specified then all the leading and trailing whitespaces are removed from the string.

# + method is used to concatenate two lists , but append method is used to add a list to another list as a single element

def preprocess(doc_text): # doc_text is a string
    return doc_text.lower().strip().split()[1:]
    # or terms = [term.lower() for term in document_text.strip().split()[1:]] return terms

# enumerate : returns a tuple containing a count for every iteration (from start which defaults to 0) and the values obtained from iterating over sequence 

vocab = {} # dictionary , similar to map in c++ , keeps track of each term and its frequency accross all documents
documents = []
for index, line in enumerate(lines):
    # preprocess line in lines and add them to documents
    tokens = preprocess(line)
    documents.append(tokens)
    tokens = set(tokens) # while calculating idf , we need to know the number of documents in which a term is present , so we use set to remove duplicates
    for token in tokens: # tokens is a document and token is a term in the doucment
        if token not in vocab:
            vocab[token] = 1
        else:
            vocab[token] += 1
        

# print("number of documents:",len(documents))
# print("size of vocab:",len(vocab))
# print("sample document:",documents[0])
# print(vocab)

# print(documents)

# reverse sort the vocab by values

vocab = dict(sorted(vocab.items(), key=lambda item: item[1], reverse=True)) #?

# save the vocab in a text file
with open('tf_idf_implementation/tf-idf/vocab.txt', 'w') as f:
    for token in vocab:
        f.write(token+'\n')

#save the idf-values in a text file
with open('tf_idf_implementation/tf-idf/idf-values.txt','w' ) as f:
    for token in vocab:
        f.write(str(vocab[token])+'\n')

# The join() method takes all items in an iterable(list,tuple,etc) and joins them into one string
# result_string = delimiter.join(iterable) : 
# delimiter: The string that will be used as the separator to join the elements.
# iterable: The iterable (e.g., list, tuple, set) containing the elements to be joined.
# The join() method is called on the delimiter string and takes the iterable as an argument. 
# It returns a new string where the elements of the iterable are concatenated together, 
# separated by the delimiter string.

# save the documents in a text file
with open('tf_idf_implementation/tf-idf/documents.txt','w') as f:
    for doc in documents:
        f.write(' '.join(doc)+'\n')

inverted_index = {}
for index, document in enumerate(documents):
    for token in document:
        if token not in inverted_index:
            inverted_index[token] = [index] # index is document id
        else:
            inverted_index[token].append(index)

# save the inverted index in a text file
with open('tf_idf_implementation/tf-idf/inverted-index.txt', 'w') as f:
    for key in inverted_index.keys():
        f.write("%s\n" % key)
        f.write("%s\n" % ' '.join([str(doc_id) for doc_id in inverted_index[key]]))