from Client.SimpleClient import SimpleClient
url = input('enter the url')
if url[-1] == '/':
    url = url[:-1]
port = input('enter the port')
client = SimpleClient(url,port)

