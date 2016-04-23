try:
	from setuptools import setup
except
	from distutils.core import setup

config = {
	'description': 'Transcription Project',
	'author': 'Dylan Medina',
	'url': 'https://github.com/dlondonmedina/transcription',
	'download_url': 'https://github.com/dlondonmedina/transcription',
	'author_email': 'dylan@dylanmedina.com',
	'version': '0.1',
	'install_requires': ['speech_transcription', 'pocketsphinx', 'sphinxbase'],
	'packages': ['transcription'],
	'scripts': [],
	'name': 'transcriptionproject'
}

setup(**config)
