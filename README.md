# sql-feed-graphite
Read datas from SQL database and send metrics to Graphite

## How to install

### Using ``pip``

```:sh
pip install sql-feed-graphite
```
### From git rpo

```:sh
git clone https://github.com/orachide/sql-feed-graphite.git
cd sql-feed-graphite
python setup.py build
python setup.py install
```

## Docker image

A Docker image with cron job to execute *sql-feed-graphite* is available [here](https://github.com/orachide/docker-sql-feed-graphite)

## Configuration

Followings environment variables can be used to configure the script
- SQL_FEED_GRAPHITE_DB_URL='postgresql://test:test@localhost:5432/test'
- SQL_FEED_GRAPHITE_PREFIX='metrics'
- SQL_FEED_GRAPHITE_HOST='localhost'
- SQL_FEED_GRAPHITE_PORT=5432 
- SQL_FEED_GRAPHITE_QUERIES_DIR='/var/datas/queries/'
