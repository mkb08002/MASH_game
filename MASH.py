import random


with open('cartoon_characters.txt') as character_list:
    characters = character_list.read().splitlines()
characters_random = random.choice(characters)

with open('locations.txt') as location_list:
    locations = location_list.read().splitlines()
locations_random = random.choice(locations)

with open('careers.txt') as careers_list:
    careers = careers_list.read().splitlines()
careers_random = random.choice(careers)

player_1 = {
    'MASH':['Mansion', 'Apartment', 'Shack', 'House'],
    'live':'',
    'marry':'',
    'job':'',
    'kids':'' }

def play_the_game():
    print('''
    You will be prompted to submit 3 places to live, 3 people to marry, and 3 careers. 
    Make sure they are all unique!''')

    place_to_live()
    person_to_marry()
    career()
    num_kids()

    print("Here is your MASH list: ")
    for item in player_1.items():
        print(item)

    user_range()
    

def place_to_live():
    places_to_live = []
    player_1['live'] = places_to_live
    
    #ask for input on 3 values for places to live - check list for 2 values, prompt question if not 2 values
    while len(places_to_live) < 3:
        places_input = input("Please type one place you would like to live: ")
        if len(places_input.strip()) == 0:
            print("Make sure to submit an entry. ")
        elif places_input in places_to_live:
            print("You have already submitted this place. ")
        else:
            places_to_live.append(places_input)

    
    places_to_live.append(locations_random)
    print("The computer has randomly selected [" + locations_random + "] as your third place to live.\n")


def person_to_marry():
    person_to_marry = []
    player_1['marry'] = person_to_marry
    
    #ask for input on 2 values for person to marry - check list for 2 values, prompt question if not 2 values
    while len(person_to_marry) < 3:
        marry_input = input("Please type the name of one person you would like to marry: ")
        if marry_input not in person_to_marry:
            person_to_marry.append(marry_input)
        elif len(marry_input.strip()) == 0:
            print("Make sure to submit an entry. ")
        else:
            print("You have already submitted this person. ")

    person_to_marry.append(characters_random)
    print("The computer has randomly selected [" + characters_random + "] as your third person to marry.\n")


def career():
    future_career = []
    player_1['job'] = future_career
    
    #ask for input on 2 values for person to marry - check list for 2 values, prompt question if not 2 values
    while len(future_career) < 3:
        career_input = input("Please type a future career: ")
        if career_input not in future_career:
            future_career.append(career_input)
        elif len(career_input.strip()) == 0:
            print("Make sure to submit an entry. ")
        else:
            print("You have already submitted this job. ")

    future_career.append(careers_random)
    print("The computer has randomly selected [" + careers_random + "] as your third career.\n")


def num_kids():
    future_kids = []
    player_1['kids'] = future_kids
    kids_random = random.randrange(0, 30)
    
    #ask for input on 2 values for person to marry - check list for 2 values, prompt question if not 2 values
    while len(future_kids) < 3:
        kids_input = input("Please type the number of kids you may want: ")
        if kids_input.isnumeric() and kids_input not in future_kids:
            future_kids.append(str(kids_input))
        else:
            print("Please make sure to type a number. ")

    future_kids.append(str(kids_random))
    print("The computer has randomly selected [" + str(kids_random) + "] as your third number of kids option.\n")


def user_range():
    user_range_input = input("The computer will now select a random number between 3 and ... ")
    
    if user_range_input.isnumeric() and int(user_range_input) > 3:
        counter = random.randint(3, (int(user_range_input)+1))
    else:
        print("Make sure to put in a number greater than 3!")
    
    print("The computer has randomly selected the number " + str(counter) + "!")


# BEGIN THE GAME
play_the_game()

# begin draw swirl/tally marks - button to stop drawing - count swirl lines/tally marks - apply count to lists - cross off item after each count until 1 item on each list remaining