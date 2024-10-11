import redis
import json
import os

redis_host = os.getenv('REDIS_HOST', 'redis-service')
redis_port = int(os.getenv('REDIS_PORT', 6379))
redis_client = redis.Redis(host=redis_host, port=redis_port, db=0)

class Item:
    @staticmethod
    def get_redis_client():
        return redis_client

    def __init__(self, name, description):
        self.id = self.get_redis_client().incr('item_id')
        self.name = name
        self.description = description

    def save(self):
        self.get_redis_client().hset('items', self.id, json.dumps(self.to_dict()))

    @staticmethod
    def get_all():
        return [json.loads(item) for item in Item.get_redis_client().hvals('items')]

    @staticmethod
    def get(item_id):
        item = Item.get_redis_client().hget('items', item_id)
        return json.loads(item) if item else None

    @staticmethod
    def delete(item_id):
        Item.get_redis_client().hdel('items', item_id)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }
