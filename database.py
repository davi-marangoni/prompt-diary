import psycopg2

connection = psycopg2.connect(
    host='localhost',
    database='diary',
    user='postgres',
    password='postgres'
)
cursor = connection.cursor()


def add_event(event_content, event_data):
    with connection:
        cursor.execute("INSERT INTO events (event_description, event_date) VALUES (%s, %s);", (event_content, event_data))


def list_events():
    cursor.execute("SELECT * FROM events;")
    return cursor