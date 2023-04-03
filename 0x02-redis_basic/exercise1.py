import redis
import uuid
from typing import Union


class cache:
    """Class that implement cache
    """
    def __init__(self):
        """Implement redis and flushdb
        """
        self._redis = redis.Redis()
        self._redis.flushdb()
   
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store method takes a single argument, data,
           which can be a string, bytes, int or float,
           return the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key