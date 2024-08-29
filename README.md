# Python Chat Application

This project is a simple chat application built using Python's socket programming. It includes a server and multiple clients that can communicate with each other in real-time.

## Table of Contents
- [Project Overview](#project-overview)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Handling Edge Cases](#handling-edge-cases)
- [Running Scenarios] (#running-scenarios)

## Project Overview

The chat application consists of two main components:
1. **Server**: Manages client connections and broadcasts messages to all connected clients.
2. **Client**: Connects to the server, sends messages, and receives messages from other clients.

### Server Features
- Accepts multiple client connections simultaneously.
- Broadcasts messages from one client to all other connected clients.
- Handles connection errors and disconnections.

### Client Features
- Connects to the server.
- Sends messages with a prefix of the client's name.
- Receives and displays messages from other clients.
- Handles empty messages and allows for connection closure with the `exit` command.


## Running the Application

###
- **Start the Server:**
	Open a terminal and run the server script with:
	`python server.py`

###
- **Start Multiple Clients:**
	Open multiple terminal windows or tabs an at each terminal, run the client script with
	`python client.py <client_name>`
	
	
## Usage

- **Send Messages:** Type your message and press Enter. The message will be sent to the server and broadcast to all connected clients.
- **Receive Messages:** Messages from other clients will be displayed in the terminal.
- **Exit:** Type exit and press Enter to close the connection to the server and terminate the client application

## Handling Edge Cases

- **Empty Messages:** The client will ignore messages that are empty or consist only of whitespace.
- **Connection Errors:** The client will handle connection errors and disconnections gracefully, printing a message if the connection is closed.

## Running Scenarios
- Server Side
![Image Alt Text](./server.png)

- Client Side
![Image Alt Text](./client.png)