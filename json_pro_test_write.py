import json

heroes_dict = {
    'bruce':['batman','batcave','batarang'],
    'clark':['superman','krypton','x-ray vision'],
    'peter':['spider-man','rooftops','spider-web'],
    'eddie':['venom','space','devour'],}

with open("json_pro_test.json", 'w') as test:
    json.dump(heroes_dict, test, indent=4)