from nltk import word_tokenize

class SplitText:

    def __init__(self, text):
        self.rawText = text
        self.table = []
        self.words = word_tokenize(self.rawText)
        self.size = len(self.words)
        self.columns = ["index", "word"]
        self.paraTable = []
        paragraphs = 0
        sentences = 0
        currentSentence = []
        currentParagraph = []
        for i in range(self.size):
            if self.words[i] == ".":
                sentences += 1
                currentParagraph.append(currentSentence)
                currentSentence = []
            if i<self.size-2 and self.words[i] == "\n" and self.words[i+1] == "\n":
                paragraphs += 1
                self.paraTable.append(currentParagraph)
                currentParagraph = []
            currentWord = {}
            currentWord["index"] = i
            currentWord["word"] = self.words[i]
            currentSentence.append(self.words[i])
            currentWord["sentence"] = sentences
            currentWord["pararaph"] = paragraphs
            self.table.append(currentWord)