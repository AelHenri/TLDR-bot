from nltk import word_tokenize
from sentences import Sentence
from sentenceProcessor import WordNetProcessor
from textSplitter import Splitter

class Text:
	def __init__(self, raw, language="english", wordTokenizer=word_tokenize, sentenceProcessor=WordNetProcessor):
		self.raw = raw
		splitter = Splitter(raw, language, wordTokenizer, sentenceProcessor)
		splitter.split()
		self.sentences = splitter.getSentences()
		self.length = len(self.sentences)

	def getSentences(self):
		return self.sentences

	def getLength(self):
		return self.length