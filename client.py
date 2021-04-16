import socket

HEADER = 64
PORT = 5050
SERVER = '192.168.0.74'     # Change for the IP of the server
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
msg_length = int(client.recv(HEADER).decode(FORMAT).strip(' '))
msg = client.recv(msg_length).decode(FORMAT)
print(f"[SERVER] : {msg}")

def send(msg):
    # Send message
    message = msg.encode(FORMAT)                        # Encode the message in utf-8
    msg_length = len(message)                           # Get the length of the message
    send_length = str(msg_length).encode(FORMAT)        
    send_length += b' ' * (HEADER - len(send_length))   # Add the necessary bytes to get to the HEADER length
    client.send(send_length)
    client.send(message)
    
    # Receive confirmation
    msg_length = len(client.recv(HEADER).decode(FORMAT))
    msg = client.recv(msg_length).decode(FORMAT)
    print(f"[SERVER] : {msg}")

while True:
    msg = input()
    if msg == 'close':
        send(DISCONNECT_MESSAGE)
        break
    send(msg)
