import json
import queue
import socket
import threading

class Func():
	def __init__(self, code):
		self.code = code
		exec(code, globals())
		self.func = func

	def __str__(self):
		return self.code

	def __call__(self, *args, **kwargs):
		return self.func(*args, **kwargs)

class Conn():
	def __init__(self, conn, mac, name=''):
		self.conn = conn
		self.mac = mac
		self.name = name
		self.q = queue.Queue()
		self.qlock = threading.Lock()

		self.data = []
		self.subscriptions = []
		self.func = {}

		if mac == 2:
			self.subscriptions.append(4)
			self.func[4] = Func('''def func(data):
	return data''')
		if mac == 3:
			self.subscriptions.append(1)
			self.func[1] = Func('''def func(data):
	return data''')


	def send(self, data):
		'''data must be in str format'''
		if self.conn is not None:
			self.conn.send(json.dumps(data).encode())
		else:
			with self.qlock:
				self.q.put(data)

	def __getitem__(self, index):
		return self.func[index]

	def __setitem__(self, *args, **kwargs):
		return self.func.__setitem__(*args, **kwargs)

class Dict(dict):
	def __init__(self, *args, **kwargs):
		super(Dict, self).__init__(*args, **kwargs)
		self._conn = {}

	def init_conn(self, mac, name, conn):
		try:
			self[mac].conn = conn
			self[mac].name = name
			self._conn[conn] = mac
		except KeyError:
			super(Dict, self).__setitem__(mac, Conn(conn, mac, name))
#			self[mac] = Conn(conn, mac)

		with self[mac].qlock:
			q = str(list(self[mac].q.queue)).encode()
			self[mac].conn.send(len(q).to_bytes(1024, 'big'))
			self[mac].conn.send(q)


	def __getitem__(self, index):
		if type(index) == socket.socket:
			return self[ self._conn[index] ]
		else:
			return super(Dict, self).__getitem__(index)

	def __setitem__(*args, **kwargs):
		pass

	def subscribe(self, sender, reciever, function):
		if reciever not in self[sender].subscription:
			self[sender].subscription.append(reciever)
			self[sender][reciever] = Func(function)

	def unsubscribe(self, sender, reciever):
		if reciever in self[sender].subscription:
			self[sender].subscription.remove(reciever)
			del(self[sender][reciever])

	def disconnect(self, conn):
		client = self[conn]
		del self._conn[conn]
		client.conn = None

if __name__ == '__main__':
	c = Conn()