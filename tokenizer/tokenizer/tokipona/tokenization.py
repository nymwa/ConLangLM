import sys
import re
from tokenizer.tokenization import BasicTokenizer
from tokenizer.token import SpecialToken, ASCIIPunctuationToken
from tokenizer.tokipona.token import TokiPonaToken, TokiPonaProperNounToken

class TokiponaTokenizer(BasicTokenizer):
	def __init__(self):
		self.special_punct = str.maketrans({'„':'"', '“':'"', '”':'"', '–':'-', '▁':'_'})
		self.left_punct  = re.compile(r'(?<=[^\s])([\W_])')
		self.right_punct = re.compile(r'([\W_])(?=[^\s])')
		self.number = re.compile(r'(\d+)')
		self.space = re.compile(r'\s+')

	def normalize(self, x):
		x = x.strip()
		x = x.translate(self.special_punct)
		x = self.left_punct.sub(r' \1', x)
		x = self.right_punct.sub(r'\1 ', x)
		x = self.number.sub(r' \1 ', x)
		x = self.space.sub(' ', x)
		return x

	def tokenize(self, x):
		x = self.normalize(x)
		x = x.split()
		lst = []
		for token in x:
			if TokiPonaToken.check(token):
				lst.append(TokiPonaToken(token))
			elif TokiPonaProperNounToken.check(token):
				lst.append(TokiPonaProperNounToken(token))
			elif ASCIIPunctuationToken.check(token):
				lst.append(ASCIIPunctuationToken(token))
			else:
				assert False, token
		return lst


def main():
	tokenizer = TokiponaTokenizer()
	for line in sys.stdin:
		print(' '.join([str(token) for token in tokenizer.tokenize(line)]))

