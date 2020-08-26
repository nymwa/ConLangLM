class Sentence(list):
	def __str__(self):
		return ' '.join([str(token) for token in self])

