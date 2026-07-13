import socket

def send_message(server_ip, port=5000, message="Hello from client!"):
    """Send a string message to the server."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((server_ip, port))
            client_socket.sendall(message.encode('utf-8'))
            response = client_socket.recv(1024)
            print("Server replied:", response.decode('utf-8'))
    except Exception as e:
        print(f"Client error: {e}")


send_message("192.168.1.10", message="Hello, Server!")