import unittest
from app.main import create_app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_get_items(self):
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
