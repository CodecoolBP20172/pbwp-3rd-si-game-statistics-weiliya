#open file once in a function
#sorted in a separate function
# Report functions

#How many games are in the file?
def count_games(file_name):
    games = set()
    with open(file_name, 'r') as file:
        for line in file:
            games.add(line)

    return len(games)


#Is there a game for a given year?
def decide(file_name, year):
    with open(file_name, 'r') as file:
        '''for line in file:
            column = line.split("\t")
            if(int(column[2]) == year):
                return True'''
        list_of_games = [line.split("\t") for line in file] #if line[2] == year]


#Which was the latest game?
def get_latest(file_name):
    latest_title = ""
    latest_year = 0
    with open(file_name, 'r') as file:
        for line in file:
            column = line.split("\t")
            if (int(column[2]) > latest_year):
                latest_title = column[0]
                latest_year = int(column[2])

    return latest_title


#How many games do we have by genre?
def count_by_genre(file_name, genre):
    count = 0
    with open(file_name, 'r') as file:
        for line in file:
            column = line.split("\t")
            if (column[3] == genre):
                count += 1

    return count


#What is the line number of the given game (by title)?
def get_line_number_by_title(file_name, title):
    with open(file_name, 'r') as file:
        for idx, line in enumerate(file):
            column = line.split("\t")
            if (column[0] == title):
                return idx + 1
    raise ValueError


#What is the alphabetical ordered list of the titles?
def sort_abc(file_name):
    titles = list()
    with open(file_name, 'r') as file:
        for line in file:
            column = line.split("\t")
            titles.append(column[0])

    tmp = ""
    for i in range(0, len(titles)):
        for j in range(i, len(titles)):
            if(titles[i] > titles[j]):
                tmp = titles[i]
                titles[i] = titles[j]
                titles[j] = tmp

    return titles


#What are the genres?
def get_genres(file_name):
    genres = set()
    with open(file_name, 'r') as file:
        for line in file:
            column = line.split("\t")
            genres.add(column[3])

    return sorted(list(genres), key=str.lower)


#What is the release date of the top sold "First-person shooter" game?
def when_was_top_sold_fps(file_name):
    found_game = False
    top_sold = 0.0
    release_date = 0
    with open(file_name, 'r') as file:
        for line in file:
            column = line.split("\t")
            if column[3] == "First-person shooter" and float(column[1]) > top_sold:
                top_sold = float(column[1])
                release_date = int(column[2])
                found_game = True
    if found_game:
        return release_date
    else:
        raise ValueError
