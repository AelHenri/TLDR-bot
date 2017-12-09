from nltk import word_tokenize
from sentenceProcessor import WordNetProcessor

class Sentence:

	def __init__(self, s, tokenizer=word_tokenize, processor=WordNetProcessor):
		self.words = tokenizer(s)
		self.processor = processor(self.words)
		self.length = len(self.words)

		self.processor.tag()
		self.processor.lemmatize()
		self.processor.filter()

		self.pos = self.processor.getPos()
		self.lemmas = self.processor.getLemmas()
		self.main_words = self.processor.getMains()

	def getWord(self, index):
		return self.words[index]
