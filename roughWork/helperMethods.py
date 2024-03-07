import os
import base64
def getFileData(path):
    path = os.path.abspath(path)
    fileData = None
    with open(path,'rb') as f:
        fileData = f.read()
    encoded_file_contents = base64.b64encode(fileData).decode('utf-8')
    return encoded_file_contents

def getDataFromPath(path):
    path = os.path.abspath(path)
    if os.path.exists(path):
        if os.path.isfile(path):
            data = getFileData(path)
            return (True,False,os.path.basename(path),data)
        elif os.path.isdir(path):
            #now lets learn how to zip the folder and all
            return (False,False,False,False)
    else:
        return (False,False,False,False)

