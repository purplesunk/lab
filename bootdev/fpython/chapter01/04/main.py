def add_prefix(document, documents):
    prefix = f"{len(documents)}. "
    new_doc = (prefix + document,)
    new_docs = documents + new_doc
    return new_docs
