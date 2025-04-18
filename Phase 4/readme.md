# Advanced GUI Chat Application

## Overview
This project implements a full-featured GUI chat application with a client-server architecture, featuring private messaging, user authentication, and real-time communication with a clean interface.

## Key Features

### Client Application
- Modern GUI: Built with Tkinter for cross-platform compatibility
- Persian Language Support: Right-to-left layout and Persian font support
- Message History: Scrollable chat window with timestamps
- Special Commands:
  - /exit - Graceful disconnection
- Responsive Design: Clean layout with message entry and send button

### Server Application
- Multi-client Support: Handles multiple simultaneous connections
- User Management: Tracks usernames and connections
- Message Routing:
  - Public broadcasts to all users
  - Private messages between specific users
- Connection Logging: Tracks user join/leave events

## Prerequisites
- Python 3.x
- Tkinter (usually included with Python)

## Installation & Usage

### Starting the Server
python Server.py

### Starting a Client
python Client_gui.py

### Default Configuration
- Host: 127.0.0.1 (localhost)
- Port: 8080

## Technical Architecture

### Client Components
1. GUI Framework:
   - Main application window
   - Message display area (read-only)
   - Message input field
   - Send/Exit buttons

2. Network Layer:
   - Dedicated thread for message receiving
   - Socket connection management
   - Automatic reconnection handling

### Server Components
1. Connection Manager:
   - Thread-per-client model
   - Username registration
   - Connection tracking

2. Message Router:
   - Public message broadcasting
   - Private message delivery
   - System notifications

## User Flow
1. Client launches and prompts for username
2. Server registers new user
3. Users can:
   - Send public messages (visible to all)
   - Send private messages using /pm [user] [message]
   - Exit cleanly with /exit command
4. Server manages disconnections and notifies other users

## Special Features
- Timestamped Messages: All messages include send time
- User Join/Leave Notifications: Automatic system messages
- Clean Disconnection: Proper resource cleanup
- Responsive GUI: Smooth user experience with message auto-scrolling

## Security Notes
- Currently uses plaintext communication
- No message encryption
- Usernames are not authenticated
- Recommended for local network use only

## Limitations
- No message history persistence
- No user avatars or profiles
- Limited to text messages only
- No file transfer capability

## Future Enhancements
1. Enhanced Security:
   - SSL/TLS encryption
   - User authentication
2. Rich Media Support:
   - File transfers
   - Image sharing
3. Additional Features:
   - Chat rooms/channels
   - Message history logging
   - User status indicators
4. Improved GUI:
   - Emoji support
   - Message formatting
   - Dark/light theme options

## Screenshots
*Client Interface*:
[پیام‌رسان - username]
-------------------------
[10:30:15] admin: Welcome!
[10:30:20] user2: Hello everyone!
[10:30:25] [PM] user3: Private message
-------------------------
[Message input field] [Send]
[Exit]

## Troubleshooting
- Connection issues: Verify server is running first
- GUI freezing: Ensure Python and Tkinter are properly installed
- Encoding problems: Confirm system supports UTF-8 encoding

## License
Open-source project, free for educational and personal use.

## Maintenance
To modify the application:
1. Edit Client_gui.py for interface changes
2. Edit Server.py for protocol/backend changes
3. Both files must maintain compatible message formats