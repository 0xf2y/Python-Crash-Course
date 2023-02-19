def make_sandwich(first,second,**sandwich):
    sandwich["first_item"]=first
    sandwich["second_item"]=second
    return sandwich
chicken_sandwich=make_sandwich("chicken","fries",sauce_type="white sauce")
print(chicken_sandwich)
