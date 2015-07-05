try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A simple CMS made in python with the only purpose to learn the language',
    'author': 'Alejo Arias',
    'url': 'http://github.com/alejoar',
    'download_url': '',
    'author_email': '',
    'version': '0.1',
    'install_requires': ['web'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'simpleCMSpy'
}

setup(**config)
