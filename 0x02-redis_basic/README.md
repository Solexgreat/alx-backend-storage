# 0x02. Redis basic
* Learn how to use redis for basic operations
* Learn how to use redis as a simple cache
<img src="https://files.realpython.com/media/A-Guide-to-Redis--Python_Watermarked.fadbf320f71f.jpg" width="600px"/>
## Resources

Read or watch:

* [Redis commands](https://redis.io/commands/)
* [Redis python client](https://redis-py.readthedocs.io/en/stable/)
* [How to Use Redis With Python](https://realpython.com/python-redis/)
* [Redis Crash Course Tutorial](https://www.youtube.com/watch?v=Hbt56gFj998)
## Installation
* `sudo apt-get -y install redis-server`

* `pip3 install redis`

* `sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf`

Redis server is stopped by default - when you are starting a container, you should start it with:

* `service redis-server start`

## Technologies
* Ubuntu 18.04