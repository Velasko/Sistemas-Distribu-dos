import json

class Adm():
	def __init__(self, connection, conn):
		self.c = connection.conn
		self.connection = connection
		self.conn = conn
		self._encoder = None

	def get_devices(self):
		cont = json.dumps([[key, value.name, value.subscriptions] for key, value in self.conn.items()]).encode()
		self.c.send(len(cont).to_bytes(1024, 'big'))
		self.c.send(cont)
		print('devices sent')

	def recv(self, encoder=None, buffer_size=1024):
		if encoder is None:
			encoder = self._encoder

		data = self.c.recv(buffer_size).decode('utf-8')
		if data == "":
			return None

		return json.loads(data, object_hook=encoder)

	def send(self, data, encoder=None):
		if encoder is None:
			encoder = self._encoder
		self.c.send(json.dumps(data, cls=encoder, indent=4).encode())

	def subscribe(self, sender, reciever, function):
		self.conn.subscribe(sender, reciever, function)

	def unsubscribe(self, sender, reciever):
		self.conn.unsubscribe(sender, reciever)
		self.conn.unsubscribe(sender, reciever)
