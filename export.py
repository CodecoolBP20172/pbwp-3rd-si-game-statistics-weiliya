from reports import *

# Export functions
def export(from_file_name, to_file_name):
    titles = set()
    years = set()
    genres = set()
    with open(from_file_name, 'r') as file:
        for line in file:
            parts = line.split("\t");
            titles.add(parts[0])
            years.add(int(parts[2]))
            genres.add(parts[3])

    with open(to_file_name, 'w') as out_file:
        out_file.write("game count: {0}\n".format(count_games(from_file_name)))
        for current_year in years:
            out_file.write("there is a game for year {0}: {1}\n".format(current_year, decide(from_file_name, current_year)))
        out_file.write("latest game: {0}\n".format(get_latest(from_file_name)))
        for current_genre in genres:
            out_file.write(
                "there number of games in genre {0} is: {1}\n".format(current_genre, count_by_genre(from_file_name, current_genre)))
        for current_title in titles:
            out_file.write('the title "{0}" is in the {1}. line\n'.format(current_title, get_line_number_by_title(from_file_name, current_title)))
        out_file.write("titles in alphabetical order: {0}\n". format(sort_abc(from_file_name)))
        out_file.write("the genres are: {0}\n". format(get_genres(from_file_name)))
        out_file.write("the top sold FPS release date is: {0}\n". format(when_was_top_sold_fps(from_file_name)))



export('game_stat.txt', 'export.txt')