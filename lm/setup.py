from setuptools import setup, find_packages

setup(
		name = 'lm',
		version = '0.1.0',
		description = 'language model',
		author = 'nymwa',
		classifiers = [ 
			'Development Status :: 3 - Alpha',
			'License :: OSI Approved :: MIT License',
			'Programming Language :: Python :: 3.8',
			'Topic :: Scientific/Engineering'],
		entry_points = { 
			'console_scripts':[
				'train-unigram-lm = lm.unigram.lm:train',
				'score-unigram-lm = lm.unigram.lm:score',
				]})


