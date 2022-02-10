# imports
import datetime as dt

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


class UpdateRecord():
    """Updates a job entry to add to the database"""

    def __init__(self, last_contact=False):
        if last_contact:
            self.company = self.get_company()
        else:
            self.company = self.get_company()
            self.column = self.get_column()
            self.value = self.get_value()

    def get_company(self):
        return input('enter the company name to update:\n> ')

    def get_column(self):
        return input('enter to column name to update:\n> ')

    def get_value(self):
        return input(f'input the new value for {self.column}:\n> ')


if __name__ == '__main__':
    print('Please provide inputs.\n')
    # get inputs

    contact_date = input('Update last contact date? (y/n)\n> ')

    if contact_date.lower() == 'y':
        record = UpdateRecord(last_contact=True)
        query = f'''UPDATE jobs 
                    SET last_contact = '{dt.date.today()}'
                    WHERE company = '{record.company}'
        '''
        print(f'{record.company} record updated: last_contact {dt.date.today()}.')
    else:
        record = UpdateRecord()
        query = f'''UPDATE jobs
                    SET {record.column} = '{record.value}', last_contact = '{dt.date.today()}'
                    WHERE company = '{record.company}'
        '''
        print(f'{record.company} record updated: {record.column} == {record.value}.')

    # push data to the database
    with conn.cursor() as c:
        c.execute(query)

    conn.commit()
