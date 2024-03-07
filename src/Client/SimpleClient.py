from .Client import Client
import json
import os
import requests
import base64
import uuid
import shutil

class SimpleClient(Client):

    def __init__(self,url=None,port=None):
        self.jsonFile = 'savedConnectionInfo.json'
        self.jsonFile = os.path.abspath(self.jsonFile)
        if  url and port:
            self.setUpServerConnectionInfo(url,port)
            return
        elif os.path.exists(self.jsonFile):
            with open(self.jsonFile,'r') as f:
                temp = json.load(f)
                if temp['url'] and temp['port']:
                    self.setUpServerConnectionInfo(temp['url'],temp['port'])
                    return
        raise ValueError('connection setup information not available')
        
    def setUpServerConnectionInfo(self,url,port):
        self.url = url
        self.port = port
        self.link = self.url+':'+str(port)
        temp = {}
        temp['url'] = url
        temp['port'] = port
        with open(self.jsonFile,'w') as f:
            json.dump(temp,f)
        return True
    
    def getResource(self,req):
        if 'id' in req:
            res = requests.get(self.link+'?id='+req['id'])
            print(res.content)
            if res.status_code == 200 and res.content: 
                temp = res.json()
                print(temp)
                if temp['type'] == 'file':
                    self.storeFile(temp,temp['path'])
                    return
                elif temp['type'] == 'dir':
                    self.storeDir(temp,temp['path'])
                    return
        raise ValueError('request object is in wrong format')

    def storeFile(self,fileRes,srcPath):
        fileName = os.path.basename(srcPath)
        data = fileRes['data']
        decoded_data = base64.b64decode(data)
        with open(fileName,'wb') as f:
            f.write(decoded_data)
        return True
    
    def storeDir(self,dirRes,srcPath):
        dirName = os.path.basename(srcPath)
        zipFileName = 'dir_n_'+uuid.uuid1().hex+'.zip'
        self.storeFile(dirRes,zipFileName)
        shutil.unpack_archive(zipFileName,dirName)
        os.remove(zipFileName) 