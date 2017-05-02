import os

from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def run_setup():
    setup(
	  name='sql-feed-graphite',
	  version='0.3',
	  description='https://github.com/orachide/sql-feed-graphite',
	  keywords = 'SQL Graphite Metrics',
	  url='https://github.com/orachide/sql-feed-graphite',
	  download_url = 'https://github.com/orachide/sql-feed-graphite/archive/0.3.tar.gz',
	  author='Rachide Ouattara',
	  author_email='ouattchidi@gmail.com',
	  license='BSD',
	  packages=['sql_feed_graphite'],
	  install_requires=[
		    'sqlalchemy',
		    'psycopg2',
            'mysql-python',
	  ],
	  zip_safe=True,
	  classifiers=[
	   ],
      entry_points="""
      [console_scripts]
      sql-feed-graphite=sql_feed_graphite:main
      """,
	)
if __name__ == '__main__':
    run_setup()
