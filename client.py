import socket

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    # Send message
    message = msg.encode(FORMAT)                        # Encode the message in utf-8
    msg_length = len(message)                           # Get the length of the message
    send_length = str(msg_length).encode(FORMAT)        
    send_length += b' ' * (HEADER - len(send_length))   # Add the necessary bytes to get to the HEADER length
    client.send(send_length)
    client.send(message)
    
    # Receive confirmation
    msg_length = len(conn.recv(HEADER).decode(FORMAT))
    msg = conn.recv(msg_length).decode(FORMAT)


send('Hello world!')
input()
send(DISCONNECT_MESSAGE)