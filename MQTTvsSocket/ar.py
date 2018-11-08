import client

class Ar_condicionado(client.Client):
	def __init__(self, *args, **kwargs):
		super(Ar_condicionado, self).__init__(mac=4, name='Ar_condicionado', *args, **kwargs)

		while True:
			try:
				if self.recv() > 27:
					print('Ar: on')
				else:
					print('Ar: off')
			except KeyboardInterrupt:
				self.disconnect()
				break

if __name__ == '__main__':
	Ar_condicionado()