import time
import os
from Server.SingletonServer import SingletonServer
from threading import Thread
from ResourceContainer.ResourceDictContainer import ResourceDictContainer
from Resource.FileResource import FileResource
from Resource.DirResource import DirResource

def runServer():
    server = SingletonServer.getServer(rc)
    server.startServer()

rc = ResourceDictContainer()
t = Thread(target=runServer)
t.start()
time.sleep(2)
#all my code will come here
while True:
    print('file sharing service is started')
    print('1 -> press 1 to add a resource')
    print('2 -> press 2 to remove a resource')
    print('3 -> press 3 to view all the exisitng shared resources')
    print('4 -> press 4 to exit the program')
    
    userInput = input()
    if userInput == '4':
        break

    if userInput not in ['1','2','3','4']:
        print('wrong userInput')
        continue
    
    if userInput == '3':
        resourceList = rc.getAllResource()
        for id in resourceList:
            print('----')
            print('resource id -> ',id)
            print('resource path -> ',rc.getResource(id).getResourcePath())
            print('----')
        continue
    
    if userInput == '2':
        print('enter resource id to remove (enter "go_back" to return to the menu)')
        innerInput = input()
        if innerInput == 'go_back':
            break
        if rc.isResourcePresent(innerInput):
            rc.removeResource(innerInput)
            print('resource removed')
        else:
            print('entered resource is not present')
        continue
    
    if userInput == '1':
        print('enter the resource Path to add (enter "go_back" to return to the menu)')
        innerInput = input()
        if innerInput == 'go_back':
            break
        #later we may need some error handeling.
        path = os.path.abspath(innerInput)
        if os.path.exists(path):
            res = None
            if os.path.isfile(path):
                res = FileResource(path)
            elif os.path.isdir(path):
                res = DirResource(path)
            else:
                print('something unexpected has happened')
            rc.addResource(res)
            print('resource added')
        else:
            print('this path does not exists')
        continue
print('exiting programme')
server = SingletonServer.getServer(rc)
server.stopServer()


