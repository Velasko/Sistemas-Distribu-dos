import client
import random
import time

class Sensor(client.Client):
	def __init__(self, *args, **kwargs):
		super(Sensor, self).__init__(mac=2, name='Sensor', *args, **kwargs)

		while True:
			time.sleep(2)
			value = random.random()
			self.send(value)
			print(value)


if __name__ == '__main__':
	Sensor()