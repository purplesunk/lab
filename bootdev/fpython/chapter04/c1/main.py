def count_nested_levels(nested_documents, target_document_id, level=1):
    for doc in nested_documents:
        if doc == target_document_id:
            return level
        elif nested_documents[doc]:
            found = count_nested_levels(nested_documents[doc], target_document_id, level + 1)
            if found != -1:
                return found
    return -1
