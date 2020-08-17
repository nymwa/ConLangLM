from tokenizer.vocabulary import Vocabulary

class TokiPonaVocabulary(Vocabulary):
	def __init__(self):
		super().__init__(vocab, has_unk = False, additional_special_token_list = ['proper'])



