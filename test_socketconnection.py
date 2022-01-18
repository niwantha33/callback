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

# !<--------------------------SOCKET BUFFER SIZE--------------->!

sendBuffer = 4096
rcvBuffer = 4096
# !<--------------------------END------------------>!
# Global Variables for test connection.
mitel_ip = '127.0.0.1'
mitel_port = 5061  # SIP PORT
mitel_userType = 'phone'
mitel_transportType = 'UDP'  # Depend on the remote pbx setting
mitel_group = 3  # depend on the remote server settings
mitel_context = 'mxone-1.test.com'  # context must match with remote pbx


class SocketConnection:
    """
        Setting socket connection to the remote server
        {Mitel, Alcotel, Asterisk etc..}
    """
    def __init__(self, remote_ip: str = "127.0.0.1", remote_port: int = 5060, snd_buffer: int = 4096,
                 rcv_buffer: int = 4096) -> None:
        self.remote_ip = remote_ip
        self.remote_port = remote_port
        self.snd_buffer = snd_buffer
        self.rcv_buffer = rcv_buffer
        self.connection = None

    def connection_to_pbx(self):
        """
            This will create the connection to remote server using the params.@parms
            @param
                ip, port, snd and rcv buffer
            @return
                connection (in order to pass the connection to send rcv function )
        """
        self.connection = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        self.connection.settimeout(180)
        self.connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.connection.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
        self.connection.setsockopt(
            socket.SOL_SOCKET, socket.SO_SNDBUF, self.snd_buffer)
        self.connection.setsockopt(
            socket.SOL_SOCKET, socket.SO_RCVBUF, self.rcv_buffer)
        try:

            self.connection.connect((self.remote_ip, self.remote_port))
            connected_port: str = None
            connected_port = int(str(self.connection).split()[6].split(')')[0])
            print(f"CONNECT TO MITEL SERVER THROUGH  PORT NO : {connected_port}")


        except Exception as e:
            print("Exception Error ", e, sep=": ", end='\n')

        return self.connection

    # while True:
    #     # This selector will manage the readers TX and Rx availability
    #     readers, xw, xr = select.select([sys.stdin, connection], [], [])
    #
    #     for r in readers:  # While connection mode -> Selector will allow send data to Server
    #
    #         if r is connection:
    #             """
    #             RCV_HANDLER(RECEIVED DATA)
    #             Function Name   : RCV_HANDLER
    #             args            : Receving data from Mitel Server
    #             Buffer Size     : SEND_BUF_SIZE
    #             Parsing Data    : data (Byte Mode)
    #             return          : NO
    #             Parsing function to Asynic mode in order to operate the main function in mode of damean
    #             """
    #             data = connection.recv(SEND_BUF_SIZE)
    #             if len(data) > 0:
    #                 print(data)
    #         else:
    #             msg = "Hello wolrd".encode()
    #             connection.sendall(msg)
    #             time.sleep(2)


def main():
    callback = SocketConnection()
    print(callback.connection_to_pbx())


if __name__ == '__main__':
    main()
