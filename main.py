import socket 

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8088


print(f"TCP server is listening on {SERVER_PORT}...")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)


while True:
    client_socket, client_address = server_socket.accept()
    
    # Use a try/except to handle potential UnicodeDecodeError and other socket errors
    try:
        # Use a smaller buffer size like 1024 for the first read to ensure you get the headers
        request = client_socket.recv(1024).decode('utf-8')
    except UnicodeDecodeError:
        # Handle binary or non-UTF-8 data gracefully
        client_socket.close()
        continue # Skip to the next loop iteration

    # If the request is empty (client closed connection before sending data), skip it
    if not request:
        client_socket.close()
        continue
        
    print(request)
    
    headers = request.split('\n')
    
    # Safely get the first line and its components
    try:
        first_header_components = headers[0].split()
        http_method = first_header_components[0]
        path = first_header_components[1]
    except IndexError:
        # Malformed request, close and continue
        client_socket.close()
        continue

    # --- FIX 1: Corrected File Opening ---
    if path == '/':
        try:
            # FIX: Use open() correctly, not fin = open=
            with open('index.html', 'r') as fin:
                 content = fin.read()
            
            # Use \r\n for HTTP line endings
            response = 'HTTP/1.1 200 OK\r\n'
            response += 'Content-Type: text/html\r\n'
            response += f'Content-Length: {len(content.encode("utf-8"))}\r\n' # Add Content-Length
            response += '\r\n' # Blank line separates headers from body
            response += content
            
            # Send the complete response (encoded as bytes)
            client_socket.sendall(response.encode('utf-8'))
            
        except FileNotFoundError:
            # Handle case where index.html is missing
            error_response = 'HTTP/1.1 404 NOT FOUND\r\n\r\n<h1>404 File Not Found</h1>'
            client_socket.sendall(error_response.encode('utf-8'))
            
        finally:
             client_socket.close()
             
    # --- FIX 2: Added Missing Response for Other Paths ---
    else:
        # Serve 404 for any path that isn't '/'
        error_response = 'HTTP/1.1 404 NOT FOUND\r\n\r\n<h1>404 Not Found</h1>'
        client_socket.sendall(error_response.encode('utf-8'))
        client_socket.close()
        