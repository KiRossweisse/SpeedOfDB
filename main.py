import csv
import random
import os
from faker import Faker
fake = Faker()
# Set the path to the desktop directory
desktop_path = os.path.expanduser("~/Desktop")
print('Desktop path: ', desktop_path)
# Generate unique primary keys
game_id_counter = 1
player_id_counter = 1
review_id_counter = 1
list_of_genres = ['Adventure game', 'Action', 'RPG', 'Simulation video game', 'Sports', 'Fighting',
                  'Platformer', 'Puzzle', 'Survival horror', 'Real-time strategy', 'Sandbox', 'Shooter',
                  'First-person shooter', 'Multiplayer online battle arena', 'Strategy',
                  'Massively Multiplayer Online Game (MMO)', 'Racing', 'Survival games', 'Action RPG',
                  'Battle royale game', 'Stealth game', 'Tactical role-playing game', 'Casual']
release_dates=[]
# Generate data and save to CSV files
with open(os.path.join(desktop_path, 'games.csv'), 'w', newline='') as games_file, \
open(os.path.join(desktop_path, 'players.csv'), 'w', newline='') as players_file, \
open(os.path.join(desktop_path, 'reviews.csv'), 'w', newline='') as reviews_file:
    games_stat = csv.writer(games_file)
    players_stat = csv.writer(players_file)
    reviews_stat = csv.writer(reviews_file)
# Adding headers to csv files
    games_stat.writerow(['game_id', 'title', 'genre', 'release_date'])
    players_stat.writerow(['player_id', 'nickname', 'email'])
    reviews_stat.writerow(['review_id', 'game_id', 'player_id', 'mark', 'review_date'])
    print('Headers written to CSV files')
# Creating game's data
    for i in range(1000000):
        title = fake.catch_phrase()
        genre = random.choice(list_of_genres)
        release_date = fake.date_between(start_date='-30y', end_date='today')
        games_stat.writerow([game_id_counter, title, genre, release_date])
        release_dates.append(release_date)
        game_id_counter += 1
        if (i + 1) % 100000 == 0:
            print(f"{i + 1} samples has been created")
    print('Game data has been successfully created')
# Creating player's data
    for i in range(1000000):
        nickname = fake.name()
        email = fake.email()
        players_stat.writerow([player_id_counter, nickname, email])
        player_id_counter += 1
        if (i + 1) % 100000 == 0:
            print(f"{i + 1} samples has been created")
    print('Player data has been successfully created')
# Creating review data
    for i in range(1000000):
        game_id = random.randint(1, 1000000)
        player_id = random.randint(1, 1000000)
        mark = random.randint(1, 5)
        release_date = release_dates[review_id_counter - 1]
        review_date = fake.date_between(start_date=release_date, end_date='today')
        reviews_stat.writerow([review_id_counter, game_id, player_id, mark, review_date])
        review_id_counter += 1
        if (i + 1) % 100000 == 0:
            print(f"{i + 1} samples has been created")
    print('Review data has been successfully created')
