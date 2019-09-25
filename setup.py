try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': '새 프로젝트',
    'author': 'Mark S. Hong',
    'url': '프로젝트 URL',
    'download_url': '내려 받을 수 있는 곳.',
    'author_email': 'sunmark@nate.com',
    'version': '0.1',
    'install_requires': ['pytest',]
    'packages': ['NAME']
    'scripts': [],
    'name': 'ProjectName', 
}

setup(**config)