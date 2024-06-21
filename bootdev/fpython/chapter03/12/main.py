def word_count_memo(document, memos):
    new_memos = memos.copy()
    if document not in new_memos:
        new_memos[document] = word_count(document)
    return new_memos[document], new_memos


# Don't edit below this line


def word_count(document):
    count = len(document.split())
    return count
