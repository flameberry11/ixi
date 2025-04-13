import socket
import threading

def handle_client(client_socket, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.")
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(message)
            broadcast(message, client_socket)
        except:
            clients.remove(client_socket)
            break
    print(f"[DISCONNECTION] {client_address} disconnected.")
    client_socket.close()

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode())
            except:
                clients.remove(client)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 12345))
server.listen(5)

print("[SERVER STARTED] Waiting for connections...")
clients = []

while True:
    client_socket, client_address = server.accept()
    clients.append(client_socket)
    thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    thread.start()