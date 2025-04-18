# Multi-Threaded Socket Chat Application

## Overview
This project implements a multi-client chat server using Python sockets and threading, allowing multiple clients to connect and communicate in real-time.

## Key Features
- Multi-client Support: Handles multiple simultaneous connections
- Real-time Broadcasting: Messages are broadcast to all connected clients
- Threaded Architecture: Uses separate threads for each client connection
- Client-Server Model: Clear separation between server and client components
- Persistent Connections: Maintains connections until client disconnects

## Prerequisites
- Python 3.x

## Installation
No additional dependencies required. Uses Python's built-in socket and threading modules.

## Usage

### Starting the Server
python Socket_Project_2.py server

### Starting a Client
python Socket_Project_2.py client

### Default Configuration
- Host: 127.0.0.1 (localhost)
- Port: 8080

## Architecture

### Server Components
- Main Thread: Accepts new client connections
- Client Handler Threads: One per client (manages message receiving/broadcasting)
- Client List: Maintains active connections

### Client Components
- Main Thread: Handles user input and message sending
- Receiver Thread: Listens for incoming messages in background

## How It Works
1. Server starts and listens for connections
2. Clients connect and spawn a handler thread on the server
3. Messages from any client are:
   - Displayed on server console
   - Broadcast to all other clients
4. Connections are maintained until client sends 'exit' or disconnects

## Message Flow
Client A → Server → Broadcast to Clients B,C,D...

## Error Handling
- Automatic client disconnection handling
- Thread-safe client list management
- Graceful socket closure

## Limitations
- No authentication or user identification
- Basic message formatting
- No private messaging between clients
- No message history persistence

## Future Enhancements
- User authentication system
- Private/direct messaging
- Message persistence
- Room/channel support
- Improved error handling and reconnection logic

## Security Note
This is a development prototype. For production use:
- Add encryption (SSL/TLS)
- Implement proper authentication
- Add input validation

## License
Open-source, free to use and modify.