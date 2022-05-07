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

mash = ['Mansion', 'Apartment', 'Shack', 'House']
places_to_live = []
person_marry_list = []
future_career = []
future_kids = []
counter = int()

def play_the_game():
    print('''
    You will be prompted to submit 2 places to live, 2 people to marry, 2 careers and how many kids you want. 
    Make sure they are all unique!''')

    place_to_live()
    person_to_marry()
    career()
    num_kids()

    print("Here is your MASH list: ")
    for item in player_1.items():
        print(item)
    print()

    user_range()
    get_results()
    

def place_to_live():
    player_1['live'] = places_to_live
    
    #ask for input on 3 values for places to live - check list for 2 values, prompt question if not 2 values
    while len(places_to_live) < 2:
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
    player_1['marry'] = person_marry_list
    
    #ask for input on 2 values for person to marry - check list for 2 values, prompt question if not 2 values
    while len(person_marry_list) < 2:
        marry_input = input("Please type the name of one person you would like to marry: ")
        if marry_input not in person_marry_list:
            person_marry_list.append(marry_input)
        elif len(marry_input.strip()) == 0:
            print("Make sure to submit an entry. ")
        else:
            print("You have already submitted this person. ")

    person_marry_list.append(characters_random)
    print("The computer has randomly selected [" + characters_random + "] as your third person to marry.\n")


def career():
    player_1['job'] = future_career
    
    #ask for input on 2 values for person to marry - check list for 2 values, prompt question if not 2 values
    while len(future_career) < 2:
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
    player_1['kids'] = future_kids
    kids_random = random.randrange(0, 30)
    
    #ask for input on 2 values for person to marry - check list for 2 values, prompt question if not 2 values
    while len(future_kids) < 2:
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


def get_results():
    mash_final = mash[(counter-1) % len(mash)]
    
    live_final = places_to_live[(counter-1) % len(places_to_live)]

    marry_final = person_marry_list[(counter-1) % len(person_marry_list)]

    job_final = future_career[(counter-1) % len(future_career)]

    kids_final = future_kids[(counter-1) % len(future_kids)]

    print(f"""
    Based on this reading:
    You will live in a {mash_final} in {live_final}.
    You will work as a {job_final}.
    You will marry {marry_final} and have {kids_final} kids.
    """)

# BEGIN THE GAME
play_the_game()



# --- to iterate through dictionary lists and remove item based on counter ---

# for key, values in player_1.items():
#     if isinstance(values, list):
#         to_pop = values[(counter-1) % len(values)]
#         values.remove(to_pop)
# print(player_1)




# begin draw swirl/tally marks - button to stop drawing - count swirl lines/tally marks - apply count to lists - cross off item after each count until 1 item on each list remaining