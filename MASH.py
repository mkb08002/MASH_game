#ask for input on 2 values for places to live - check list for 2 values, prompt question if not 2 values

def place_to_live():
    places_to_live = []
    
    if len(places_to_live) < 2:
        places_to_live = input("Please type one place you would like to live: ")
        for place in places_to_live:
            if place not in player_1['live']:
                player_1['live'] = player_1['live'].append(places)
            else:
                print("You have already submitted this place. ")
    print(player_1)

def play_the_game():
    player_1 = {
        'live':'',
        'marry':'',
        'job':'' }
    
    place_to_live()

play_the_game()

# begin draw swirl/tally marks - button to stop drawing - count swirl lines/tally marks - apply count to lists - cross off item after each count until 1 item on each list remaining