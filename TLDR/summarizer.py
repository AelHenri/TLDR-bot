class Summarizer:
	def __init__(self, text):
		self.text = text
		self.summary = ""

	def summarize(self, function):
		self.summary = function(self.text)