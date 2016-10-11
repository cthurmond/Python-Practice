# *** MY CODE ***

import os
import json

key_dict = {}
directory = "/Users/Connor/Documents/Personal Projects/Python/scores"

for filename in os.listdir(directory):
    path_name = os.path.join(directory, filename)
    if os.path.isfile(path_name):
        open_file = open(path_name, "r")
        json_object = json.load(open_file)
        for entry in json_object:
            for key in entry:
                if key in key_dict:
                    key_dict[key].append(entry[key])
                else:
                    key_dict[key] = [entry[key]]
    print path_name
    for keyword in key_dict:
        summ = 0.0;
        count = 0.0;
        for value in key_dict[keyword]:
            summ += value
            count += 1
        average = summ / count
        print keyword + ": " + "min " + str(min(key_dict[keyword]))\
            + ", max " + str(max(key_dict[keyword])) + ", average "\
            + str(average)

        open_file.close()



        
