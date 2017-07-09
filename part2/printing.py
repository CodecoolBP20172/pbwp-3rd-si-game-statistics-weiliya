from reports import *

# Printing functions
name = 'game_stat.txt'
title = 'The Sims 3'
print('Q1: What is the title of the most played game?\nA1: {0} \n'.format(get_most_played(name)))
print('Q2: How many copies have been sold total?\nA2: {0} \n'.format(sum_sold(name)))
print('Q3: What is the average selling?\nA3: {0} \n'.format(get_selling_avg(name)))
print('Q4: How many characters long is the longest title?\nA4: {0} \n'.format(count_longest_title(name)))
print('Q5: What is the average of the release dates?\nA5: {0} \n'.format(get_date_avg(name)))
print('Q6: What properties has a game?\nA6: {0}'.format(get_game(name, title)))
print('Q7: How many games are there grouped by genre?\nA7: {0} \n'.format(count_grouped_by_genre(name)))
print('Q8: What is the date ordered list of the games?\nA8: {0} \n'.format(get_date_ordered(name)))