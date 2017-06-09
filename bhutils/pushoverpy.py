from bhutils import httpsession

class Pushover():
	def __init__(self, app_token, user_key):
		self.app_token = app_token
		self.user_key = user_key
		self.root = "https://api.pushover.net"
		self.path = "/1/messages.json"
		self.session = self.session = httpsession.HTTPSession()

	def send(self, msg):
		# Format the POST
		body = {"token" : self.app_token, "user" : self.user_key, "message" : msg}
		header = {"content-type" : "application/x-www-form-urlencoded"}
		
		# Send POST
		rv = self.session.POST(self.root, self.path, body, header)
		return rv

def main():
	''' TEST '''
	po = Pushover("a5emh7y9woca2evnmkrr9sbuntemub", "ute3atiphqoqg2kidfksd1497rfqan")
	rv = po.send("Hello Bryant!")
	print(rv)

if __name__ == "__main__":
	main()