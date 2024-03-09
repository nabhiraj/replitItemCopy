import sys
from Client.SimpleClient import SimpleClient
if len(sys.argv)<=1:
    print('you need to give resource id as arguments')
resourceId = sys.argv[1]
client = SimpleClient()
client.getResource({'id':resourceId})
print('done')

