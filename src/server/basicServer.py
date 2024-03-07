from .Server import Server
from flask import Flask, request, jsonify

class BasicServer(Server):

    def __init__(self,resourceContainer):
        self.resourceContainer = resourceContainer
        self.app = Flask(__name__)
        self.setup_routes()
        self.serverState = 'stoped'

    def setup_routes(self):
        @self.app.route('/')
        def getResource():
            resourceId = request.args.get('id', None)
            print('the resource id is ',resourceId)
            if resourceId and self.resourceContainer.isResourcePresent(resourceId):
                resource = self.resourceContainer.getResource(resourceId)
                response = {
                    "type" : resource.getResourceType(),
                    "path" : resource.getResourcePath(),
                    "id" : resource.getResourceId(),
                    "data": resource.getResourceData(),
                }
                return response
            return ''
        
    def startServer(self):
        #this should be done in a new thread
        self.app.run()
        self.serverState = 'running'

    def stopServer(self):
        self.serverState = 'stopped'
        shutdown_func = request.environ.get('werkzeug.server.shutdown')
        if shutdown_func is None:
            raise RuntimeError('Not running with the Werkzeug Server')
        shutdown_func()
        return True

    
    def setResourceContainer(self,resourceContainer):
        self.resourceContainer = resourceContainer