try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Learn Python3 The Hard Way',
    'author': 'BeatsBassBoom',
    'url': 'https://github.com/BeatsBassBoom/LP3THW',
    'download_url': 'https://github.com/BeatsBassBoom/LP3THW/archive/master.zip',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'LP3THW'
}

setup(**config)
