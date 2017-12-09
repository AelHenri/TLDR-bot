from nltk import word_tokenize, pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet

class Sentence:

	def __init__(self, s, language="english", tokenizer=word_tokenize):
		self.words = tokenizer(s)
		self.length = len(self.words)
		self.pos = []
		self.lemmas = []
		self.main_words = []
		self.language = language

	def getWord(self, index):
		return self.words[index]

	def posTag(self):
		pos_tags = pos_tag(self.words)
		for i in range(self.length):
			self.pos.append(pos_tags[i][1])

	def lemmatize(self):

		lemm = WordNetLemmatizer()
		def getWordnetPos(tag):
			if tag.startswith('J'):
				return wordnet.ADJ
			elif tag.startswith('V'):
				return wordnet.VERB
			elif tag.startswith('N'):
				return wordnet.NOUN
			elif tag.startswith('R'):
				return wordnet.ADV
			else:
				return ''

		if not self.pos:
			self.posTag()

		for i in range(self.length):
			currentTag = getWordnetPos(self.pos[i])
			if currentTag:
				self.lemmas.append(lemm.lemmatize(self.words[i], currentTag))
			else:
				self.lemmas.append(lemm.lemmatize(self.words[i]))

	def filter(self):

		def checkInPos(pos):
			allowed = ["F", "J", "NN", "RB", "UH", "V"]
			for a in allowed:
				if a in pos:
					return True
			return False

		for i in range(self.length):
			if checkInPos(self.pos[i]):
				self.main_words.append(self.lemmas[i])
