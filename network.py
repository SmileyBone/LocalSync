import sys
import socked
import time

"""network handles multiple connections"""
class network(object):
    def __init__(self):
        pass

    """send looking for connections """
    def broadcast(self):
        pass
        
    def connect(self):
        pass


"""the network class handles one connection only"""
class _connection(object):
    def __init__(self, connection):
        pass

    """given a payload send it to the remote"""
    def send(self, payload):
        pass

    def receive(self):
        pass
