from ResourceContainer.ResourceDictContainer import ResourceDictContainer
from Resource.DirResource import DirResource
print('hello world')
temp = ResourceDictContainer()
temp.addResource(DirResource('./Resource'))
print(temp.getAllResource()) #okey so till now code feels like working.