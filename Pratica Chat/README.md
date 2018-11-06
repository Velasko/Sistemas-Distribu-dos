Script para chat fazendo uso de RMI

Linguagem utilizada: Python 3.7.0

Bibliotecas necessárias:
	- json
	- time
	- socket
	- threading
	- tkinter
	- Pyro4

As bibliotecas Pyro4 e tkinter podem não vir com o python, dependendo do sistema operacional utilizado.

O programa consiste de 4 arquivos:
	- client.py - responsável por descobrir os chats existentes no servidor e conectar o usuário à sala.
	- server.py - responsável por criar um 'servidor dns' para os chats e criar os chats. 
	- user.py - contém a classe 'User' que irá criar a interface gráfica e interagir com a sala de bate-papo por RMI.
	- chat.py - contém a classe 'Chat' que faz o gerenciamento entre os usuários participantes do bate-papo.


Caso não possua python 3.7 ou uma das bibliotecas, no repositório do programa, existem duas pastas: server e client, na qual possuem versões .exe criadas usando pyinstall.
entre na pasta server e execute o arquivo server.exe.
execute então o client de forma análoga para cada usuário que for conectar ao servidor.

Repositório: https://github.com/Velasko/RMI-Chat