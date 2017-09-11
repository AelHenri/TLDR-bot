from nltk.tokenize import sent_tokenize, word_tokenize
import csv

def getText(path):
    text = ""
    with open(path) as file:
        text = file.read()
    return text

def splitText(text):
    split_text = []
    sentences = sent_tokenize(text)
    i = 0
    for s in sentences:
        split_text.append(word_tokenize(sentences[i]))
        i += 1
    return split_text

def intersectionScore(s1, s2):
    inter_len = len(set(s1).intersection(s2))
    return inter_len/((len(s1)+len(s2))/2)

