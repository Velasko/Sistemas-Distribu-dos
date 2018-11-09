import client

class Recep(client.Client):
	def __init__(self, *args, **kwargs):
		super(Recep, self).__init__(mac=1, name='receptor', *args, **kwargs)

		while True:
			try:
				print(self.recv())
			except KeyboardInterrupt:
				self.disconnect()
				break

if __name__ == '__main__':
	Recep()