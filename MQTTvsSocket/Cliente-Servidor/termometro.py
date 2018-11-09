import client
import random
import time

class Termometro(client.Client):
	def __init__(self, *args, **kwargs):
		super(Termometro, self).__init__(mac=2, name='Termometro', *args, **kwargs)

		while True:
			time.sleep(2)
			value = 20 + random.randrange(1, 20)
			self.send(value)
			print(value)


if __name__ == '__main__':
	Termometro()