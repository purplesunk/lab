def new_collection(initial_docs):
    docs = initial_docs.copy()
    def add_doc(doc):
        nonlocal docs
        docs.append(doc)
        return docs
    return add_doc
