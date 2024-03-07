from ResourceContainer.ResourceDictContainer import ResourceDictContainer
from Resource.DirResource import DirResource
from Resource.FileResource import FileResource
from Server.BasicServer import BasicServer
temp = ResourceDictContainer()
temp.addResource(DirResource('./Resource'))
temp.addResource(FileResource('./joker.txt'))
print(temp.getAllResource())
s = BasicServer(temp)
s.startServer()