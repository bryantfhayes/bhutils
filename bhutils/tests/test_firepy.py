from bhutils import firepy
import warnings, json, unittest

class TestFirepy(unittest.TestCase):
    def test_get(self):
        # Open Firebase connection
        fb = firepy.FirebaseApplication('https://secret-hitler-4415c.firebaseio.com/', None)
        result = fb.get('/games', None)
        self.assertTrue(result != None)
        
if __name__ == '__main__':
    unittest.main()