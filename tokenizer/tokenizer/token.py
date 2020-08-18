import string

class Token:
	replace_proper_noun = False

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

class ProperNounToken(Token):
	tag = 'proper'

	def __str__(self):
		if self.replace_proper_noun:
			x =  f'<{self.tag}>'
		else:
			x = self.token
		return x

class SpecialToken(Token):
	def __init__(self, token):
		self.token = f'<{token}>'

class ASCIIPunctuationToken(CheckingToken):
	punctuation_list = list(string.punctuation)

	@classmethod
	def check(self, token):
		return token in self.punctuation_list

