import csv

'''What properties has a game?
Expected name of the function: get_game(file_name, title) .
Expected output of the function: a list of all the properties of the game (a list of various type).
Details: the function get a parameter named game. This is the title of the game (string). This is an existent game.
The function return a list of the properties of this game including the title.
An example return value: ["Minecraft", 23, 2009, "Survival game", Microsoft].'''

def get_game(file_name, title):
    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter=",")
        parsed = ((row[0], 
                    float(row[1]),
                    int(row[2]),
                    row[3],
                    row[4])
                for row in reader)

        for game_properties in parsed:
            if game_properties[0] == title:
                return game_properties


print(get_game('game_stat.txt', 'Guild Wars'))





