import client

class Lampada(client.Client):
	def __init__(self, *args, **kwargs):
		super(Lampada, self).__init__(mac=1, name='Lampada', *args, **kwargs)

		while True:
			try:
				if self.recv() > 0.5:
					print('lampada: on')
				else:
					print('lampada: off')
			except KeyboardInterrupt:
				self.disconnect()
				break

if __name__ == '__main__':
	Lampada()