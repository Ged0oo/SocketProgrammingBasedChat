import socket
import threading
import sys

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
            else:
                break
        except Exception as e:
            print("\nConnection closed.")
            break

def start_client(client_name):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))
    
    print("\nConnected successfully to server.\n")
    
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()
    
    while True:
        message = input()        
        if not message.strip():
            continue
        
        if message.lower() == 'exit':
            client_socket.close()
            break
        
        full_message = f"{client_name}: {message}"
        client_socket.send(full_message.encode('utf-8'))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python client.py <client_name>")
        sys.exit(1)
    
    client_name = sys.argv[1]
    start_client(client_name)