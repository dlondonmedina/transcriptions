try:
	from setuptools import setup
except
	from distutils.core import setup

config = {
	'description': 'Transcription Project',
	'author': 'Dylan Medina',
	'url': 'URL to get it',
	'download_url': 'Where to download it.',
	'author_email': 'medinad@uw.edu',
	'version': '0.1',
	'install_requires': ['none'],
	'packages': ['transcription'],
	'scripts': [],
	'name': 'transcriptionproject'
}

setup(**config)

