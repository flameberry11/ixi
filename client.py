import socket
import threading

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except:
            print("[ERROR] Lost connection to the server.")
            client.close()
            break

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = input("Enter server IP address: ")
username = input("Enter your username: ")

try:
    client.connect((server_ip, 12345))
    print("[CONNECTED] Connected to the chat server.")
    client.send(f"[{username}] has joined the chat.".encode())
except:
    print("[ERROR] Unable to connect to the server.")
    exit()

thread = threading.Thread(target=receive_messages)
thread.start()

while True:
    message = input()
    if message.lower() == "/quit":
        client.send(f"[{username}] has left the chat.".encode())
        client.close()
        break
    client.send(f"[{username}] {message}".encode())