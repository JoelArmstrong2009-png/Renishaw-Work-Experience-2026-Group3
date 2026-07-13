import socket

def start_server(host='0.0.0.0', port=5000):
    """Start a TCP server that listens for incoming strings."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((host, port))
            server_socket.listen(1)
            print(f"Server listening on {host}:{port}...")

            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)  # Receive up to 1024 bytes
                    if not data:
                        break
                    print("Received:", data.decode('utf-8'))
                    conn.sendall(b"Message received")  # Send acknowledgment
    except Exception as e:
        print(f"Server error: {e}")

start_server()