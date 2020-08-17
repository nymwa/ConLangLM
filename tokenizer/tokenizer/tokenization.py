class BasicTokenizer:
	def detokenize(self, token_list):
		return ' '.join([str(token) for token in token_list])

