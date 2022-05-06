#ask for input on 2 values for places to live - check list for 2 values, prompt question if not 2 values
player_1 = {
    'live':'',
    'marry':'',
    'job':'' }

def play_the_game():
    
    place_to_live()
    # person_to_marry()
    # career()

def place_to_live():
    places_to_live = []
    player_1['live'] = places_to_live

    
    while len(places_to_live) < 2:
        places_input = input("Please type one place you would like to live: ")
        if places_input not in places_to_live:
            places_to_live.append(places_input)
        else:
            print("You have already submitted this place. ")
    print(player_1)

play_the_game()

# begin draw swirl/tally marks - button to stop drawing - count swirl lines/tally marks - apply count to lists - cross off item after each count until 1 item on each list remaining