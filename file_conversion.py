# Task 1: Reading the file line by line (database.txt)
# Task 2: Collect each record in a data structure
# Task 3: Convert all Titles to a titlecased (Capitalized) version
# Task 4: sort the records alphabetically according to ID
# Task 5: print the sorted table on the console, make sure to line up the comumns with
# one space in between ID, Date and Title, like shown below. Use string formatting and programatically
# determine the widest ID and widest Date beforehand (i.e. do not hardcode it to 8, loop through
# all IDs and find out how many letters the longest ID has!)
# Also, no NOT just use a third party table formatter like prettytable or tabulate, use standard python only!


file = open('database.txt', 'r')
from_string = file.read().split("\n")

keys = []
dates = []
letter = []
for i in from_string:
    if 'ID=' in i:
        new_item = i.replace("ID=", "")
        keys.append(new_item)
    elif 'Date=' in i:
        new_date = i.replace("Date=", "")
        dates.append(new_date)
    elif 'Title=' in i:
        new_title = i.replace("Title=", "").capitalize()
        letter.append(new_title)
    else:
        zero_title = 'None'
        letter.append(zero_title)

merge_a = 0
for i in keys:
    count_id = len(i)
    if count_id > merge_a:
        merge_a = count_id

merge_b = 0
for i in dates:
    count_dates = len(i)
    if count_dates > merge_b:
        merge_b = count_dates

print('ID'+' '*(merge_a-2)+'Date'+' '*(merge_b-4)+'Title')
for i in range(len(keys)):
    print(f'{keys[i]}' + ' ' * (merge_a - len(keys[i]) + 1) +
          f'{dates[i]}' + ' ' * (merge_b-len(dates[i]) + 1) + f'{letter[i]}')

