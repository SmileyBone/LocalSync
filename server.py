from socket import *

class server(object):
    port = 45000
    def __init__(self):
        self.serv = socket(AF_INET, SOCK_STREAM)
        self.serv.bind(('', 0))
        self.soc = None
        self.connect()

    def broadcast(self):
        print "sending " , str(self.serv.getsockname()[1])
        u = socket(AF_INET, SOCK_DGRAM)
        u.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        u.sendto(str(self.serv.getsockname()[1]), ('<broadcast>', self.port))

    def connect(self):
        connected = False
        self.serv.settimeout(1)
        self.serv.listen(5)
        while not connected:
            try:
                #self.serv.listen(5)
                self.soc, a = self.serv.accept()
                connected = True
            except Exception as e:
                print "The following exception has occured: ", e
                self.broadcast()
            else:
                print "connection opened to: ", a

    """given a payload send it to the remote"""
    def send(self, payload):
        print "trying to send: ", payload
        sent = self.soc.send(payload)
        return sent

    def close(self):
        self.soc.close()


if __name__ == "__main__":
    import time
    serv = server()
    sent = serv.send("did it work? Is this thing on?")
    time.sleep(1)
    message = serv.soc.recv(1024)
    print message
    serv.soc.close()
