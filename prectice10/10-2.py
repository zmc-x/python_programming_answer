with open('file\learning_python.txt') as file_object:
    file=file_object.read()
File=file.replace('python','c')
print(File)