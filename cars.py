def car_info(manufacturer,model,**car):
    car["manufacturer_name"] = manufacturer
    car["model_name"]= model
    return car
subaru=car_info("subaru", "outback", color="blue", tow_package=True)
print(subaru)