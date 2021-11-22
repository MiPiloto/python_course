import json

theForce = {
    'luke':['jedi', 'yoda', 'green saber'],
    'anakin':['sith', 'darth sidious', 'red saber'],
    'ahsoka':['jedi','anakin','blue saber'],}

# append a new dictionary to the json file
# open json file and load to a variable
with open('json_pro_test.json', 'r') as test:
    test_open = json.load(test)

# append dictionary to the variable
test_open.update(theForce)

# rewrite the json file using the new variable created
with open('json_pro_test.json', 'w') as test:
    json.dump(test_open, test, indent=4)