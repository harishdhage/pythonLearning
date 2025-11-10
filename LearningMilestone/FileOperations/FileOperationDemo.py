file1= open('someText.txt','r')
fullcontent = file1.read()
print(fullcontent)
print("File closed = ",file1.closed)
file1.close()
print("File closed = ",file1.closed)

with open('someText.txt','w') as file: #write mode w will overwrite the file
    file.writelines('First of all, save the following script in the parent folder,')
    file.write("Hope you are doing well!")
    file.write("\nHope you are doing well!")

line = ['line 1 ', 'line 2', 'line three']
with open('someText.txt', 'a') as file:  # write mode w will overwrite the file
    file.writelines('\nAppending the line tct 12412')
    file.writelines(line)
print(file.closed) #when used with command, file will automatically closed after block







