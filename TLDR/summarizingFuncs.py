# naive intersection scoring function: length of the intersection between 2 sentences
def naiveTR_intersection(s1, s2):
	inter_len = len(set(s1).intersection(s2))
    return inter_len/((len(s1)+len(s2))/2)

# returns the best sentence of a paragraph, based on an intersection scoring function
def naiveTR_best(paragraph, scoring=naiveTR_intersection):
	graph = {}
	for i, s1 in enumerate(paragraph):
		for j, s2 in enumerate(paragraph):
			if i == j:
				continue
			graph[(i,j)] = scoring(s1, s2)
			
		

def naiveTextRank(splitText):
	

