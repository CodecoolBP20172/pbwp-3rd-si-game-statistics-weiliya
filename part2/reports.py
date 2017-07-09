import math
import csv
# Report functions

'''What is the title of the most played game?
Expected name of the function: get_most_played(file_name)
Expected output of the function: (string)
Other expectation:  if there is more than one, then return the first from the file'''

def get_most_played(file_name):
    most_played = list()
    with open(file_name, 'r') as file:
        for line in file:
            column = line.split("\t")
            most_played.append(column[0])

    tmp = ""
    for i in range(0, len(most_played)):
        for j in range(i, len(most_played)):
            if(most_played[i] > most_played[j]):
                tmp = most_played[i]
                most_played[i] = most_played [j]
                most_played[j] = tmp

            return most_played[0]

'''How many copies have been sold total?
Expected name of the function: sum_sold(file_name)
Expected output of the function: (number)'''

def sum_sold(file_name):
    s_sold = list()
    with open(file_name, 'r') as file:
        for line in file:
            column = line.split("\t")
            s_sold.append(column[1])

    return sum(map(float,s_sold))

'''What is the average selling?
Expected name of the function: get_selling_avg(file_name)
Expected output of the function: (number)
Other expectation: if there is more than one, then return the first from the file'''

def get_selling_avg(file_name):
    s_sold = list()
    with open(file_name, 'r') as file:
        for line in file:
            column = line.split("\t")
            s_sold.append(column[1])

    return (sum(map(float,s_sold))/float(len(s_sold)))

'''How many characters long is the longest title?
Expected name of the function: count_longest_title(file_name)
Expected output of the function: (number)'''

def count_longest_title(file_name):
    titles = list()
    with open(file_name, 'r') as file:
        for line in file:
            column = line.split("\t")
            titles.append(column[0])
            clt = len(max(titles, key=len))
        
        return clt

'''What is the average of the release dates?
Expected name of the function: get_date_avg(file_name)
Expected output of the function: average year (number)
Other expectation: the return value must be the rounded up average'''

def get_date_avg(file_name):
    years = list()
    with open(file_name, 'r') as file:
        for line in file:
            column = line.split("\t")
            years.append(int(column[2]))
            
    round_year = sum(years)/len(years)

    return math.ceil(round_year)


'''What properties has a game?
Expected name of the function: get_game(file_name, title) .
Expected output of the function: a list of all the properties of the game (a list of various type).
Details: the function get a parameter named game. This is the title of the game (string). This is an existent game.
The function return a list of the properties of this game including the title.
An example return value: ["Minecraft", 23, 2009, "Survival game", Microsoft].'''

def get_game(file_name, title):
    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter="\t")
        game_properties_list =map(lambda row: (row[0], float(row[1]), int(row[2]), row[3], row[4]), reader)

        for game_properties in game_properties_list:
            if game_properties[0] == title:
                return list(game_properties)


'''How many games are there grouped by genre?
Expected name of the function: count_grouped_by_genre(file_name)
Expected output of the function: a dictionary with this structure: { [genre] : [count] }
Detailed description: return a dictionary where each genre is associated with the count of the games of its genre'''

def count_grouped_by_genre(file_name):
    genre_dict = {}
    with open(file_name, 'r') as file:
        for line in file:
            column = line.split("\t")
            if column[3] in genre_dict:
                genre_dict[column[3]] += 1
            else:
                genre_dict[column[3]] = 1

    return genre_dict

'''What is the date ordered list of the games?
Expected name of the function: get_date_ordered(file_name)
Expected output of the function: the date ordered list of the titles (list of string)
Other expectation: The secondary ordering rule is the alphabetical ordering of the titles.
So if there are titles from the same year, you need to order them alphabetically in ascending order.'''

def get_date_ordered(file_name):
    titles = list()
    with open(file_name, 'r') as file:
        for line in file:
            row = line.strip("\n").split("\t")
            titles.append(row)
    
    titles = sorted(titles, key=lambda title: title[0])
    titles = sorted(titles, key=lambda title: title[2], reverse = True)
    return list(map(lambda title: title[0], titles))