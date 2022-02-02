import psycopg2

# db global variables
HOST = 'localhost'
USER = 'postgres'
PASSWORD = 'Master/99'
DATABASE = 'job_apps'

print('Initiating database connections.')

# db connection
conn = psycopg2.connect(host=HOST, database=DATABASE,
                        user=USER, password=PASSWORD)

print('Database connected.')

if __name__ == '__main__':
    query = input('enter a sql query to execute:\n> ')

    with conn.cursor() as c:
        c.execute(query)

        results = c.fetchall()
        print(results)
