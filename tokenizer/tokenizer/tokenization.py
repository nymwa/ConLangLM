from tokenizer.token import Token, ProperNounToken, SpecialToken
from tokenizer.sentence import Sentence
from tokenizer.exception import OutOfVocabularyException

class BasicTokenizer:
	def __init__(
			self,
			bos_symbol = None,
			unk_symbol = None,
			eos_symbol = None,
			additional_special_token_list = [],
			):
		self.bos_token = SpecialToken(bos_symbol, 'bos') if bos_symbol is not None else None
		self.unk_token = SpecialToken(unk_symbol, 'unk') if unk_symbol is not None else None
		self.eos_token = SpecialToken(eos_symbol, 'eos') if eos_symbol is not None else None

		self.special_token_list = []
		if self.bos_token is not None:
			self.special_token_list.append(self.bos_token)
		if self.unk_token is not None:
			self.special_token_list.append(self.unk_token)
		if self.eos_token is not None:
			self.special_token_list.append(self.eos_token)
		if Token.replace_proper_noun:
			self.special_token_list.append(self.proper_noun_token)
		self.special_token_list += additional_special_token_list

	@property
	def proper_noun_token(self):
		assert Token.replace_proper_noun
		if not hasattr(self, '_special_token'):
			self._proper_noun = ProperNounToken()
		return self._proper_noun

	def normalize(self, x):
		x = ' '.join(x.split())
		return x

	def symbols_to_sentence(self, symbol_list):
		sent = Sentence()
		for symbol in symbol_list:
			token = self.symbol_tokenize(symbol)
			if token is None:
				raise OutOfVocabularyException(symbol, sent = ' '.join(symbol_list))
			sent.append(token)
		return sent

	def load_tokenized(self, line):
		return self.symbols_to_sentence(line.strip().split())

	def tokenize(self, raw):
		raw = raw.strip()
		lst = self.normalize(raw).split()
		return symbols_to_sentence(lst)

	def detokenize(self, token_list):
		return ' '.join([str(token) for token in token_list])

