import pickle
import os

cities = ['Berlin', 'Beijing', 'Sydney', 'Moscow']

# with open('cities.bin', 'ab') as fileObject:
#     pickle.dump(cities, fileObject)

with open('cities.bin', 'rb') as fileObject:
    val = os.stat("cities.bin").st_size == 0
    data = pickle.load(fileObject)
    print(data)
    print('something')