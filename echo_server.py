import socket
import threading

def handle_client(client_socket, address):
    print(f"Connection established with {address}")
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8').strip()
            
            if not data:
                break
            
            print(f"Received from {address}: {data}")
            if len(data) > 0:
                first_char = data[0]
                rest_of_string = data[1:]
                
                if first_char == 'A':
                    response = ''.join(sorted(rest_of_string))
                elif first_char == 'D':
                    response = ''.join(sorted(rest_of_string, reverse=True))
                elif first_char == 'C':

                    response = rest_of_string.upper()
                else:
                    response = data
            else:
                response = data
            
            client_socket.send(response.encode('utf-8'))
            print(f"Sent to {address}: {response}")
            
        except Exception as e:
            print(f"Error handling client {address}: {e}")
            break

    client_socket.close()
    print(f"Connection with {address} closed")

def start_server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    host = '0.0.0.0' 
    port = 8888
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")
    
    try:
        while True:
            client_socket, address = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
            client_thread.daemon = True
            client_thread.start()
            
    except KeyboardInterrupt:
        print("Server shutting down...")
    finally:
        server_socket.close()
        print("Server closed")

if __name__ == "__main__":
    start_server()