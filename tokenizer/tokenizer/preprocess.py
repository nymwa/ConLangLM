from collections import Counter
from tokenizer.exception import OutOfVocabularyException

def tokenize_sentence(tokenizer, line):
	try:
		token_list = tokenizer.tokenize(line)
	except OutOfVocabularyException as e:
		if tokenizer.unk_token is not None:
			raise e
	return token_list

def tokenize_lines(tokenizer, f):
	for line in f:
		yield tokenize_sentence(tokenizer, line)

def prepare_vocab(vocab_cls, sents, ignore_tokens = None):
	counter = Counter([word for sent in sents for word in sent])
	x = counter.most_common()
	if ignore_tokens is None:
		ignore_tokens = {}
	else:
		ignore_tokens = set(ignore_tokens)
	vocab = [word for word, freq in x if word not in ignore_tokens]
	return vocab_cls(vocab)

