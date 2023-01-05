import psycopg2
import psycopg2.extras
import random
import time
# created the connection to the database via terminal until the GUI is done .

# connect to db
hostname = 'localhost'
port = 5432
username = 'postgres'
pwd = 'mysoul2323'
Database = 'anime_db'
connect = None # -> connection
cur = None #-> cursor

# main banner
def main():
    print('**************************************************************')
    time.sleep(0.3)
    print('\nHOLA! , WELCOME TO YOUR AWESOME DB WHICH UR AWESOME BRAIN HAS CREATED . \n')
    print('----------------------------------------------------------------')
    time.sleep(0.3)
    print(''' 1- INSERT INTO Db\n 2- RECOMMEND ME an anime ASAP. \n 3- Remove From DB.''')
    Choose_menue = input('\n>')
    return Choose_menue

def remove():
    table_name = input('\n1- REMOVE from Studio table.\n 2- REMOVE from anime_shows table.\n 3- REMOVE from anime_movies table.')
    return table_name

# body:
try:
    with psycopg2.connect(
            host=hostname,
            user=username,
            port=port,
            password=pwd,
            dbname=Database) as connect:

        with connect.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

            main = main()
            if main == '1':
                Insert_input = input(
                    ' Choose 1 to add to studio table\n Choose 2 to Add to anime_shows Table. \n Choose 3 to Add to anime_movies DB:')
                if Insert_input == '1':
                    # INSERT
                    SQL_INSERT_studio = 'INSERT INTO studio(studio_id,name) VALUES(%s,%s);'
                    SQL_studio_values = (int(input('ID:')), input('Studio Name:'))
                    cur.execute(SQL_INSERT_studio, SQL_studio_values)
                    connect.commit()

                elif Insert_input == '2':
                    # INSERT shows
                    SQL_INSERT_shows = 'INSERT INTO anime_shows VALUES(%s,%s,%s,%s,%s,%s,%s,%s); '
                    SQL_INSERT_shows_value = (
                        int(input('ID:')), input('Title:'), input('Release_year:'), int(input('studio ID:')),
                        input('is the anime contiuned? True/False'), input('genre:'), int(input('raiting')),
                        int(input('episodes :')))
                    cur.execute(SQL_INSERT_shows, SQL_INSERT_shows_value)

                elif Insert_input == '3':
                    # INSERT moives
                    SQL_INSERT_movies = 'INSERT INTO anime_movies VALUES(%s,%s,%s,%s,%s,%s);'
                    SQL_movies_values = (
                        input('ID:'), input('Movie Title:'), input('Release Year:'), input('Studio ID:'),
                        input('Genre:'),
                        int(input('Rating:')))
                    cur.execute(SQL_INSERT_movies, SQL_movies_values)

            elif main == '2':
                # rec
                print(' \nChoose one : Action - Comedy - Romance - Adventure\n')
                Genre_input = input("Genre:\n >")
                type_input = input('Type Movie/show: \n >')
                SQL_shows = 'SELECT * FROM anime_shows;'
                SQL_movies = 'SELECT * FROM anime_movies;'

                if Genre_input == 'Action':
                    if type_input == 'show':
                        cur.execute(SQL_shows)
                    elif type_input == 'movie':
                        cur.execute(SQL_movies)
                    anime_list = cur.fetchall()  # -> anime_list ->[ -> anime[recs]]
                    title_list = []
                    genre_list = []

                    for rec in anime_list:
                        if 'Action' in rec['genre']:
                            title_list.append(rec['title'])
                            genre_list.append(rec['genre'])
                            print('.......... Scaaning........'.center(85))
                            time.sleep(0.2)
                    print('We recommend : ', random.choice(title_list))
                    print('\n', 'Genre:', random.choice(genre_list))

                elif Genre_input == 'Romance':
                    if type_input == 'show':
                        cur.execute(SQL_shows)
                    elif type_input == 'movie':
                        cur.execute(SQL_movies)
                    anime_list = cur.fetchall()
                    romance_list = []
                    romance_list2 = []

                    for romance_anime in anime_list:
                        if 'Romance' in romance_anime['genre']:
                            romance_list.append(romance_anime['title'])
                            romance_list2.append(romance_anime['genre'])
                            print('.......... Scaaning........'.center(60))
                            time.sleep(0.2)
                    print('We recommend : ', random.choice(romance_list))
                    print('\n', 'Genre:', random.choice(romance_list2))

                elif Genre_input == 'Comedy' and type_input == 'show':
                    cur.execute(SQL_shows)
                    anime_list = cur.fetchall()  # -> anime_list ->[ -> anime[recs]]
                    comedy_list = []
                    comedy2_list = []

                    for comedy in anime_list:
                        if 'Comedy' in comedy['genre']:
                            comedy_list.append(comedy['title'])
                            comedy2_list.append(comedy['genre'])
                            print('.......... Scaaning........'.center(60))
                            time.sleep(0.2)
                    print('We recommend : ', random.choice(comedy_list))
                    print('\n', 'Genre:', random.choice(comedy2_list))

                elif Genre_input == 'Adventure' and type_input == 'show':
                    cur.execute(SQL_shows)
                    anime_list = cur.fetchall()  # -> anime_list ->[ -> anime[recs]]
                    Adventure_1_list = []
                    Adventure_2_list = []

                    for anime in anime_list:
                        if 'Adventure' in anime['genre']:
                            Adventure_1_list.append(anime['title'])
                            Adventure_2_list.append(anime['genre'])
                            print('.......... Scanning........'.center(60))
                            time.sleep(0.2)
                    print('We recommend : ', random.choice(Adventure_1_list))
                    print('\n', 'Genre:', random.choice(Adventure_2_list))

                else:
                    print('PLEASE TRY AGAIN , CHECK YOUR SPELLING /CAPITALIZATION')

            elif main == '3': # this mf
                # remove
                if remove() == '1': # -> studio table
                    SQL_remove_studio = '''ALTER TABLE studio DROP COLUMN %s;'''
                    remove_input = input('\nColumn name ... >')
                    cur.execute(SQL_remove_studio, remove_input)

                elif remove() == '2':# -> remove from anime_shows table
                    SQL_remove_shows = '''ALTER TABLE anime_shows DROP COLUMN %s;'''
                    remove_input = input('\nColumn name ... >')
                    cur.execute(SQL_remove_shows,remove_input)

                elif remove() == '3':
                    SQL_remove_movies = '''ALTER TABLE anime_movies DROP COLUMN %s'''
                    remove_input = input('\nColumn name ... >')
                    cur.execute(SQL_remove_movies,remove_input)

            else:
                print('Choose a vaild input.')
        connect.commit()
except:
    print('WEO WEO WEO BAD CONNECTION AMIGO')

finally:
    if connect and cur:
        connect.close()
        print('********connected **************'.center(80))
    else:
        print(False, 'weo weo weo')
