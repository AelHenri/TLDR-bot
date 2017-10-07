import numpy as np

# naive intersection scoring function: length of the intersection between 2 sentences
def naiveTR_intersection(s1, s2):
	inter_len = len(set(s1).intersection(s2))
	return inter_len/((len(s1)+len(s2))/2)

# returns the best sentence of a paragraph, based on an intersection scoring function
def naiveTR_best(paragraph, scoring=naiveTR_intersection):
	# build a weighted graph
	graph = np.zeros((len(paragraph), len(paragraph)))
	for i, s1 in enumerate(paragraph):
		for j, s2 in enumerate(paragraph):
			if i == j:
				continue
			graph[i][j] = scoring(s1, s2) #graph[i][j] contains the length of the intersection between s1 and s2 (by default)
	scores = []

	# compute the final score of each sentence
	for i in range(len(paragraph)):
		currentScore = sum(graph[i])
		score.append(currentScore)

	# find the sentence with the max score
	return paragraph[scores.index(max(scores))]

def naiveTextRank(splitText):
	bestSentences = []
	for paragraph in splitText:
		currentBest = naiveTR_best(paragraph)
		bestSentences.append(currentBest)
	return "".join(bestSentences)
	

