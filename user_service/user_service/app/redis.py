import redis

redis_conn = redis.Redis(host='redis', port=6379, db=0)