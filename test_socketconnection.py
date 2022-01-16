

import asyncio
import hashlib
import io
import logging
import os
import random
import re
import select
import socket
import socketserver
import sqlite3
import ssl
import sys
import threading
import time
import timeit
import uuid
from binascii import hexlify
from datetime import datetime

#!<--------------------------SOCKET BUFFER SIZE--------------->!
SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096
#!<--------------------------END------------------>!
# REMOTE_EXT = 12000 # Variable
REMOTE_IP_MITEL = '127.0.0.1'
REMOTE_PORT_MITEL = 5061  # SIP PORT
USER = 'phone'
TRANSPORT = 'UDP'  # Depend on the remote pbx setting
MITEL_TGROUP = 3  # depend on the remote server settings
MITEL_CONTEXT = 'mxone-1.test.com'  # context must match with remote pbx


class SOCKETCONNECTION():
    def __init__(self, REMOTE_IP_MITEL, REMOTE_PORT_MITEL) -> None:

        self.REMOTE_IP_MITEL = REMOTE_IP_MITEL
        self.REMOTE_PORT_MITEL = REMOTE_PORT_MITEL

    async def connectPBX():
        connection = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        connection.settimeout(180)
        connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        connection.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
        connection.setsockopt(
            socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_BUF_SIZE)
        connection.setsockopt(
            socket.SOL_SOCKET, socket.SO_RCVBUF, RECV_BUF_SIZE)
        try:

            connection.connect((REMOTE_IP_MITEL, REMOTE_PORT_MITEL))
            CONANYTED_PORT = int(str(connection).split()[6].split(')')[0])
            print(f"CONNECT TO MITEL SERVER THROUGH  PORT NO : {CONANYTED_PORT}")

        except Exception as e:
            print(e, end='\n')

        while True:
            # This selector will manage the readers TX and Rx availability
            readers, xw, xr = select.select([sys.stdin, connection], [], [])

            for r in readers:   # While connection mode -> Selector will allow send data to Server

                if r is connection:
                    """
                    RCV_HANDLER(RECEIVED DATA)
                    Function Name   : RCV_HANDLER
                    args            : Receving data from Mitel Server
                    Buffer Size     : SEND_BUF_SIZE
                    Parsing Data    : data (Byte Mode)
                    return          : NO
                    Parsing function to Asynic mode in order to operate the main function in mode of damean 
                    """
                    data = connection.recv(SEND_BUF_SIZE)
                    if len(data) > 0:
                        print(data)
                else:
                    msg = "Hello wolrd".encode()
                    connection.sendall(msg)
                    time.sleep(2)


if __name__ == '__main__':
    SOCKETCONNECTION()
