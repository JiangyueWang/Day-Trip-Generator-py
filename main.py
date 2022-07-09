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


# let user to confirm the random generated item
def user_confirmation_fn(original_type_list, random_type, random_type_list, type):

    while True:
        print(
            f'We have selected {random_type} for your {type}! Does this sound good?')
        user_decision = (input("Enter y/n: ")).lower()
        if user_decision == 'y':
            random_type = random_type
            print(f'Awesome! Glad your {type} is decide, lets move on')
            break
        else:
            while True:
                if len(random_type_list) < len(original_type_list):
                    random_type = rand_item(original_type_list)
                    if random_type not in random_type_list:
                        append_rand_item(random_type, random_type_list,)
                        break
                else:
                    print(
                        f'You havent selected a {type} from the recommendation list, go through again')
                    random_type_list = []
                    continue
            continue
    return random_type


# user confirms the random generated destiantion
def confirmed_destiantion():
    random_destination_list = []
    random_destination = rand_item(destinations_list)
    random_destination_list = append_rand_item(
        random_destination, random_destination_list)
    confirmed_random_destination = user_confirmation_fn(
        destinations_list, random_destination, random_destination_list, "destination")
    return confirmed_random_destination
