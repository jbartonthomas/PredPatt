from setuptools import setup

setup(name='predpatt',
      version='1.0',
      description='Multilingual predicate-argument extraction from universal dependency syntax.',
      packages=['predpatt', 'predpatt.util'],
      install_requires=['concrete==4.11.10',
			'networkx==2.2',
                        'termcolor',
                        'nltk>=3.0',
                        'bottle',
                        'tabulate',
                        'PyStanfordDependencies',
                        'jpype1',
                        'future']
)
