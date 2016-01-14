from setuptools import setup, find_packages
from codecs import open
from os import path

requires = [ 
        'pyramid'
        ]


here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'pyramid_favicon',

    # version
    version = '0.0.5',

    # description
    description = 'Pyramid add-on for defining relocatable favicon.ico',
    long_description = long_description,
    keywords = 'pyramid addon favicon',

    #url
    url='https://www.github.com/niteoweb/pyramid_favicon',
    download_url='https://pypi.python.org/pypi/pyramid_favicon',

    #author
    author = 'Niteoweb Ltd',
    author_email = 'info@niteoweb.com',
    
    license='3-clause BSD',

    classifiers = [
        'Environment :: Web Environment',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    install_requires = requires,
    tests_require = requires,
    
    entry_points = '''
        ''',

    packages = find_packages(
        exclude=['docs', 'tests']
        )
    )
    