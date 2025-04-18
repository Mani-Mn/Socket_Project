# Socket Communication Project

## Overview
This project demonstrates a simple client-server communication system using Python sockets. It allows for bidirectional messaging between a server and one client over a local network.

## Features
- Basic Socket Communication: Establishes TCP connection between client and server
- Interactive Messaging: Allows real-time message exchange
- Local Host Operation: Runs on 127.0.0.1 (localhost) by default
- Simple Exit Mechanism: Type 'exit' to terminate the connection

## Prerequisites
- Python 3.x

## Installation
No additional installation required beyond Python standard libraries.

## Usage

### Running the Server
python Socket_Project.py server

### Running the Client
python Socket_Project.py client

### Default Configuration
- Host: 127.0.0.1 (localhost)
- Port: 8080

## How It Works
1. The server starts listening on the specified port
2. Client connects to the server
3. Either party can send messages which will be displayed on the other end
4. Type 'exit' to terminate the connection

## Code Structure
- run_server(): Handles server-side socket operations
- run_client(): Handles client-side socket operations
- Main block processes command line arguments to determine mode (server/client)

## Limitations
- Currently supports only one client at a time
- No authentication or encryption
- Basic error handling

## Future Improvements
- Multi-client support using threading
- GUI interface
- Message encryption
- Persistent chat history

## License
This project is open-source and available for free use.