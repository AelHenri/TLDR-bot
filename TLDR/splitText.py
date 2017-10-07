from nltk import word_tokenize, sent_tokenize

class SplitText:

    def __init__(self, text):
        self.rawText = text
        self.paragraphs = []

    def splitIntoParts(self, lang=None):
        # Naive way to split the text into paragraphs
        basicParagraphs = self.rawText.split("\n\n")

        # Build the array of paragraph: a paragraph is an array of sentences, which are arrays of words
        for p in basicParagraphs:
            currentParagraph = []
            basicSentences = sent_tokenize(p, language=lang)

            # Discard "paragraphs" with one sentence (subtitles, links, etc...)
            if len(basicSentences) == 1:
                continue

            for s in basicSentences:
                words = word_tokenize(s)
                currentParagraph.append(words)
            self.paragraphs.append(currentParagraph)

    def getParagraph(self, index):
        return self.paragraphs[index]

    def getSentence(self, paragraph, index):
        return self.paragraphs[paragraph][index]

    def getWord(self, paragraph, sentence, index):
        return self.paragraphs[paragraph][sentence][index]

    def __iter__(self):
        return iter(self.paragraphs)

            

