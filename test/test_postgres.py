from unittest import TestCase

from sql_feed_graphite import get_executor


class TestSelectFromMySQL(TestCase):

    def test_mysql_executor(self):
        dsn = 'mysql://root@localhost/sql-to-graphite'
        executor = get_executor(dsn)
        result = list(executor('SELECT 1+1;'))
        self.assertEqual(result, [(2,)])
