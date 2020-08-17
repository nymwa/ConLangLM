from tokenizer.token import SpecialToken

class Vocabulary(list):
	def __init__(self, vocab, bos_token = None, unk_token = None, eos_token = None, has_bos = True, has_unk = True, has_eos = True, additional_special_token_list = None):
		special_token_list = []

		if has_bos:
			self.bos_token = bos_token = bos_token if bos_token else SpecialToken('s')
			special_token_list.append(self.bos_token)

		if has_unk:
			self.unk_token = unk_token = unk_token if unk_token else SpecialToken('unk')
			special_token_list.append(self.unk_token)

		if has_eos:
			self.eos_token = eos_token = eos_token if eos_token else SpecialToken('/s')
			special_token_list.append(self.eos_token)

		if additional_special_token_list is not None:
			specail_token_list += [SpecialToken(token) for token in additional_special_token_list]

		super().__init__(special_token_list + [token for token in vocab if all(special_token != token for special_token in special_token_list)])
		self.index_dict = {str(word) : n for n, word in enumerate(self)}

		for special_token in special_token_list:
			setattr(self, str(special_token), self.index_dict[str(special_token)])

	def __contains__(self, x):
		return x in self.index_dict

	 def word_to_index(self, x):
		 return self.index_dict[x] if x in self.index_dict else self.unk


def prepare_vocab(sents, ignore_tokens = None):
	counter = Counter([word for sent in sents for word in sent])
	 x = counter.most_common()
	 if ignore_tokens is None:
		 ignore_tokens = {}
	 else:
		 ignore_tokens = set(ignore_tokens)
	 vocab = [word for word, freq in x if word not in ignore_tokens]
	 return Vocabulary(vocab)

