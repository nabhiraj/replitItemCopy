from .Resource import Resource
import uuid
import os
import base64
class FileResource(Resource):

    def __init__(self,resourcePath):
        if self.verifyFilePath(resourcePath):
            self.resourcePath = os.path.abspath(resourcePath)
            self.resourceId = uuid.uuid1().hex
            self.resourceType = 'file'
        else:
            raise ValueError('parameter verification failed, cannot create resource')

    def verifyFilePath(self,path):
        path = os.path.abspath(path)
        if os.path.exists(path) and os.path.isFile(path):
            return True
        else:
            return False

    def getResourceData(self):
        with open(self.resourcePath,'rb') as f:
            fileData = r.read()
            encodedData = base64.b64encode(fileData).decode('utf-8')
            return encodedData
        return 'error in reading file data'

    def getResourceType(self):
        return self.resourceType

    def getResourcePath(self):
        return self.resourcePath

    def getResourceId(self):
        return self.resourceId