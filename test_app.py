import unittest
from app import app

class RestaurantFinderTest(unittest.TestCase):

    def setUp(self):
        # Set up the test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        # Test if home page loads correctly
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Restaurant Finder', response.data)

    def test_search_functionality(self):
        # Test a search 
        response = self.app.get('/?postcode=L40TH')
        self.assertEqual(response.status_code, 200)

    def test_no_postcode_handling(self):
        # Test empty search
        response = self.app.get('/?postcode=')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Discovering local gems', response.data)

    def test_invalid_postcode_handling(self):
        # Test invalid postcode
        response = self.app.get('/?postcode=L40THX')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'We are sorry', response.data)

if __name__ == '__main__':
    unittest.main()