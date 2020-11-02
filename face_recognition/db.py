import psycopg2
from psycopg2.extras import DictCursor
from contextlib import closing

def get_data():
    result = []
    with closing(psycopg2.connect(dbname='face_recognition', user='postgres', password='sokorjopa', host='localhost')) as connection:
        with connection.cursor(cursor_factory=DictCursor) as cursor:
            cursor.execute('select name, surname, age, image from Person')
            for row in cursor:
                result.append({'Name': row['name'], 'Surname': row['surname'], 'Age': row['age'], 'Path': row['image']})
    return result