"""
This project will start as a basic command line tool to track job applications 
with a Postgres SQL database.

I intend to create a GUI for this project


The project will have the following features:
- Add a position to the database
- Edit a position
- Display all positions
- Display positions through filters
- Utilize the rich library for a better command line interface
"""

import psycopg2
import pandas as pd
from rich.console import Console
from rich.table import Column, Table
from datetime import date
from os import system, name
from pick import pick

def clear_screen():
    """
    Clears the screen
    """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def execute_query(query):
    """
    Connects to and executes a query on the database
    """
    c = Console()
    try:
        conn = psycopg2.connect(host = 'localhost', dbname = 'jobs', user='postgres', password='zfechko')
        cursor = conn.cursor()
        #c.print('[bold green]Connected to the database[/bold green]')
    except:
        c.print('[bold red]Failed to connect to the database[/bold red]')
        exit()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    if 'SELECT' in query:
        return cursor.fetchall()
    else:
        c.print('[bold green]Changes made successfully[/bold green]')


def add_listing():
    """
    Adds a listing to the database
    """
    clear_screen()
    c = Console()
    c.print('[bold]Adding a listing[/bold]')
    job_title = input('Job Title: ').title()
    company = input('Company Name: ')
    salary = input('Lower value of salary range: ')
    city = input('City: ').title()
    state = input('State: ').upper()
    options = ['In Person', 'Hybrid', 'Remote']
    title = 'Job Type: '
    job_type, index = pick(options, title, indicator='->')
    job_type = options[index]
    applied_on = date.today()
    query = f"INSERT INTO POSITION (title, company, salary, job_city, job_state, job_type, applied_on) VALUES ('{job_title}', '{company}', {salary}, '{city}', '{state}', '{job_type}', '{applied_on}');"
    execute_query(query)
    pass

def update_listing():
    """
    Updates an attribute of an existing listing

    - Prompts the user to input the ID of a listing
    - Shows the user the current attributes of the listing and prompts for which attribute to update
    - User inputs new attribute value and the listing in the DB is updated
    """
    clear_screen()
    c = Console()
    
    results = execute_query("SELECT TITLE, COMPANY FROM POSITION ORDER BY ID ASC;")
    options = [f'{row[0]} at {row[1]}' for row in results]
    title = "Select a listing to update: "
    selected, index = pick(options, title, indicator='->')
    id = index + 2 # ID is off in DB

    options = ['Job Title', 'Company', 'Salary', 'City', 'State', 'Job Type', 'Application Date', 'Application Status']
    title = f"What would you like to update from {selected}?"
    option, index = pick(options, title, indicator='->')
    new_value = input('Enter the new value: ')


    index_to_attribute_dict = {0: 'title', 1: 'company', 2: 'salary', 3: 'job_city', 4: 'job_state', 5: 'job_type', 6: 'applied_on', 7: 'status'}
    query = f"UPDATE POSITION SET {index_to_attribute_dict[index]} = '{new_value}' WHERE id = {id};"
    execute_query(query)

def display_all_listings():
    """
    Displays all listings in the database

    - Displays all listings in the database using rich table
    - Shows the user the number of listings in the database
    """
    clear_screen()
    query = f"SELECT * FROM POSITION ORDER BY STATUS, ID ASC;"
    result = execute_query(query)
    table = Table(
        #"ID",
        Column(header="Job Title", no_wrap=True, style="cyan"),
        Column(header="Company", no_wrap=True, style="magenta"),
        Column(header="Salary", style="green"),
        "City",
        "State",
        "Job Type",
        "Applied On",
        "Application Status",
        title='Jobs I\'ve Applied To')

    for row in result:
        table.add_row(row[1], row[2], row[3], row[4], row[5], row[6], row[7].strftime('%b %d'), row[8])

    c = Console()
    c.print(table)

def display_active_applications():
    clear_screen()
    query = f"SELECT * FROM POSITION WHERE NOT STATUS IN ('Rejected', 'Ghosted') ORDER BY STATUS, ID ASC;"
    result = execute_query(query)
    table = Table(
        #"ID",
        Column(header="Job Title", no_wrap=True, style="cyan"),
        Column(header="Company", no_wrap=True, style="magenta"),
        Column(header="Salary", style="green"),
        "City",
        "State",
        "Job Type",
        "Applied On",
        "Application Status",
        title='Jobs I\'ve Applied To')

    for row in result:
        table.add_row(row[1], row[2], row[3], row[4], row[5], row[6], row[7].strftime('%b %d'), row[8])

    c = Console()
    c.print(table)



if __name__ == '__main__':
    ended = False
    while not ended:
        clear_screen()
        title = 'Select an option by using the arrow keys and ENTER: '
        options = ['Add an application', 'Update an application','Display active applications', 'Display all applications', 'Exit']
        option, index = pick(options, title, indicator='->')
        if index == 0:
            add_listing()
        elif index == 1:
            update_listing()
        elif index == 2:
            display_active_applications()
            input('Press ENTER to continue...')
        elif index == 3:
            display_all_listings()
            input('Press ENTER to continue...')
        elif index == 4:
            ended = True
            clear_screen()
            c = Console()
            c.print('[bold]Goodbye![/bold]')
            exit()
