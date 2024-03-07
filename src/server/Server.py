from abc import *
class Server(ABC):
    @abstractmethod
    def startServer(self):
        pass
    @abstractmethod
    def stopServer(self):
        pass
    @abstractmethod
    def setResourceContainer(self):
        pass