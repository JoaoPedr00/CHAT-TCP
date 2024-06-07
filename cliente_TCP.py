import socket
import threading

# Configuração do cliente

HOST = '127.0.0.1'  # Localhost
PORT = 12345       # Porta para conectar

# Função para receber mensagens do servidor
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Mensagem: {message}")
            else:
                break
        except:
            break

# Função para enviar mensagens para o servidor
def send_messages(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

# Função principal para iniciar o cliente
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    threading.Thread(target=receive_messages, args=(client_socket,)).start()
    threading.Thread(target=send_messages, args=(client_socket,)).start()

if __name__ == "__main__":
    start_client()
