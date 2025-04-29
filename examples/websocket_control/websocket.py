import socket
import parser

# Setup socket IP
HOST = "127.0.0.1"
PORT = 65432

# Output data to client and print terminal
def output(conn, string):
    print(string)
    conn.send(string.encode())

# Parse args and execute a command
def parse_args(conn, data):
    # Parse through argparser
    args = parser.parser.parse_args(data)
    command = args.command

    if command == 'close':
        return 1
    elif command == 'channel':
        output(conn, f'Setting channel {args.channel} to range {args.range}')
    elif command == 'trigger':
        output(conn, f'Setting trigger to {args.threshold}mV on channel {args.channel}')
    elif command == 'run':
        output(conn, f'Running block capture with {args.samples} at timebase {args.timebase}, Saving to {args.filename}')
    elif command == 'siggen':
        output(conn, f'Setting SigGen to {args.waveform} at {args.frequency}Hz and {args.amplitude}V')

# PicoScope Functions
def setup_picoscope():
    print('Setting up PicoScope...', end='')
    print('Done!')


# Open the socket and parse command
def run_socket():
    print('Opening socket...')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    if parse_args(conn, data.decode().split(' ')):
                        return


if __name__ == '__main__':
    setup_picoscope()
    run_socket()
    print('exiting...')