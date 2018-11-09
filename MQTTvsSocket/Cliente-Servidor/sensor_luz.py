import client
import random
import time

class sensor_luz(client.Client):
	def __init__(self, *args, **kwargs):
		super(sensor_luz, self).__init__(mac=3, name='sensor_luz', *args, **kwargs)

		while True:
			time.sleep(2)
			value = random.random()
			self.send(value)
			print(value)


if __name__ == '__main__':
	sensor_luz()