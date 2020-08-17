import string

class Token:
	def __str__(self):
		return self.token

	def __eq__(self, other):
		return str(self) == str(other)

class CheckingToken(Token):
	def __init__(self, token):
		assert self.check(token)
		self.set(token)

	def set(self, token):
		self.token = token

	@classmethod
	def check(self, token):
		return False

class SpecialToken(Token):
	def __init__(self, token):
		self.token = f'<{token}>'

class ASCIIPunctuationToken(CheckingToken):
	punctuation_list = list(string.punctuation)

	@classmethod
	def check(self, token):
		return token in self.punctuation_list

