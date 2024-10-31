import redis

class RedisService:

    host= "127.0.0.1"
    port= "6379"
    db= "0"

    def __init__(self):
        self.redis_client = redis.Redis(host=self.host, port=self.port, db=self.db)

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
        