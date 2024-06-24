def word_count_aggregator():
    count = 0
    def word_count(doc):
        nonlocal count
        count = count + len(doc.split())
        return count
    return word_count
