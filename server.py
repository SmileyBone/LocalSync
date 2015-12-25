from socket import *
import threading
import thread_template
from collections import deque
import time

class network(thread_template.manager):
    def add_connection(self, soc):
        t = threading.Thread(target=connection(soc, self.killEvent, self.msg_queue))
        self.threads.append(t)
        t.start()

    def run(self):
        self.msg_queue = deque()
        #start the server / broadcaster
        t = threading.Thread(target=server(self.killEvent, self.queue))
        self.threads.append(t)
        t.start()

        lastTime = time.time()
        while not self.killEvent.isSet():
            if time.time() - lastTime > 1:
                lastTime = time.time()
                print threading.active_count(), "threads at time ", time.time()
            try:
                if len(self.queue) > 0:
                    ncon = self.queue.pop()
                    print "adding connection", ncon.getsockname()
                    self.add_connection(ncon)

                if len(self.msg_queue) > 0:
                    msg = self.msg_queue.pop()
                    print msg
            except KeyboardInterrupt:
                self.killEvent.set()

class connection(thread_template.worker):
    def __init__(self, soc, killEvent, queue):
        self.soc = soc
        self.killEvent = killEvent
        self.queue = queue

    def __call__(self):
        time.sleep(3)
        while not self.killEvent.isSet():
            try:
                data = self.soc.recv(1024)
                self.queue.append(data)
            except KeyboardInterrupt:
                self.killEvent.set()
                self.soc.close()
            except Exception:
                if e is None:
                    print "huh"
                    
#this is a test for xmass checkin
class server(thread_template.worker):
    port = 45000
    def __init__(self, killEvent, queue):
        self.killEvent = killEvent
        self.queue = queue

    def __call__(self):
        while not self.killEvent.isSet():
            try:
                serv = socket(AF_INET, SOCK_STREAM)
                print "binding new socket"
                serv.bind(('', 0))
                print "New socket at ", serv.getsockname()
                serv.settimeout(5) #set the server timeout to 1 second
                serv.listen(1)     #allow up to five pending connections
                self.broadcast(serv)
                soc, a = serv.accept()
                self.queue.append(soc)
            except Exception as e:
                if e is KeyboardInterrupt:
                    self.killEvent.set()
                else:
                    print e
            finally:
                serv.close()

    def broadcast(self, serv):
        print "boop"
        u = socket(AF_INET, SOCK_DGRAM)
        u.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        u.sendto(str(serv.getsockname()[1]), ('<broadcast>', self.port))



if __name__ == "__main__":
    net = network()
    net.run()
