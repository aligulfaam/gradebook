front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)

# Your code below: 

# Checkpoint 2
front_display_list.insert(0, "Pineapple")
print(front_display_list)

data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

# Your code below: 

# Checkpoint 2
data_science_topics.pop()
print(data_science_topics)

# Checkpoint 3
data_science_topics.pop(3)
print(data_science_topics)

# Checkpoint 1
number_list = range(9)
print(list(number_list))

# Checkpoint 2
zero_to_seven = range(8)
print(list(zero_to_seven))

# Checkpoint 1
number_list = range(9)
print(list(number_list))

# Checkpoint 2
zero_to_seven = range(8)
print(list(zero_to_seven))

long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

big_range = range(2, 3000, 10)

# Your code below: 

# Checkpoint 1 & 2
long_list_len = len(long_list)
print(long_list_len)

# Checkpoint 3 & 4
big_range_length = len(big_range)
print(big_range_length)

# Checkpoint 5
# Change range_list to be equal to range(2, 3000, 100)

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

beginning = suitcase[0:4]

# Your code below: 

# Checkpoint 2 
# Change beginning to suitcase[0:2]

# Checkpoint 3
middle = suitcase[2:4]
print(middle)

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

# Your code below: 

# Checkpoint 1
last_two_elements = suitcase[-2:]
print(last_two_elements)

# Checkpoint 2
slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)

votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

# Your code below: 

# Checkpoint 1
jake_votes = votes.count("Jake")

# Checkpoint 2
print(jake_votes)

# Checkpoint 1 & 2
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]
addresses.sort()
print(addresses)


# Checkpoint 3
names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()


# Checkpoint 4 & 5
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
sorted_cities = cities.sort(reverse=True)
print(sorted_cities)
print(cities)

games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

# Your code below:
# Checkpoint 1
games_sorted = sorted(games)

# Checkpoint 2
print(games)
print(games_sorted)

inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

# Checkpoint 1
inventory_len = len(inventory)

# Checkpoint 2
first = inventory[0]

# Checkpoint 3
last = inventory[-1]

# Checkpoint 4
inventory_2_6 = inventory[2:6]

# Checkpoint 5
first_3 = inventory[:3]

# Checkpoint 6
twin_beds = inventory.count("twin bed")

# Checkpoint 7
removed_item = inventory.pop(4)

# Checkpoint 8
inventory.insert(10, "19th Century Bed Frame")

#Checkpoint 9
inventory.sort()
print(inventory)

