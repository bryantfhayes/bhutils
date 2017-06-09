import os, sys
from bhutils import httpsession

#TODO: Finish firebase implementation
class FirebaseApplication():
    def __init__(self, root):
        self.session = httpsession.HTTPSession()
        self.root = root

    def __del__(self):
        del self.session

    def get(self, path):
        rv = self.session.GET(self.root, path + ".json", {})
        print(rv)

    def put(self, path, data):
        rv = self.session.PUT(self.root, path + ".json", data)
        print(rv)


def main():
    # EXAMPLE:
    #
    # fb = FirebaseApplication("https://secret-hitler-4415c.firebaseio.com/")
    # rv = fb.put("games", {"game" : "newgame"})
    # print(rv)
    pass

if __name__ == "__main__":
    main()