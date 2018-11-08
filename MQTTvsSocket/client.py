import json
import socket as sk
from uuid import getnode as get_mac

class Client():
	def __init__(self, name='', addr='127.0.0.1', porta=5001, mac=None):
		server = (addr, porta)
		tcp = sk.socket(sk.AF_INET, sk.SOCK_STREAM)#criando o socket
		self.tcp = tcp
		tcp.connect(server)#conectando o tcp ao endereço

		self._encoder = None

		self.name = name
		if mac is None:
			mac = get_mac()
		
		self.send((mac, name))

		buffer_size = int.from_bytes(tcp.recv(1024), 'big')
		self.q = self.recv(buffer_size=buffer_size)

	def send(self, data, encoder=None):
		if encoder is None:
			encoder = self._encoder
		self.tcp.send(json.dumps(data, cls=encoder, indent=4).encode())

	def recv(self, encoder=None, buffer_size=1024):
		if encoder is None:
			encoder = self._encoder
		return json.loads(self.tcp.recv(buffer_size).decode('utf-8'), object_hook=encoder)

	def disconnect(self):
		self.tcp.close()

if __name__ == '__main__':
	c = Client()