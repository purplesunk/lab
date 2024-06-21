import functools


def join(doc_so_far, sentence):
    if doc_so_far:
        return f"{doc_so_far}. {sentence}"
    return sentence


def join_first_sentences(sentences, n):
    if n == 0:
        return ""
    return f"{functools.reduce(join, sentences[:n])}."
