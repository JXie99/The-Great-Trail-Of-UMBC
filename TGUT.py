NAME_MIN_WORD = 2
NAME_MAX_WORD = 3
MAX_POINTS = 10
ZERO_POINTS = 0
STARTING_POINT = 1
DESTINATION = 2


def create_character():
    """
    This function will create the character by getting the name, charisma points, and stealth points.
    charcter will have a first last or first middle last name (2 words or more)
    :return: the name, charisma points, and stealth points in a dictionary
    """

    name_pass = False
    character = {}

    #handles user entering name
    #makes sure user is entering a name with 2 words and no more than 3 words 
    while(name_pass == False):
        name = input("Enter your full name: ")
        name_list = name.split()

        #name must be 2 or 3 words
        if len(name_list) >= NAME_MIN_WORD and len(name_list) <= NAME_MAX_WORD:
            character["name"] = name

            name_pass = True
        
        else:
            print("Invalid Name, Must have 2 or 3 words")
    
    charisma_pass = False
    stealth_pass = False

    curr_pts = MAX_POINTS

    #allocates points to charisma
    while(charisma_pass != True):
        charisma_pts = int(input("How many points would you like to allocate to charisma?: "))

        if charisma_pts >  MAX_POINTS:
            print("Invalid choice, points must be 10 or less")
       
        if charisma_pts <= MAX_POINTS:
            if charisma_pts == MAX_POINTS:
                print("Max points given. Character setup is complete")
                character["charisma"] = charisma_pts
                character["stealth"] = 0
                charisma_pass = True
                stealth_pass = True

            else:
                curr_pts = curr_pts - charisma_pts
                print("Points remaining is ", str(curr_pts))
                character["charisma"] = charisma_pts
                charisma_pass = True


    #allocates points to stealth if there are points left over
    while(stealth_pass != True):
        stealth_pts = int(input("How many points would you like to put into stealth?: "))
        
        if(stealth_pts > curr_pts):
            print("Invalid entry, exceeds curr points left")
        
        if(stealth_pts <= curr_pts):
            curr_pts_test = ZERO_POINTS
            curr_pts_test = curr_pts - stealth_pts

            if curr_pts_test != ZERO_POINTS:
                print("all points must be allocated.")
            
            else:
                character["stealth"] = stealth_pts
                stealth_pass = True
    
    return character
    

def load_events(event_file_name):
    """
    This function will take the file name and return it to a dictionary of events that we can use.
    :param event_file_name: the name of the file with the events
    :return: the events in a dictionary that we can use
    """

    with open(event_file_name) as file:
        event_dict = {}

        for x in file:
            line_list = x.strip().split(",")

            event_dict[line_list[0]] = {}
            event_dict[line_list[0]]["event txt"] = line_list[1]
            event_dict[line_list[0]]["event win txt"] = line_list[2]
            event_dict[line_list[0]]["event lose txt"] = line_list[3]
            event_dict[line_list[0]]["charisma to win"] = int(line_list[4])
            event_dict[line_list[0]]["stealth to win"] = int(line_list[5])
            event_dict[line_list[0]]["time lost"] = int(line_list[6])


def load_map(map_file_name):
    """
    This function will take a file with a list of locations and return a map that we can use
    :param map_file_name: the file with the locations
    :return: a map for rest of the program to use
    """
    map ={}
    with open(map_file_name) as f:

        for x in f:
            curr_item = x.strip().split(", ")

            if len(curr_item) == STARTING_POINT:
                map[curr_item[0]] = {}
                temp_dest = curr_item[0]
            
            if len(curr_item) == DESTINATION:
                map[temp_dest][curr_item[0]] = int(curr_item[1])
                



def play_game(start_time, game_map, events):
    """
    This function will play our game and use the map and events we got from the other functions to run and keep track of the time remaining
    :param start_time: the time we have to get to ITE
    :param game_map: the map that we will use to navigate through UMBC
    :param events: the dictionary of events that we will use if we reach a location with a event
    :return: nothing
    """

    new_character = create_character()
    print("You are currently in The Dorms and have ", start_time, " seconds left. Where would you like to go?")

if __name__ =="__main__":

    load_map("maps.txt")
    load_events("events.txt")
    game_time = int(input("How many seconds would you like to have? "))