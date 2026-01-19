from pathlib import Path

# Use a path relative to this script so the file is found regardless
# of the current working directory when the script is executed.
file_path = Path(__file__).resolve().parent / 'someText.txt'

if not file_path.exists():
    print('someText.txt not found at', file_path)
else:
    file1 = file_path.open('r', encoding='utf-8')
    fullcontent = file1.read()
    print(fullcontent)
    print("File closed = ", file1.closed)
    file1.close()
    print("File closed = ", file1.closed)

with file_path.open('w', encoding='utf-8') as file:  # write mode w will overwrite the file
    file.writelines('First of all, save the following script in the parent folder,')
    file.write("Hope you are doing well!")
    file.write("\nHope you are doing well!")

line = ['line 1 ', 'line 2', 'line three']
with file_path.open('a', encoding='utf-8') as file:  # append mode a will append to the file
    file.writelines('\nAppending the line tct 12412')
    file.writelines(line)
print(file.closed)  # when used with `with`, file will be automatically closed after block







