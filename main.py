# Threaded version of the Omegle Bot
import _thread
import time

from BlackList import BlackList
from MITMController import MITMController

blacklist = BlackList()
blacklist.load('blacklist.txt')

controller = MITMController(blacklist=blacklist)
controller.Setup()

_thread.start_new_thread(controller.Run, ())

while True:
    command = input('Enter a command: ')

    print(command)

    if command == 'quit':
        controller.running = False
        break

time.sleep(0.5)

controller.Stop()
