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

import ssl
import sys
import threading
import time
import timeit
import uuid
from binascii import hexlify
from datetime import datetime
import selectors
from callback_db import DatabaseHandler


# !<--------------------------SOCKET BUFFER SIZE--------------->!


class SocketConnection:
    """
        Setting socket connection to the remote server
        {Mitel, Allcatel, Asterisk etc..}
    """

    def __init__(self, remote_ip: str = "127.0.0.1", remote_port: int = 5060, snd_buffer: int = 4096,
                 rcv_buffer: int = 4096) -> None:
        self.remote_ip = remote_ip
        self.remote_port = remote_port
        self.snd_buffer = snd_buffer
        self.rcv_buffer = rcv_buffer
        self.connection = None

    def connection_to_pbx(self):
        """Return connection
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
            connected_port: int = int(str(self.connection).split()[6].split(')')[0])
            print(f"CONNECT TO MITEL SERVER THROUGH  PORT NO : {connected_port}")

        except Exception as e:
            print("raised exceptions error in connection, Sys exit....")
            print("Exception Error ", e, sep=": ", end='\n')

        finally:
            # sys.exit(0) # Use in case of connection fails.
            return self.connection


class SndRcvToRemotePbx:
    """
        Once the connection made form socket connection then,
        this class will handle send and receiving function of the main program
    """

    def __init__(self, connection) -> None:
        if connection is None:
            sys.exit(1)
        else:
            self.connection = connection

    def snd_rcv(self, rcv_buffer: int = 4096):
        """Socket data stream handler """
        print(self.connection)
        cnt: int = 0
        try:
            while True:
                # This selector will manage the readers TX and Rx availability
                readers, xw, xr = select.select([sys.stdin, self.connection], [], [])
                cnt = cnt + 1
                print(f"Speed count :{cnt}")
                for r in readers:
                    """
                        There are two modes in the r :
                           Reader Write Mode: <socket.socket fd=3, family=AddressFamily.AF_INET, 
                                                type=SocketKind.SOCK_STREAM, proto=6, laddr=('127.0.0.1', 47456), 
                                                raddr=('127.0.0.1', 5060)>
                           Reader Read Mode:
                                            <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>              

                    """
                    if r is self.connection:
                        """Socket will allowed to send data to remote server."""
                        data = self.connection.recv(rcv_buffer)
                        if len(data) > 0:
                            print(data)
                    else:  # <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>
                        x = DatabaseHandler()
                        msg = x.get_callback_ext()
                        self.connection.sendall(str(msg).encode())
                        sys.exit(1)
                        # time.sleep(2)
        except Exception as e:
            print(e)


def main():
    """
    Main setup
    """
    # Global Variables for test connection.
    mitel_ip = '127.0.0.1'
    mitel_port = 5061  # SIP PORT
    mitel_userType = 'phone'
    mitel_transportType = 'UDP'  # Depend on the remote pbx setting
    mitel_group = 3  # depend on the remote server settings
    mitel_context = 'mxone-1.test.com'  # context must match with remote pbx
    conn_to_db = DatabaseHandler();
    conn_to_db.get_callback_ext()
    callback = SocketConnection()
    conn = (callback.connection_to_pbx())
    rx_tx = SndRcvToRemotePbx(conn)
    print(rx_tx.snd_rcv())


if __name__ == '__main__':
    main()
