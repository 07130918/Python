import json

j = {
    "employee":
        [
            {"id": 111, "name": "Mike"},
            {"id": 222, "name": "Kota"}
        ]
}

print(j["employee"][0]["id"], j["employee"][0]["name"])
print(j)
print(json.dumps(j))
print('')


with open('test.json', 'w') as f:
    json.dump(j, f)

with open('test.json', 'r') as f:
    print(json.load(f))
