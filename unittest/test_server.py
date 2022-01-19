import socket
import selectors


class SipServer:
    """
        #* In order to check echoing use this command with the terminal *#
        Testing Command: nc localhost [port]

        Test server will respond with followings;

        Test methods (1):

            responseType == 'SIP/2.0 200 OK'

        """
    def __init__(self) -> None:
        self.host = "127.0.0.1"
        self.port = 5060
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
