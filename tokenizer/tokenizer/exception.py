class OutOfVocabularyException(Exception):
	def __init__(self, token, sent = None):
		self.token = token
		if sent is None:
			message = f'Token "{token}" is invalid.'
		else:
			message = f'Token "{token}" in "{sent}" is invalid.'
		super().__init__(message)

