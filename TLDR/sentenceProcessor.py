from nltk import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet

class SentenceProcessor:

	def __init__(self, words):
		self.words = words
		self.pos = []
		self.lemmas = []
		self.mains = []
		self.tagger = None
		self.lemmatizer = None

	def tag(self):
		self.pos = self.tagger(self.words)

	def lemmatize(self):
		return

	def filter(self):
		return

	def getPos(self):
		return self.pos

	def getLemmas(self):
		return self.lemmas

	def getMains(self):
		return self.mains

class WordNetProcessor(SentenceProcessor):

	def __init__(self, words):
		super().__init__(words)
		self.tagger = pos_tag
		self.lemmatizer = WordNetLemmatizer()

	def __getWordnetPos(self, tag):
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

	def lemmatize(self):
		if not self.pos:
			self.tag()

		for i in range(len(self.words)):
			currentTag = self.__getWordnetPos(self.pos[i][1])
			if currentTag:
				self.lemmas.append(self.lemmatizer.lemmatize(self.words[i], currentTag))
			else:
				self.lemmas.append(self.lemmatizer.lemmatize(self.words[i]))

	def filter(self):
		def checkInPos(pos):
			allowed = ["F", "J", "NN", "RB", "UH", "V"]
			for a in allowed:
				if a in pos:
					return True
			return False

		for i in range(len(self.words)):
			if checkInPos(self.pos[i][1]):
				self.mains.append(self.lemmas[i])



