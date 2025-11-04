#  HTTP Server: Building from the TCP/IP Foundation

This project is a **minimalist, educational HTTP server** built directly on Python's native `socket` library.

The primary goal is to gain a deep, practical understanding of fundamental computer networking concepts, specifically how the **Application Layer (HTTP)** interacts with the **Transport Layer (TCP)**, without relying on high-level frameworks like Flask or Django.

---

##  Educational Focus and Key Concepts

This project serves as a hands-on exercise to master the following core concepts:

* **TCP Socket Programming:** Implementation of the standard **Client-Server communication model** using `socket.socket(socket.AF_INET, socket.SOCK_STREAM)`.
    * Demonstrates the workflow: `bind()` -> `listen()` -> `accept()`.
* **Request/Response Cycle:** Manually handling the complete HTTP/1.1 transaction flow:
    1.  Receiving and parsing the raw byte stream from the client (`client_socket.recv()`).
    2.  Extracting the **HTTP Method** and **Request Path**.
    3.  Manually constructing a compliant HTTP Response (Status Line, Headers, and Body).
    4.  Transmitting the response using `client_socket.sendall()`.
* **Protocol Compliance:** Understanding and adhering to the necessary formatting for an HTTP response, including the use of **`\r\n`** line endings and the critical role of the **`Content-Length`** header.

---

##  Getting Started

### Prerequisites

* **Python 3.x**
* Ensure an `index.html` file exists in the root directory for the server to serve.

### Running the Server

1.  Clone this repository or navigate to the project directory.
2.  Start the server from your terminal:
    ```bash
    python main.py
    ```
3.  Access the server in your browser:
    ```
    http://localhost:8080
    ```

---

##  Future Learning/Improvements

* Implement basic multi-threading or non-blocking I/O to handle multiple concurrent client connections.
* Add logic to serve common static file types (e.g., `.css`, `.js`, `.png`) based on the requested file path.
* Introduce robust error handling for broken pipes and malformed requests.
