import argparse
import os
import socket
import sys
import time
import json

import sqlalchemy

def get_executor(dbUrl):
    engine = sqlalchemy.create_engine(dbUrl, isolation_level='READ UNCOMMITTED')
    connection = engine.connect()
    return connection.execute

def run(graphite_host, graphite_port, graphite_prefix, executor , **query):
    resultRow = []
    now = time.time()
    sock = _socket_for_host_port(graphite_host, graphite_port)
    resultRow = executor(query['sql'])
    for result in resultRow:
        metric, value = result[:2]
        metric = '{0}.{1} {2} {3}\n'.format(graphite_prefix, metric, value, now)
        print metric,
        sock.sendall(metric)
    sock.close()

def _socket_for_host_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)
    sock.connect((host, port))
    sock.settimeout(None)
    return sock


def main():
    graphiteHost = os.environ.get('SQL_FEED_GRAPHITE_HOST')
    if graphiteHost is None:
        graphiteHost = 'localhost'
    graphitePort = os.environ.get('SQL_FEED_GRAPHITE_PORT')
    if graphitePort is None:
        graphitePort = 5432
    graphitePrefix = os.environ.get('SQL_FEED_GRAPHITE_PREFIX')
    if graphitePrefix is None:
        print 'You must set your graphitePrefix in the environment variable `SQL_FEED_GRAPHITE_PREFIX`'
        sys.exit(1)
    dbUrl = os.environ.get('SQL_FEED_GRAPHITE_DB_URL')
    if dbUrl is None:
        print 'You must set your DBUrl in the environment variable `SQL_FEED_GRAPHITE_DB_URL`'
        sys.exit(1)
    queriesDIR = os.environ.get('SQL_FEED_GRAPHITE_QUERIES_DIR')
    if queriesDIR is None:
        queriesDIR = os.getcwd()
    for filename in os.listdir(queriesDIR):
        if filename.endswith(".json"): 
            currentFile = os.path.join(queriesDIR, filename)
            print('Processing file',currentFile)
            with open(currentFile) as data_file:    
                data = json.load(data_file)
                print(data["queries"])
                for query in data["queries"]:
                    print(query['sql'])
                    run(
                        graphiteHost,
                        graphitePort,
                        graphitePrefix,
                        get_executor(dbUrl),
                        **query
                    )
            continue
        
def excepthook(type, value, tb):
    # you can log the exception to a file here
    print ('ERROR:',type,value)

    # the following line does the default (prints it to err)
    sys.__excepthook__(type, value, tb)

sys.excepthook = excepthook

if __name__ == '__main__':
    main()
