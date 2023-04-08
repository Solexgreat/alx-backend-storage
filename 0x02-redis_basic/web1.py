import redis 
import requests

r = redis.Redis()
def get_page(url: str) -> str:
    page_url = r.get(url)
    
    if page_url:
        page_url = page_url.decode('utf-8')

