import json
import socket
import threading
import adm_server
import connections

def standby(conns, mac):
	loop = True
	while loop:
		try:
			recv = json.loads(conns[mac].conn.recv(1024).decode('utf-8'))
			conns[mac].data.append(recv)
			for sub in conns[mac].subscriptions:
				func = conns[mac][sub]
				conns[sub].send( func(recv) )
		except json.decoder.JSONDecodeError:
			conns[mac].conn.close()
			conns[mac].conn = None
			loop = False

def adm_connection(conns, mac):
	adm = adm_server.Adm(conns[mac], conns)

	quit = False
	while not quit:
		request = adm.recv()
		if request is None: continue
		print(f'request: {request}')
		getattr(adm, request[0])(*request[1:])

def main(addr='127.0.0.1', porta=5001):

	conns = connections.Dict()

	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server = (addr, porta)
	tcp.settimeout(10000)
	tcp.bind(server)
	tcp.listen()

	while True: 
		conn, cliente = tcp.accept()

		print(f'Client connected {cliente}')

		mac, name = json.loads(conn.recv(1024).decode('utf-8'))
		conns.init_conn(mac, name, conn)

		if mac == 0:
			t = threading.Thread(target=adm_connection, args=(conns, mac))
		else:
			t = threading.Thread(target=standby, args=(conns, mac))

		t.setName(name)
		t.daemon = True
		t.start()

if __name__ == '__main__':
	main()