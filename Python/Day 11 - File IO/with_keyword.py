# with keyword is used for resource management in fillle I/O operations, ensuring filels are automcatically closed after code block executes

with open('sample', 'r') as f:
    print(f.read())