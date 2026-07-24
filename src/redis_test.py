# -*- coding: utf-8 -*-

import redis

#直连方式
#r = redis.Redis(host='127.0.0.1',port=6379,db=0)

#连接池
pool = redis.ConnectionPool(host='127.0.0.1', port=6379,db=0)
r = redis.Redis(connection_pool=pool)

r.set('first_key','test')
keys = r.keys()
print(keys)

value = r.get('first_key')
print(value)