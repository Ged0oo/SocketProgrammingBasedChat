import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

clients = []
def broadcast(message, _client):
    for client in clients:
        if client != _client:
            try:
                client.send(message)
            except:
                client.close()
                remove(client)

def remove(client):
    if client in clients:
        clients.remove(client)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if not message: break
            broadcast(message, client)
        except:
            remove(client)
            client.close()
            break

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Server started on {HOST}:{PORT}")

    while True:
        client, addr = server_socket.accept()
        print(f"Connected with {addr}")
        clients.append(client)
        threading.Thread(target=handle_client, args=(client,)).start()

server()