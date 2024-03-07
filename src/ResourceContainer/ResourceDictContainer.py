from .ResourceContainer import ResourceContainer

class ResourceDictContainer(ResourceContainer):
    
    def __init__(self):
        self.resourcePathMap = {}

    def addResource(self,resource):
        self.resourcePathMap[resource.resourceId] = resource
        return True
    
    def removeResource(self,resourceId):
        del self.resourcePathMap[resourceId]
        return True
    

    def clearAll(self):
        self.resourcePathMap = {}
        return True
    
    def isResourcePresent(self,reqId):
        if reqId in self.resourcePathMap:
            return True
        else:
            return False

    def getResource(self,resourceId):
        return self.resourcePathMap[resourceId]
    
    def getAllResource(self):
        res = []
        for i in self.resourcePathMap:
            res.append(i)
        return res
    
    def numOfResource(self):
        return len(self.resourcePathMap)
