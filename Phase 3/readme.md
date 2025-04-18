# Advanced Multi-Client Chat Application

## Overview
This enhanced chat application builds upon basic socket communication by adding user authentication, private messaging, and special commands. It features a robust server-client architecture with timestamped messages and user management.

## Key Features
- User Authentication: Requires username registration upon connection
- Private Messaging: /pm command for direct user-to-user communication
- Special Commands:
  - /exit - Disconnect from chat
  - /list - Show online users
  - /pm [user] [message] - Send private message
- Timestamped Messages: All messages include time of posting
- Connection Management: Tracks users with their connection details

## Prerequisites
- Python 3.x
- No external dependencies required

## Installation & Usage

### Starting the Server
python Socket_Project_3.py server

### Starting a Client
python Socket_Project_3.py client

### Default Configuration
- Host: 127.0.0.1 (localhost)
- Port: 8080

## Technical Architecture

### Server Components
- Client Dictionary: Stores {connection: (username, address)} pairs
- Broadcast Function: Sends messages to all clients except sender
- Private Messaging: Direct message routing between users
- Connection Handler: Manages client lifecycle (join/leave)

### Client Components
- Dual-Thread Design:
  - Main thread handles user input
  - Background thread receives messages
- Command Parser: Processes special commands locally and remotely

## Message Format
[HH:MM:SS] Username: Message content
[Private][HH:MM:SS] Sender: Message content

## Special Features
1. User Join/Leave Notifications: Automatic broadcasts when users connect/disconnect
2. Online User List: Available via /list command
3. Graceful Disconnection: Proper resource cleanup on exit
4. Error Handling: Manages connection drops and invalid inputs

## Security Notes
- Still uses plaintext communication (consider SSL/TLS for production)
- No password authentication (username-only identification)
- Basic input sanitization recommended for production use

## Limitations
- No message history persistence
- No room/channel support
- Limited to single server instance

## Future Enhancements
1. Message Encryption: Implement SSL/TLS for secure communication
2. Persistent Chat History: Log conversations to file/database
3. User Authentication: Add password protection
4. Chat Rooms: Support for multiple channels
5. File Transfer: Ability to share files

## Sample Session Flow
1. Client connects and provides username
2. Server broadcasts join notification
3. User can:
   - Send public messages (broadcast to all)
   - Send private messages (/pm command)
   - Check online users (/list)
   - Disconnect (/exit)
4. Server broadcasts leave notification on exit

## License
Open-source project, free for educational and personal use.

## Troubleshooting
- Connection refused: Ensure server is running before clients connect
- Username conflicts: Server doesn't currently enforce unique usernames
- Message delays: Check network connectivity if messages don't appear promptly