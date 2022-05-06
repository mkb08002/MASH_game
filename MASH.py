#ask for input on 2 values for places to live - check list for 2 values, prompt question if not 2 values

def place_to_live():
    places_to_live = []
    places_to_live = input("Please type one place you would like to live: ")

    if places_to_live not in player_1['live']:
        player_1['live'] = player_1['live'].append(places_to_live)
    else:
        print("You have already submitted this place. ")

def two_players():
    player_1 = {
        'live':'',
        'marry':'',
        'job':'' }

    if player_1['live'] == False:
        place_to_live()
        print(player_1)


# begin draw swirl/tally marks - button to stop drawing - count swirl lines/tally marks - apply count to lists - cross off item after each count until 1 item on each list remaining