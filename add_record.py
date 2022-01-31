# imports
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


class CreateRecord:
    """Creates a job entry to add to the database"""

    def __init__(self):
        self.company = self.get_company()
        self.status = self.get_status()
        self.date_applied = self.get_date_applied()
        self.last_contact = self.get_last_contact()

    def get_company(self):
        return input(f'company:\n> ')

    def get_status(self):
        return input(f'status:\n> ')

    def get_date_applied(self):
        return input(f'date applied (YYYY-MM-DD):\n> ')

    def get_last_contact(self):
        return input(f'date of last contact (YYYY-MM-DD):\n> ')


if __name__ == '__main__':
    print('Please provide inputs.\n')

    # get data
    record = CreateRecord()

    # build query
    query = f"""
            INSERT INTO jobs (
                company, status, date_applied, last_contact
            )
            VALUES (
                '{record.company}', '{record.status}', '{record.date_applied}',
                '{record.last_contact}'
            );
            """

    # push data to the database
    with conn.cursor() as c:
        c.execute(query)

    conn.commit()

    print(f'Record added for company: {record.company}.')
