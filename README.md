# Job Application Tracker

Simple tool for tracking the status of job applications. Feel free to fork and adapt to your needs.

## DB Contruction

The business logic is designed for [Postresql](https://www.postgresql.org/download/). If you want a different db, you'll have to change some of the logic.

Table:

```SQL
-- Table Definition ----------------------------------------------

CREATE TABLE jobs (
    uuid uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
    company character varying(64),
    status character varying(64),
    date_applied date,
    last_contact date
);

-- Indices -------------------------------------------------------

CREATE UNIQUE INDEX jobs_pkey ON jobs(uuid uuid_ops);
```

## Code

### import_csv_data.py

I was previously tracking the applications that I submitted in a .csv.

Columns

`company` `status` `date_applied` `last_contact`

### add_record.py

Allows user to add a record for a CLI.

1. Fast add: Requires input for the `company` name.
2. Detailed add: Requires inputs for all columns.

### update_record.py

Prompts user for `table`, `company` name, `column`, new `value`. Auto updates `last_contact` to `dt.date.today()`.
