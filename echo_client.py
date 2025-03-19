import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = '127.0.0.1'
    port = 8888
    
    try:
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")
        
        while True:
            message = input("Enter a message (or 'exit' to quit): ")
            
            if message.lower() == 'exit':
                break
            
            client_socket.send(message.encode('utf-8'))
            
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Server response: {response}")
            
    except ConnectionRefusedError:
        print("Connection refused. Make sure the server is running.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        print("Connection closed")

if __name__ == "__main__":
    start_client()