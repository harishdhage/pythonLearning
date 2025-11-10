
try:
    file = open('example.txt','r')
    content = file.read()
    a=b
except FileNotFoundError as fe:
    print(fe)
except Exception as e:
    print(e)
finally:
    if file in locals() or not file.closed:
        file.close()
        print('file is closed')