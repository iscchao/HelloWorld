import socket

sock = socket.socket()
sock.bind(('127.0.0.1', 8080))
sock.listen(5)
conn, addr = sock.accept()
conn.send(b'HTTP/1.1 200 ok\r\n\r\n')
while 1:
    data = conn.recv(1024)
    print("data:", data.decode('utf-8'))
    conn.send(b"hello")
    conn.close()
