rainfall_dict = {}

while True:
    city_name = raw_input("Enter the name of a city: ")
    if not city_name:
        for city in rainfall_dict:
            print city + ": " + str(rainfall_dict[city])
        break

    rainfall = raw_input("Enter the rainfall in mm: ")
    
    if city_name in rainfall_dict:
        rainfall_dict[city_name] += int(rainfall)
    else:
        rainfall_dict[city_name] = int(rainfall)

    