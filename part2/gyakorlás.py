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

print(get_most_played('game_stat.txt'))

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

print(sum_sold('game_stat.txt'))

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

print(get_selling_avg('game_stat.txt'))

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

print(count_longest_title('game_stat.txt'))