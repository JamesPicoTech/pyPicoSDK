import parser
import socket 
import sys

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    args = sys.argv[1:]
    parser.parser.parse_args(args)
    s.sendall(' '.join(args).encode())
    print(s.recv(1024).decode())
