def build_car(name,model,**extras):
    car = {}
    car['name'] = name
    car['model'] = model
    for key,value in extras.items():
        car[key]=value 
    return car # tenha certeza que o return está for do laço for