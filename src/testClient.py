#now lets test the client
from Client.SimpleClient import SimpleClient
client = SimpleClient(url='http://127.0.0.1',port='5000')
client.getResource({'id':'295dfd64dcae11eea1213e165e550ecf'})
client.getResource({'id':'295dfe9adcae11eea1213e165e550ecf'})