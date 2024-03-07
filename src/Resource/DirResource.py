from .Resource import Resource
import uuid
import os
import base64
import shutil

class DirResource(Resource):
    def __init__(self,resourcePath):
        if self.verifyDirPath(resourcePath):
            self.resourcePath = os.path.abspath(resourcePath)
            self.resourceId = uuid.uuid1().hex
            self.resourceType = 'dir'
        else:
            raise ValueError('parameter verification failed, cannot create resource')

    def verifyDirPath(self,path):
        path = os.path.abspath(path)
        if os.path.exists(path) and os.path.isdir(path):
            return True
        else:
            return False

    def getResourceData(self):
        zipFilePath = 'archive_shutil_'+uuid.uuid1().hex
        zipFilePath = os.path.abspath(zipFilePath)
        shutil.make_archive(zipFilePath, format='zip', root_dir=self.resourcePath)
        zipFilePath+='.zip'
        with open(zipFilePath,'rb') as f:
            fileData = f.read()
            encodedData = base64.b64encode(fileData).decode('utf-8')
            os.remove(zipFilePath)
            return encodedData
        os.remove(zipFilePath)
        return 'error in reading file data'

    def getResourceType(self):
        return self.resourceType

    def getResourcePath(self):
        return self.resourcePath

    def getResourceId(self):
        return self.resourceId
