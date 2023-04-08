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

def call_history(method: callable=None) -> callable:
    """Decorator call history
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper function"""
        key = method.__qualname__
        input_key = f"{key}:inputs"
        output_key = f"{key}:outputs"
    
    
        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))

        return str(result)
    return wrapper

def replay(func: callable):
    r = redis.Redis()
    func_name = func.__qualname__
    number_calls = r.get(func_name)

    try:
        number_calls = number_calls.decode('utf-8')
    except Exception:
        number_calls = 0

    input = r.lrange(f"{func_name}:inputs", 0, -1)
    output = r.lrange(f"{func_name}:outputs", 0, -1)

    for ins, outs in zip(input, output):
        try:
            ins = ins.decode('utf-8')
        except Exception:
            ins = ""
        try:
            out = ins.decode('utf-8')
        except Exception:
            outs = ""

    #Cache.store(*('foo',)) -> 13bf32a9-a249-4664-95fc-b1062db2038f
    print (f"{func_name }(*({ins})) -> {outs}")


class cache:
    """Class that implement cache
    """
    def __init__(self):
        """Implement redis and flushdb
        """
        self._redis = redis.Redis()
        self._redis.flushdb()
   
    @count_calls
    @call_history
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
    