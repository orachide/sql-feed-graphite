from sqlfeedgraphite import get_executor


dsn = 'postgresql://test:test@localhost:5432/test'
executor = get_executor(dsn)
result = list(executor('SELECT 1+1;'))
print(result)
