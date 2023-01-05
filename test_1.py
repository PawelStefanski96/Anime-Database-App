import psycopg2
import psycopg2.extras
import random
# my previous try to connect to the database via clean code :(

hostname = 'localhost'
port = 5432
username = 'postgres'
pwd = 'mysoul2323'
Database = 'anime_db'
connect = None # -> connection
cur = None #-> cursor

class Anime_table:
    def __init__(self, type=None, id=None, title=None, Studio=None,release_year=None ,continued = None, Genre = None , rating = None , eps = None):
        self.type = type
        self.id = id
        self.title = title
        self.Studio = Studio
        self.release_year = release_year
        self.continued = continued
        self.rating = rating
        self.Genre = Genre
        self.eps = eps

    def add_new_studio(self,id,title):
        self.id = id
        self.title = title
        if self.id and self.title:
            Insert_into_studio = 'INSERT INTO TABLE studio (studio_id,name) VALUES(%s,%s)'
            Execute_insert = (id,title)
            return Insert_into_studio%Execute_insert
        return 'WEO WEO ...'

    def add_anime_db(self , type, id ,title, studio,release_year, continued,gerne, rating,eps):
        type,id,title,release_year,studio,conitnued,genre = self.type, self.id , self.title,self.Studio,self.release_year,self.continued,self.Genre
        rating, eps = self.rating , self.eps

        if type == 'show'.upper().lower() and type is not None:
            Insert_into_shows = """INSERT INTO TABLE anime_shows(id,title,release_year,studio_id, conituned,genre,rating, eps )Values(%s,%s,%s, %s ,%s , %s , %s,%s)
            """
            values = (id,title,studio,release_year,conitnued,genre,rating,eps)
            return Insert_into_shows%values
        return "WEO WEO WEO "

    def anime_rec(self, Genre,type , cursor):
        if Genre.lower().upper() is not None or Genre.upper().lower() == self.Genre and type.upper().lower() == self.type:
            Select_all = 'SELECT * FROM anime_shows'

            for anime in cursor.fetchall():
                title = cursor['title']
                date = cursor['release_year']
            print(random.choices(title) , random.choices(date))
            return Select_all
        else:
            return 'WEO WEO WEO ...'

def remove_anime(self, table_column_name):
        drop = 'DROP COULMN IF EXISTS %s'
        drop_value = table_column_name
        return drop%drop_value

def adding_to_table_input():
    type = input('Type:\n')
    id = input('ID :\n')
    title = input('Anime_title: \n')
    studio = int(input('Studio Id: \n'))
    continued = input('is the anime continued ? True/False : \n')
    genre = input('Genre:\n')
    rating = int(input('Rating:\n'))
    eps = int(input('Number of episodes:\n'))

    instance = Anime_table()
    add_command = instance.add_anime_db(type,id,title,studio,continued,genre,rating,eps)
    return add_command

def rec_input():
    genre = input('Genre')
    type = input('Anime Type:\n')
    rec = Anime_table()
    rec_command = rec.anime_rec(genre,type,cur)
    return rec_command

def remove_input():
    column_name = input('Column name:\n')
    column_instance = Anime_table()
    remove_column_command = column_instance.remove_anime(column_name)
    return remove_column_command

def add_studio_input():
    id_input = input('ID:\n >')
    Name_input = input('Studio Name:\n>')
    id_input_instance = Anime_table()
    id_name_command = id_input_instance.add_new_studio(id_input,Name_input)
    return id_name_command


def user_input():
    input_1 = input('''Choose what to do with the data base .
                    I- insert into the table
                    D- delete a column
                    A- recommend anime. >''')
    try:
        if input_1 == 'I':
            return add_studio_input(), adding_to_table_input()
        elif input_1 == 'D':
            return remove_input()
        elif input_1 == 'A':
            return rec_input()
    except:
        print('Something went wrong Hermano weo weo weo')

while True:
    try:
        with psycopg2.connect(
                host=hostname,
                user=username,
                port=port,
                password=pwd,
                dbname=Database) as connect:

            with connect.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                #print(user_input())
                #if user_input():
                 #   cur.execute(user_input())
                    connect.commit()


    except:
        print('WEO WEO WEO BAD CONNECTION AMIGO')

    finally:
        if connect and cur:
            print(True)
            connect.close()
        else:
            print(False, 'weo weo weo')




#print(test.add_new_studio(2,'MAPPA')) -> PASSED
#print(test.edit_anime_db('show', 2,'some anime 2', 'some studio 2', True, 2 ,'Action' , 5)) -> PASSED
#print(test.anime_rec('romance' , 'movie',connect_db()))
#test = Anime_table('show', 2,'some anime', '2002-5-2',90, True,'Action' , 5 , 20)
#print(test.add_anime_db('show', 2,'some anime', '2002-5-2',90, True,'Action' , 5 , 20))