NAME_MIN_WORD = 2
NAME_MAX_WORD = 3
MAX_POINTS = 10

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

        if name_list >= NAME_MIN_WORD and name_list <= NAME_MAX_WORD:
            character["name"] = name

            name_pass = True
    
    points_pass = False
    
    while(points_pass != True):
        curr_pts = 10
        charisma_pts = int(input("How many points would you like to allocate to charisma?: "))

        if charisma_pts >  MAX_POINTS:
            print("Invalid choice, points must be 10 or less")

        #all points are given so no need to allocate points for stealth
        if charisma_pts == MAX_POINTS:
            print("Max points given. Character setup is complete")
            character["charisma"] = charisma_pts
            character["stealth"] = 0
       
        if charisma_pts <= MAX_POINTS:
            curr_pts = MAX_POINTS - curr_pts
            print("Points remaining is ", +str(curr_pts))

            stealth_pass = False

            while(stealth_pass != True):
                stealth_pts = int(input("How many points would you like to put into Stealth?: "))
                
                if(stealth_pts > curr_pts)

        
            

    return character

    

def load_events(event_file_name):
    """
    This function will take the file name and return it to a dictionary of events that we can use.
    :param event_file_name: the name of the file with the events
    :return: the events in a dictionary that we can use
    """

def load_map(map_file_name):
    """
    This function will take a file with a list of locations and return a map that we can use
    :param map_file_name: the file with the locations
    :return: a map for rest of the program to use
    """

def play_game(start_time, game_map, events):
    """
    This function will play our game and use the map and events we got from the other functions to run and keep track of the time remaining
    :param start_time: the time we have to get to ITE
    :param game_map: the map that we will use to navigate through UMBC
    :param events: the dictionary of events that we will use if we reach a location with a event
    :return: nothing
    """

if __name__ =="__main__":
