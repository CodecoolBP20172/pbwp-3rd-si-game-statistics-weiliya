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
        out_file.write("The most played game is: {0}\n".format(get_most_played(from_file_name)))
        out_file.write("All copies sold: {0}\n".format(sum_sold(from_file_name)))
        out_file.write("Digits of the longest title: {0}\n".format(count_longest_title(from_file_name)))
        out_file.write("The average release date of games: {0}\n".format(get_date_avg(from_file_name))) 
        for current_title in titles:         
            out_file.write('The properties of "{0}" are: {1}\n'.format(current_title, get_game(from_file_name, current_title)))
        out_file.write("Games grouped by genre: {0}\n". format(count_grouped_by_genre(from_file_name)))
        out_file.write("Date ordered list of the games: {0}\n". format(get_date_ordered(from_file_name)))

export('game_stat.txt', 'export2.txt')