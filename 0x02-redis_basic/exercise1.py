import redis
import uuid
from typing import Union
from functools import wraps

def count_calls(methods: callable=None) -> callable:
    """
    """
    @wraps(methods)
    def wrapper(self, data: Union[str, int, float, bytes]) -> Union[str, int, float, bytes, None]:
        key = methods.__qualname__
        self._redis.incr(key)
        return methods(self, data)
    return wrapper


class cache:
    """Class that implement cache
    """
    def __init__(self):
        """Implement redis and flushdb
        """
        self._redis = redis.Redis()
        self._redis.flushdb()
   
    @count_calls
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
    
    def get_int(self, key: str) -> Union[int, None]:
        """Return key in 'int'
        """
        value = self._redis.get(key)
        try:
            value = int(value.decode('utf-8'))
        except Exception:
            return None
        
        return value
    
    def get_str(self, key: str) -> Union[str, None]:
        """Return key in 'str'
        """
        return self._redis.get(key).decode('utf-8')
    