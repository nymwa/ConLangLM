import sys
import pickle
from argparse import ArgumentParser
from collections import Counter
from tokenizer.preprocess import tokenize_lines, prepare_vocab
from tokenizer.vocabulary import Vocabulary
from tokenizer.token import Token
from tokenizer.tokipona.tokenization import TokiPonaTokenizer

class TokiPonaVocabulary(Vocabulary):
	def __init__(self):
		super().__init__(vocab, additional_special_token_list = ['proper'])

def main():
	parser = ArgumentParser()
	parser.add_argument('vocab_name')
	parser.add_argument('--proper-noun-as-special', action = 'store_true')
	parser.add_argument('--no-unk', action = 'store_true')
	args = parser.parse_args()

	if args.proper_noun_as_special:
		Token.replace_proper_noun = True
	tokenizer = TokiPonaTokenizer(allow_unk = not args.no_unk)

	sents = [tokenizer.load_tokenized(line) for line in sys.stdin]
	vocab = Vocabulary(tokenizer, sents)

	vocab.show()

	with open(f'{args.vocab_name}.vocab', 'wb') as f:
		pickle.dump(vocab, f)

