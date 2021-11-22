import json

# opens and prints json file, with indentation
with open('json_pro_test.json', 'r') as test:
    print(json.dumps(json.load(test), indent=4))



