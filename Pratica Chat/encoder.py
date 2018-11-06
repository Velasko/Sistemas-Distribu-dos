import json
import user
import chat

class MyEncoder(json.JSONEncoder):
	def default(self, o):
		return {'__{}__'.format(o.__class__.__name__): o.__dict__}

	def decode_object(o):
		if '__User__' in o:
			u = user.User(None, None)

			u.__dict__.update(o['__User__'])

			return u

		elif '__Message__' in o:
			m = user.Message(None, None)

			m.__dict__.update(p['__Message__'])

			return m

		elif '__Chat__' in o:
			c = chat.Chat()

			c.__dict__.update(o['__Chat__'])

			return c

		return o

def dumps(var):
	return json.dumps(var, cls=MyEncoder, indent=4)

def loads(var):
	return json.loads(var, object_hook=MyEncoder.decode_object)
