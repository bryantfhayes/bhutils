from bhutils import pushoverpy
import warnings, json, unittest

class TestPushover(unittest.TestCase):
    def test_notify(self):
        # Get pushover instance
        push = pushoverpy.Pushover("a5emh7y9woca2evnmkrr9sbuntemub")

        # Send notification
        rv = push.send("awesome title")
        print(rv)

        self.assertTrue(rv != None)

if __name__ == '__main__':
    unittest.main()