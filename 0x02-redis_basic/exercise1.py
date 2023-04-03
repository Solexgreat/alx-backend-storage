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
    
    def get(self, key: str, fn: callable=None) -> Union[str, bytes, int, float, None]:
        """Return key in the desired fn(format)
        """
        value = self._redis.get(key)
        if value is not value:
            if fn is not None:
                value = fn(value)
            
            else:
                return value

        return None
    
    def get_int(self, key: str, fn: callable=None) -> Union[int, None]:
        """Return key in 'int'
        """
        value = self._redis.get(key)
        if value is not value:
            if fn is not None:
                if isinstance(fn, int):
                    value = int(value)
            
            else:
                return value

        return None
    
    def get_str(self, key: str, fn: callable=None) -> Union[str, None]:
        """Return key in 'str'
        """
        value = self._redis.get(key)
        if value is not value:
            if fn is not None:
                if isinstance(fn, str):
                    value = str(value)
            
            else:
                return value

        return None