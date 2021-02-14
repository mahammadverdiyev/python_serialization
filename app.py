with open('test.txt', 'rb') as fileObject:
    fileContent = fileObject.read()
    print(fileContent)
    print(type(fileContent))

fileContent = bytearray(fileContent)
fileContent[0] = 74
print(fileContent)

with open('test_new.txt', 'wb') as fileObject:
    fileObject.write(fileContent)