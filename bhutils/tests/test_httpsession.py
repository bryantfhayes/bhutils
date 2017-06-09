from bhutils import httpsession
import warnings, json, unittest

class TestHTTPSession(unittest.TestCase):
    def test_post(self):
        # Open HTTPSession
        session = httpsession.HTTPSession()

        # Issue a test POST request
        rv = session.POST("http://httpbin.org", "/post", {})
        self.assertTrue('data' in rv)

        try:
            rv = session.POST("http://thisisnotarealsite.org", "/post", {})
        except:
            self.assertTrue('data' in rv)

    def test_get(self):
        # Open HTTPSession()
        session = httpsession.HTTPSession()

        # Issue a test GET request
        rv = session.GET("http://httpbin.org", "/get", {})
        print(rv)
        self.assertTrue('args' in rv)

        try:
            rv = session.GET("http://thisisnotarealsite.org", "/get", {})
        except:
            self.assertTrue('args' in rv)

if __name__ == '__main__':
    unittest.main()