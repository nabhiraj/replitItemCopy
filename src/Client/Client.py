from abc import *
class Client(ABC):
    
    @abstractmethod
    def setUpServerConnectionInfo(self,url,port):
        pass
    
    @abstractmethod
    def getResource(self,req):
        pass
    