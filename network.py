import sys
from socket import *
import time

"""network handles multiple connections"""
class network(object):
    broadcast_port = 5005

    def __init__(self):
        self.udp_socket = socket(AF_INET, SOCK_DGRAM)
        self.udp_socket.bind('', 0)
        self.udp_socket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

        #maintain a list of connected devices
        self.connections = []

    """send looking for connections """
    def broadcast(self):
        pass


    def connect(self):
        pass


#another xmass test
if __name__ == "__main__":
    """run some tests on a local machine for sending and reciving
    data"""

    netA = network()
    netB = network()
