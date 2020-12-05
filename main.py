
#Author: Michael Perkins
#Date: 11/24/2020


"""

"""

from itertools import permutations, combinations_with_replacement

city_temps = {
    "Casa_Grande": [76, 69, 60, 64, 69],
    "Chandler": [77, 68, 61, 65, 67],
    "Flagstaff": [46, 35, 33, 40, 44],
    "Lake Havasu City": [71, 65, 63, 66, 68],
    "Sedona": [62, 47, 45, 51, 56]
}

hotel_rates = {
    "Motel 6": 89,
    "Best Western": 109,
    "Holiday Inn Express": 115,
    "Courtyard by Marriott": 229,
    "Residence Inn": 199,
    "Hampton Inn": 209
}


def city_temp_avg(days, city_temps):
    city_names = city_temps.keys()
    city_permutations = list(permutations(city_names))
    max_temp = 0
    tempary_sum = 0
    max_perm = 0
    for i in range(0, len(city_permutations)):
        for j in range(0, len(city_permutations[i])):
            tempary_sum += city_temps[city_permutations[i][j]][j]
        avg = tempary_sum / days
        if avg > max_temp or i == 0:
            max_temp = avg
            max_perm = i
        tempary_sum = 0
    return city_permutations[max_perm], max_temp


HOTEL_BUDGET = 850


def hotel_budget(days, budget, hotel_rates):
    hotel_names = hotel_rates.keys()
    hotel_combo = list(combinations_with_replacement(hotel_names, days))
    max_cost = 0
    max_combo = 0
    tempary_sum = 0
    for i in range(0, len(hotel_combo)):
        for j in range(0, len(hotel_combo[i])):
            tempary_sum += hotel_rates[hotel_combo[i][j]]
        if (tempary_sum > max_cost or i == 0) and tempary_sum <= budget:
            max_cost = tempary_sum
            max_combo = i
        tempary_sum = 0
    #print(hotel_combo[max_combo], max_cost)
    return hotel_combo[max_combo], max_cost


# ...
# ...

if __name__ == "__main__":
    cities = list(city_temps.keys())
    hotels = list(hotel_rates.keys())
    city_temp_avg(5, city_temps)
    hotel_budget(5, HOTEL_BUDGET, hotel_rates)
    # ..
    print(f'Here is your best route: {city_temp_avg(5, city_temps)[0]} the average of the daily max temp. is {city_temp_avg(5, city_temps)[1]}')
    # ..
    print(f'To max out your hotel budget, stay at these hotels: {hotel_budget(5, HOTEL_BUDGET, hotel_rates)[0]}, totaling ${hotel_budget(5, HOTEL_BUDGET, hotel_rates)[1]}')


