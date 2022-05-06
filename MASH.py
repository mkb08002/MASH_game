import random


with open('cartoon_characters.txt') as character_list:
    characters = character_list.read().splitlines()
characters_random = random.choice(characters)

with open('locations.txt') as location_list:
    locations = location_list.read().splitlines()
locations_random = random.choice(locations)

player_1 = {
    'live':'',
    'marry':'',
    'job':'' }

def play_the_game():
    
    place_to_live()
    person_to_marry()
    # career()

def place_to_live():
    places_to_live = []
    player_1['live'] = places_to_live
    
    #ask for input on 2 values for places to live - check list for 2 values, prompt question if not 2 values
    while len(places_to_live) < 2:
        places_input = input("Please type one place you would like to live: ")
        if places_input not in places_to_live:
            places_to_live.append(places_input)
        else:
            print("You have already submitted this place. ")
    
    places_to_live.append(locations_random)
    print("The computer has randomly selected [" + locations_random + "] as your third place to live.")

def person_to_marry():
    person_to_marry = []
    player_1['marry'] = person_to_marry
    
    #ask for input on 2 values for person to marry - check list for 2 values, prompt question if not 2 values
    while len(person_to_marry) < 2:
        marry_input = input("Please type the name of one person you would like to marry: ")
        if marry_input not in person_to_marry:
            person_to_marry.append(marry_input)
        else:
            print("You have already submitted this person. ")

    person_to_marry.append(characters_random)
    print("The computer has randomly selected [" + characters_random + "] as your third person to marry.")


play_the_game()

# begin draw swirl/tally marks - button to stop drawing - count swirl lines/tally marks - apply count to lists - cross off item after each count until 1 item on each list remaining