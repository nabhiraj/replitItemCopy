from abc import *
class ResourceContainer(ABC):
    
    @abstractmethod
    def addResource(self,resource):
        pass
    
    @abstractmethod
    def removeResource(self,resourceId):
        pass
    
    @abstractmethod
    def clearAll(self):
        pass
    
    @abstractmethod
    def isResourcePresent(self,reqId):
        pass

    @abstractmethod
    def getResource(self,resourceId):
        pass
    
    @abstractmethod
    def getAllResource(self):
        pass
