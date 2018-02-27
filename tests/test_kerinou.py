import unittest

import kerinou


class KerinouTestCase(unittest.TestCase):

    def setUp(self):
        self.app = kerinou.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to kerinou', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
