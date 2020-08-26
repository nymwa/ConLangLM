import sys
import re
from argparse import ArgumentParser
from tokenizer.exception import OutOfVocabularyException
from tokenizer.tokenization import BasicTokenizer
from tokenizer.token import Token, SpecialToken, ASCIIPunctuationToken
from tokenizer.sentence import Sentence
from tokenizer.tokipona.token import TokiPonaToken, TokiPonaProperNounToken

class TokiPonaTokenizer(BasicTokenizer):
	def __init__(
			self,
			bos_symbol = 'bos',
			unk_symbol = 'unk',
			eos_symbol = 'eos',
			additional_special_token_list = [],
			allow_unk = True,
			):
		super().__init__(
				bos_symbol = bos_symbol,
				unk_symbol = unk_symbol if allow_unk else None,
				eos_symbol = eos_symbol,
				additional_special_token_list = additional_special_token_list,
				)
		self.special_punct = str.maketrans({'„':'"', '“':'"', '”':'"', '–':'-', '▁':'_'})
		self.left_punct  = re.compile(r'(?<=[^\s])([\W_])')
		self.right_punct = re.compile(r'([\W_])(?=[^\s])')
		self.number = re.compile(r'(\d+)')

	@property
	def proper_noun_token(self):
		assert Token.replace_proper_noun
		if not hasattr(self, '_special_token'):
			self._proper_noun = TokiPonaProperNounToken()
		return self._proper_noun

	def normalize(self, x):
		x = x.translate(self.special_punct)
		x = self.left_punct.sub(r' \1', x)
		x = self.right_punct.sub(r'\1 ', x)
		x = self.number.sub(r' \1 ', x)
		x = ' '.join(x.split())
		return x

	def symbol_tokenize(self, symbol):
		if TokiPonaToken.check(symbol):
			token = TokiPonaToken(symbol)
		elif TokiPonaProperNounToken.check(symbol):
			token = TokiPonaProperNounToken(symbol)
		elif ASCIIPunctuationToken.check(symbol):
			token = ASCIIPunctuationToken(symbol)
		elif Token.replace_proper_noun and symbol == self.proper_noun_token:
			token = self.proper_noun_token
		else:
			token = self.unk_token
		return token


def main():
	parser = ArgumentParser()
	parser.add_argument('--replace-proper-noun', action = 'store_true')
	parser.add_argument('--remove-sentence-with-unk', action = 'store_true')
	args = parser.parse_args()

	if args.replace_proper_noun:
		Token.replace_proper_noun = True
	tokenizer = TokiPonaTokenizer(allow_unk = not args.remove_sentence_with_unk)

	for line in sys.stdin:
		line = line.strip()
		try:
			print(tokenizer.tokenize(line))
		except OutOfVocabularyException as e:
			if args.remove_sentence_with_unk:
				print('OOV Exception :', e, file = sys.stderr)
			else:
				raise e

