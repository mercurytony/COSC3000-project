import json

with open('planets data.json', 'r') as f:
    data = json.load(f)

print(data["Mercury"]["mass_1024kg"])
