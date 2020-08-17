import re
from tokenizer.token import CheckingToken

class TokiPonaToken(CheckingToken):
	nimi_list = ['a', 'akesi', 'ala', 'alasa', 'ale', 'ali', 'anpa', 'ante', 'anu', 'apeja', 'awen', 'e', 'en', 'esun', 'ijo', 'ike', 'ilo', 'insa', 'jaki', 'jan', 'jelo', 'jo', 'kala', 'kalama', 'kama', 'kan', 'kasi', 'ken', 'kepeken', 'kijetesantakalu', 'kili', 'kin', 'kipisi', 'kiwen', 'ko', 'kon', 'kule', 'kulupu', 'kute', 'la', 'lape', 'laso', 'lawa', 'leko', 'len', 'lete', 'li', 'lili', 'linja', 'lipu', 'loje', 'lon', 'luka', 'lukin', 'lupa', 'ma', 'majuna', 'mama', 'mani', 'meli', 'mi', 'mije', 'moku', 'moli', 'monsi', 'monsuta', 'mu', 'mulapisu', 'mun', 'musi', 'mute', 'namako', 'nanpa', 'nasa', 'nasin', 'nena', 'ni', 'nimi', 'noka', 'o', 'oko', 'olin', 'ona', 'open', 'pakala', 'pake', 'pali', 'palisa', 'pan', 'pana', 'pata', 'pi', 'pilin', 'pimeja', 'pini', 'pipi', 'poka', 'poki', 'pona', 'pu', 'sama', 'seli', 'selo', 'seme', 'sewi', 'sijelo', 'sike', 'sin', 'sina', 'sinpin', 'sitelen', 'sona', 'soweli', 'suli', 'suno', 'supa', 'suwi', 'tan', 'taso', 'tawa', 'telo', 'tenpo', 'toki', 'tomo', 'tu', 'unpa', 'uta', 'utala', 'walo', 'wan', 'waso', 'wawa', 'weka', 'wile', 'yupekosi']

	@classmethod
	def check(self, token):
		return token in self.nimi_list

class TokiPonaProperNounToken(CheckingToken):
	proper_noun_pattern = re.compile(r'^([AIUEO]|[KSNPML][aiueo]|[TJ][aueo]|W[aie])n?(([ksnpml][aiueo]|[tj][aueo]|w[aie])n?)*$')

	@classmethod
	def check(self, token):
		return self.proper_noun_pattern.match(token)

