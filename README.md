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
