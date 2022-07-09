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


# user confirms the random generated restaurant
def confirmed_restaurant():
    random_restaurant_list = []
    random_restaurant = rand_item(restaurants_list)
    random_restaurant_list = append_rand_item(
        random_restaurant, random_restaurant_list)
    confirmed_random_restaurant = user_confirmation_fn(
        restaurants_list, random_restaurant, random_restaurant_list, "restaurant")
    return confirmed_random_restaurant


# user onfirms the random generated transportation
def confirmed_transportation():
    random_transportation_list = []
    random_transportation = rand_item(transportations_list)
    random_transportation_list = append_rand_item(
        random_transportation, random_transportation_list)
    confirmed_random_transportation = user_confirmation_fn(
        transportations_list, random_transportation, random_transportation_list, "transportation")
    return confirmed_random_transportation


# user confirms the random generated entertaiment
def confirmed_entertainment():
    random_entertainment_list = []
    random_entertainment = rand_item(entertainments_list)
    random_entertainment_list = append_rand_item(
        random_entertainment, random_entertainment_list)
    confirmed_random_entertainment = user_confirmation_fn(
        entertainments_list, random_entertainment, random_entertainment_list, "entertainment")
    return confirmed_random_entertainment


# main function to run Day Trip Generator
def run():
    while True:
        print("----------choosing destination----------")
        my_destination = confirmed_destiantion()

        print("----------choosing restaurant----------")
        my_restaurant = confirmed_restaurant()

        print("----------choosing transportation----------")
        my_transportation = confirmed_transportation()

        print("----------choosing entertainment ----------")
        my_entertainment = confirmed_entertainment()
        print("----------Trip Confirmation----------")
        print("Congrats! We have completed generating your day trip. Now let's confirm that is the trip you wanted")
        print(
            f'Destiantion: {my_destination}\nRestaurant: {my_restaurant}\nTransportation: {my_transportation}\nEntertainment: {my_entertainment}')
        user_final_confirmation = input(
            'Would you like to finalize this trip? Enter y/n: ')
        if user_final_confirmation == 'y':
            print("Thanks for confirming your trip! Enjoy your holiday")
            break
        else:
            print(f'Did happy with your selection, start again...')
            continue


run()
