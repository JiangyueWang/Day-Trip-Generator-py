# Day Trip Generator
# This application allows user to randomly select a destination, restaurant, transportaion, and way of entertaiment for their next holiday trip
import random

destinations_list = ['Melbourne', 'Sydney', 'Canberra',
                     'Adelaide', 'Brisbane', 'Tokyo', 'Yokohama', 'Osaka']
restaurants_list = ['resturant_one', 'resturant_two',
                    'resturant_three', 'resturant_four', 'resturant_five']
transportations_list = ['rental car', 'bike',
                        'railway', 'light rail', 'ferry', 'bus']
entertainments_list = ['Visit Local Parks', 'Go On A Hike',
                       'Historic Sights & Museums', 'Have A Picnic',
                       'Book A Day Tour Or Excursion', 'Tasting Local Popular Foods']


# return a random element from the list
def rand_item(input_list):
    random_index = random.randint(0, len(input_list)-1)
    random_element = input_list[random_index]
    return random_element


# save the random selected item into a rand_item_list
def append_rand_item(random_type, random_type_list):
    random_type_list.append(random_type)
    return random_type_list
