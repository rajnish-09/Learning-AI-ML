# Load JSON and print each city and population

import json

with open('cities.json', 'r') as f:
    # reading data from json
    data = json.load(f)
    print(data)


    # writing data to json
with open('cities.json', 'w') as f:
    d = {
        "Dang": 100000,
        "Jhapa": 150000
    }
    json.dump(d,f, indent=4, sort_keys=True)



