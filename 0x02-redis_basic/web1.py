import redis 
import requests
from typing import Callable
from functools import wraps

r = redis.Redis()

def count_call(method: Callable) -> Callable:
    """
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        r.incr(f"count:{url}")
        page_content = r.get(f"cache:{url}")
        if page_content:
            return page_content.decode('utf-8')

        html = method(url)
        r.setex(f"cache:{url}, html")

def get_page(url: str) -> str:
    page_url = r.get(url)
    
    if page_url:
        page_url = page_url.decode('utf-8')

    response = requests.get(url)
    page_content = response.content.decode('utf-8')
    r.setex()


