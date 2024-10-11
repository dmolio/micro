import unittest
import json
from unittest.mock import patch
from app.main import create_app
from app.models import Item, redis_client

class MockRedis:
    def __init__(self):
        self.data = {}

    def incr(self, key):
        if key not in self.data:
            self.data[key] = 0
        self.data[key] += 1
        return self.data[key]

    def hset(self, name, key, value):
        if name not in self.data:
            self.data[name] = {}
        self.data[name][key] = value

    def hget(self, name, key):
        return self.data.get(name, {}).get(key)

    def hvals(self, name):
        return list(self.data.get(name, {}).values())

    def hdel(self, name, key):
        if name in self.data and key in self.data[name]:
            del self.data[name][key]

    def flushdb(self):
        self.data = {}

class TestApp(unittest.TestCase):
    def setUp(self):
        self.redis_mock = MockRedis()
        self.redis_patcher = patch('app.models.redis_client', self.redis_mock)
        self.redis_patcher.start()
        self.app = create_app()
        self.client = self.app.test_client()
        # Clear items before each test
        self.redis_mock.flushdb()

    def tearDown(self):
        self.redis_patcher.stop()

    def test_get_items(self):
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'items': []})

    def test_create_item(self):
        item_data = {'name': 'Test Item', 'description': 'This is a test item'}
        response = self.client.post('/items', json=item_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['name'], 'Test Item')
        self.assertEqual(response.json['description'], 'This is a test item')

    def test_get_item(self):
        item = Item('Test Item', 'This is a test item')
        item.save()
        response = self.client.get(f'/items/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'Test Item')

    def test_update_item(self):
        item = Item('Test Item', 'This is a test item')
        item.save()
        update_data = {'name': 'Updated Item', 'description': 'This item was updated'}
        response = self.client.put(f'/items/{item.id}', json=update_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'Updated Item')

    def test_delete_item(self):
        item = Item('Test Item', 'This is a test item')
        item.save()
        response = self.client.delete(f'/items/{item.id}')
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(Item.get(item.id))

if __name__ == '__main__':
    unittest.main()
