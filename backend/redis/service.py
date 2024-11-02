import redis

class RedisService:

    # This class is used to connect to redis server and perform operations on it.
    # Redis is a cache server that is used to store data in memory.
    # It is used to store session data, tokens, and other data that needs to be accessed quickly.

    def __init__(self, host='localhost', port=6379, db=0):
        self.redis_client = redis.Redis(host=host, port=port, db=db)

    def set(self, key, value, session_id:str):
        self.redis_client.set(session_id + key, value)

    def get(self, key, session_id:str):
        return self.redis_client.get(session_id + key)

    def delete(self, key, session_id:str):
        self.redis_client.delete(session_id + key)

    def push(self, key, value, session_id:str):
        self.redis_client.rpush(session_id + key, value)    

    def flushall(self):
        self.redis_client.flushall()

    def keys(self, pattern):
        return self.redis_client.keys(pattern)

    def close(self):
        self.redis_client.connection_pool.disconnect()
        