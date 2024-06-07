import socket
import threading

# Configuração do servidor

HOST = '127.0.0.1'  # Localhost
PORT = 12345       # Porta para escutar

# Função para lidar com a conexão do cliente
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Recebido: {message}")
                broadcast(message, client_socket)
            else:
                remove(client_socket)
                break
        except:
            continue

# Função para transmitir mensagens para todos os clientes
def broadcast(message, connection):
    for client in clients:
        if client != connection:
            try:
                client.send(message.encode('utf-8'))
            except:
                remove(client)

# Função para remover um cliente da lista
def remove(connection):
    if connection in clients:
        clients.remove(connection)

# Função principal para iniciar o servidor
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Servidor iniciado em {HOST}:{PORT}")

    while True:
        client_socket, addr = server_socket.accept()
        clients.append(client_socket)
        print(f"Conexão de {addr}")
        
        threading.Thread(target=handle_client, args=(client_socket,)).start()

# Lista para rastrear os clientes conectados
clients = []

if __name__ == "__main__":
    start_server()
