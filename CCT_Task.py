from typing import List


def find_maximum_distance( number_of_cities: int, cities_with_train_station: List[int]) -> int:

    if number_of_cities < 1:
        print("ERROR: Number of cities < 1")
        return -1
    elif number_of_cities > 10000:
        print("ERROR: Number of cities > 10000")
        return -1  

    if len(cities_with_train_station) < 1:
        print("ERROR: Number of cities with train station < 1")
        return -1  
    elif len(cities_with_train_station) > number_of_cities:
        print("ERROR: Number of cities with train station > number of cities")
        return -1  
    
    if len(cities_with_train_station) != len(set(cities_with_train_station)): # We check if there are no duplicates in the list
        print("No city can have more than one train station.")
        return -1

    if number_of_cities == len(cities_with_train_station): # We check, because maybe all of the cities will have a train station so the distance will be 0
        return 0
    
    cities_with_train_station.sort() # We sort the list so all the indexes of train stations are in order
    res = cities_with_train_station[0] # Because our list is sorted, we can calculate the distance from the first city to the first train station which is the first element of the list
    
    for ind in range(1, len(cities_with_train_station)): # We calculate the distance between all the train stations
        res = max(res, (cities_with_train_station[ind] - cities_with_train_station[ind-1]) // 2 ) # "//" is used for integers
        
    res = max(res, number_of_cities-1 - cities_with_train_station[-1]) #to compare my current maximum distance with the from the last city to the last train station

    return res


if __name__ == "__main__":
    
    assert find_maximum_distance(number_of_cities=3, cities_with_train_station=[1]) == 1
    assert find_maximum_distance(number_of_cities=4, cities_with_train_station=[3]) == 3
    assert (find_maximum_distance(number_of_cities=5, cities_with_train_station=[0, 4]) == 2)
    
    print("ALL TESTS PASSED")

