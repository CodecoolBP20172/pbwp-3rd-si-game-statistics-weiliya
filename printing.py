from reports import *
# Printing functions

name = 'game_stat.txt'
year = 2000
genre = 'Simulation	Electronic Arts'
title = 'The Sims 3'
print('Q: How many games are in the file?\nA: {0} \n'.format(count_games(name)))
print('Q: Is there a game for a given year?\nA: {0} \n'.format(decide(name, year)))
print('Q: Which was the latest game?\nA: {0} \n'.format(get_latest(name)))
print('Q: How many games do we have by genre?\nA: {0} \n'.format(count_by_genre(name, genre)))
print('Q: What is the line number of the given game (by title)?\nA: {0} \n'.format(get_line_number_by_title(name, title)))
print('Q: What is the alphabetical ordered list of the titles?\nA: '.format(sort_abc(name)))