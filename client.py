from socket import *

class client(object):
    port = 45000
    def __init__(self):
        self.soc = socket(AF_INET, SOCK_STREAM)
        self.soc.settimeout(5)


    def connect(self):
        #start a UDP listener to get the port information
        u = socket(AF_INET, SOCK_DGRAM)
        u.bind(('', self.port))
        remote_port, (ip, udp_port) = u.recvfrom(1024)

        #now that we have that try to connect at the given port and ip
        print "###############################"
        print ip, remote_port
        address = (ip, int(remote_port))
        print "connecting to:", address
        self.soc.connect(address)

if __name__ == "__main__":
    import time
    c = client()
    c.connect()
    message = c.soc.recv(1024)
    print message
    c.soc.send("Yup, this thing is on.")
    time.sleep(2)
    c.soc.close()
    print "done"
