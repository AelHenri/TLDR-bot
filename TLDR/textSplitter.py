import nltk.data
from nltk import word_tokenize
from sentences import Sentence
from sentenceProcessor import WordNetProcessor

class Splitter:

	def __init__(self, raw, language="english", wordTokenizer=word_tokenize, sentenceProcessor=WordNetProcessor):
		self.raw = raw
		self.sentences = []
		self.language = language
		self.wordTokenizer = word_tokenize
		self.sentenceProcessor = sentenceProcessor

	def split(self):
		tokenizer = nltk.data.load("tokenizers/punkt/"+self.language+".pickle")
		rawSentences = tokenizer.tokenize(self.raw)
		for s in rawSentences:
			self.sentences.append(Sentence(s, self.wordTokenizer, self.sentenceProcessor))

	def getSentences(self):
		return self.sentences
