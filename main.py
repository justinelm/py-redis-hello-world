import redis

#init redis
r = redis.StrictRedis(host="cdmp-lab20-jm-3.escwrb.0001.apse1.cache.amazonaws.com", port=6379, db=0)
#set keys
r.set('hello', 'world')
#get keys

#return ok
print(r.get('hello')) 