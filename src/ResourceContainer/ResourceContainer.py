from abc import *
class ResourceContainer(ABC):
    
    @abstractmethod
    def addResource(self,resource):
        pass
    
    @abstractmethod
    def removeResource(self,resource):
        pass
    
    @abstractmethod
    def clearAll(self):
        pass
    
    @abstractmethod
    def isResourcePresent(self,reqId):
        pass
    
    @abstractmethod
    def getAllHosterResource(self):
        pass
