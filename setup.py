import os

from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def run_setup():
	setup(
	  name='sqlfeedgraphite',
	  version='0.1',
	  description='https://github.com/orachide/sql-feed-graphite',
	  keywords = 'SQL Graphite Metrics',
	  url='https://github.com/orachide/sql-feed-graphite',
	  download_url = 'https://github.com/orachide/sql-feed-graphite/archive/0.1.tar.gz',
	  author='Rachide Ouattara',
	  author_email='ouattchidi@gmail.com',
	  license='BSD',
	  packages=['sqlfeedgraphite'],
	  install_requires=[
		    'sqlalchemy',
		    'psycopg2',
	  ],
	  test_suite='tests',
	  zip_safe=True,
	  classifiers=[
	   ],
	)
if __name__ == '__main__':
    run_setup()
