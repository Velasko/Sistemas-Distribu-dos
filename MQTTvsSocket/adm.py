import time
import client
import threading
import tkinter as tk

class Function():
	def __init__(self, f, *args, **kwargs):
		self.f = f
		self.args = args
		self.kwargs = kwargs

	def __call__(self):
		self.f(*self.args, *self.kwargs)

class Adm(client.Client):
	def __init__(self, *args, **kwargs):
		super(Adm, self).__init__(mac=0, name='ADM', *args, **kwargs)

		self.buttons = []
		self.root = tk.Tk()
		self.main_page()

		tk.mainloop()

	def clear_page(self):
		for button in self.buttons:
			button.destroy()
		self.buttons = []

	def main_page(self):
		self.clear_page()
		self.devices = self.update_devices()

		for key, name, subscriptions in self.devices:
			if name == 'ADM': continue
			button = tk.Button(self.root, text=name, command=Function(self.second_page, key, subscriptions))
			button.pack()
			self.buttons.append(button)

	def second_page(self, key, subscriptions):
		self.clear_page()

		for key_other, name_other, _ in self.devices:
			print(key, key_other, subscriptions)
			if name_other == 'ADM' or key == key_other: continue
			if key_other in subscriptions:
				button = tk.Button(self.root, text=f'{name_other} - subscribed', command=lambda: self.unsubscribe(key_other, key))
			else:
				text = f'{name_other} - not subscribed'
				button = tk.Button(self.root, text=text, command=lambda: self.code_page(key_other, key))				
			button.pack()
			self.buttons.append(button)

		button = tk.Button(self.root, text='<- back', command=lambda: self.main_page())
		button.pack()
		self.buttons.append(button)

	def code_page(self, sender, reciever):
		self.clear_page()

		my_msg = tk.StringVar()
		my_msg.set('''def func(data):\n\treturn data''')
		entry_field = tk.Entry(self.root, textvariable=my_msg)
		entry_field.bind("<ctr><Return>", lambda: self.subscribe(sender, reciever, my_msg.get()))
		entry_field.pack()
		self.buttons.append(entry_field)
		self.buttons.append(my_msg)

	def keep_alive(self):
		while True:
			self.send(None)

	def update_devices(self):
		self.send(('get_devices',))

		buffer_size = int.from_bytes(self.tcp.recv(1024), 'big')
		return self.recv(buffer_size=buffer_size)

	def subscribe(self, sender, reciever, function):
		self.send(('subscribe', sender, reciever, function))
		self.main_page()

	def unsubscribe(self, sender, reciever):
		self.send(('unsubscribe', sender, reciever, function))
		self.main_page()

if __name__ == '__main__':
	Adm()