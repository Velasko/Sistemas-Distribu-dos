import time
import client

class Ccdc(client.Client):
	def __init__(self, *args, **kwargs):
		super(Ccdc, self).__init__(mac=5, name='Ccdc', *args, **kwargs)

		while True:
			try:
				time.sleep(5)
				print('Ccdc')
				self.send('Ccdc')
			except KeyboardInterrupt:
				self.disconnect()
				break

if __name__ == '__main__':
	Ccdc()