import redis

# 连接到Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# 监视一个键
r.watch('key1')

# 开启事务
pipe = r.pipeline()

# 尝试修改键
pipe.set('key1', 'new_value')

# 执行事务
try:
    results = pipe.execute()
    print(results)
except redis.WatchError:
    print("Transaction aborted due to key change.")