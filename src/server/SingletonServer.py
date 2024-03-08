from .BasicServer import BasicServer
class SingletonServer(BasicServer):
    #right now this class is not thread safe in future we need to make it thread safe.
    serverInstance = None
    def __init__(self,resourceContainer):
        super().__init__(resourceContainer)

    @classmethod    
    def getServer(cls,resourceContainer):
        if not cls.serverInstance:
            cls.serverInstance = cls(resourceContainer)
        return cls.serverInstance