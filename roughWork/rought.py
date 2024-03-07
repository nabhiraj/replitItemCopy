import os

#this is just the rough code right now
def checkPathExist(path):
  return os.path.exists(path)


print('enter the path')
userPath = input()
absolutePath = os.path.abspath(userPath)
print('path ', absolutePath, checkPathExist(absolutePath))
#now we need to start a python flask server.
if os.path.exists(absolutePath):
  if os.path.isfile(absolutePath):
    print("It's a file.")
  elif os.path.isdir(absolutePath):
    print("It's a directory.")