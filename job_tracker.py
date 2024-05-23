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
from rich.table import Table


def add_listing(conn, cursor):
    """
    Adds a listing to the database
    """
    pass

def update_listing():
    """
    Updates an attribute of an existing listing

    - Prompts the user to input the ID of a listing
    - Shows the user the current attributes of the listing and prompts for which attribute to update
    - User inputs new attribute value and the listing in the DB is updated
    """

def display_listings():
    """
    Displays all listings in the database

    - Displays all listings in the database using rich table
    - Shows the user the number of listings in the database
    """
    pass



if __name__ == '__main__':
    # Connect to the database
    c = Console()
    try:
        conn = psycopg2.connect(host = 'localhost', dbname = 'jobs', user='postgres', password='zfechko')
        cursor = conn.cursor()
        c.print('[bold green]Connected to the database[/bold green]')
    except:
        c.print('[bold red]Failed to connect to the database[/bold red]')
        exit()