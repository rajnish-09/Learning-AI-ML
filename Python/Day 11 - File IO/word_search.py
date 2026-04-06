# Search python word in sample file (in which row)

data = True
line = 1

with open('sample', 'r') as f:
    while (data):
        data = f.readline()
        if ('python' in data):
            print(f"Word fount at line {line}")

        line += 1
        
