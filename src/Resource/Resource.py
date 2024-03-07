from abc import *
class Resource(ABC):
    
    @abstractmethod
    def getResourceData(self):
        pass

    @abstractmethod
    def getResourceType(self):
        pass
    
    @abstractmethod
    def getResourcePath(self):
        pass

    @abstractmethod
    def getResourceId(self):
        pass