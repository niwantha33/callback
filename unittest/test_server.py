import socket
import selectors


class SipServer:
    '''
        #* In order to check echoing use this command with the terminal *#
        Testing Command: nc localhost [port]

        Test server will response with followings; 
        
        Test methods (1): 

            responseType == 'SIP/2.0 200 OK'

        """
        {'Via': 'SIP/2.0/UDP [ip]:5060;branch=z9hG4bK-f0e9859ec-9cc5-4a489-8ad3-008768667b561;rport=41886;received=[ip]', 
        'Contact': '<sip:13400@10.30.44.71:5060>', 
        'To': '<sip:134@[ip2];user=phone;transport=UDP;tgrp=1;trunk-context=tel.test.com>;tag=40814c42', 
        'From': '<sip:1501@[ip]>;user=phone;tgrp=1;trunk-context=n1.test.com>;tag=9cc594ra48',
         'Call-ID': 'f0ee99859c11', 
         'CSeq': '494113 SUBSCRIBE', 'Expires': '3600', 'User-Agent': 'Aastra SN', 'Content-Length': '0'}      
        """

    '''
    def __init__(self) -> None:
        self.host = "127.0.0.1"
        self.port = 5061
        self.SEND_BUF_SIZE = 4096
        self.RECV_BUF_SIZE = 4096
        self.sel = selectors.DefaultSelector()
        

    def configServer(self,sock=None) -> int:
        if sock is None:
            sock = socket.socket(socket.AF_INET,
                             socket.SOCK_STREAM, socket.IPPROTO_TCP)
        else:
            sock = sock        
        
        sock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF,
                        self.SEND_BUF_SIZE)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF,
                        self.RECV_BUF_SIZE)
        try:
            sock.bind((self.host, self.port))
        except Exception as e:
            print(f'socket bind error :{e}')

        sock.listen(100)
        return sock

    def accept(self, sock,mask):
        fd, addr = sock.accept()
        print("accepted : ", addr)
        fd.setblocking(False)
        self.sel.register(fd, selectors.EVENT_READ, self.read)

    def read(self, sock,mask):
        sent:int = 0
        data = sock.recv(1000)  # Should be ready
        if data:
            print('echoing', repr(data), 'to', sock)
            sent = sock.send(data)  # Hope it won't block
            if sent == 0:
                raise RuntimeError("socket connection broken")
        else:
            print('closing', sock)
            self.sel.unregister(sock)
            sock.close()

    def eventHandler(self,sock):
        sock.setblocking(False)
        self.sel.register(sock, selectors.EVENT_READ, self.accept)
        while True:
            events = self.sel.select()
            for key, mask in events:
                callback = key.data
                callback(key.fileobj, mask)


sip = SipServer()
con = sip.configServer()
sip.eventHandler(con)
