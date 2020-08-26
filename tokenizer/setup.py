from setuptools import setup, find_packages

setup(
		name = 'tokenizer',
		version = '0.1.0',
		description = 'tokenizer',
		author = 'nymwa',
		classifiers = [ 
			'Development Status :: 3 - Alpha',
			'License :: OSI Approved :: MIT License',
			'Programming Language :: Python :: 3.8',
			'Topic :: Scientific/Engineering'],
		entry_points = { 
			'console_scripts':[
				'tokipona-tokenize = tokenizer.tokipona.tokenization:main',
				'tokipona-vocabulary = tokenizer.tokipona.vocabulary:main',
				]})


