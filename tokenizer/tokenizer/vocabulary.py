from collections import Counter

class Vocabulary(list):
	def __init__(self, tokenizer, sents):
		token_counter = Counter()
		for sent in sents:
			for token in sent:
				token_counter.update([str(token)])

		token_freqs = token_counter.most_common()
		token_freqs = [(symbol, freq)
				for symbol, freq
				in token_freqs
				if not (symbol.startswith('<') and symbol.endswith('>'))]
		self.special_token_list = tokenizer.special_token_list
		self.word_token_list = [tokenizer.symbol_tokenize(symbol) for symbol, freq in token_freqs]
		self.word_freq_list = [freq for symbol, freq in token_freqs]
		self.token = tokenizer.special_token_list + self.word_token_list

		super().__init__(self.token)
		self.index_dict = {str(token) : n for n, token in enumerate(self)}

		for special_token in self.special_token_list:
			setattr(self, special_token.tag, self.index_dict[str(special_token)])

	def __contains__(self, x):
		return x in self.index_dict

	def word_to_index(self, x):
		return self.index_dict[x] if x in self.index_dict else self.unk

	def show(self):
		for token in self.special_token_list:
			print(str(token))
		for token, freq in zip(self.word_token_list, self.word_freq_list):
			print(str(token), freq)


