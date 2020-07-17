from texttable import Texttable
from requests import request
import json
import os
import threading
import datetime

# response = request("GET", url)
# response = json.loads(response.text)

# t = Texttable()

# t.add_row(['Location', 'Count'])
# toplocations = [ [item['_id'], item['count']] for item in response]
# t.add_rows(toplocations, False)
# print(t.draw())

usernames = "http://localhost:8000/topusernames"
passwords = "http://localhost:8000/toppasswords"
combinations = "http://localhost:8000/topcombinations"
locations = "http://localhost:8000/toplocations"


def draw_location_table(url):
    response = request("GET", url)
    response = json.loads(response.text)

    t = Texttable()
    rows = [['Location', 'Count']]

    [rows.append([item['_id'], item['count']]) for item in response]
    t.add_rows(rows)

    print('\nTop Locations')
    print(t.draw())

def draw_username_table(url):
    response = request("GET", url)
    response = json.loads(response.text)

    t = Texttable()
    rows = [['Username', 'Count']]

    [rows.append([item['_id'], item['count']]) for item in response]
    t.add_rows(rows)

    print('\nTop Usernames')
    print(t.draw())


def draw_password_table(url):
    response = request("GET", url)
    response = json.loads(response.text)

    t = Texttable()
    rows = [['Password', 'Count']]

    [rows.append([item['_id'], item['count']]) for item in response]
    t.add_rows(rows)

    print('\nTop Passwords')
    print(t.draw())


def draw_combination_table(url):
    response = request("GET", url)
    response = json.loads(response.text)

    t = Texttable()
    rows = [['Username', 'Password', 'Count']]

    [rows.append([item['_id']['username'], item['_id']['pass'], item['count']]) for item in response]
    t.add_rows(rows)

    print('\nTop Combinations')
    print(t.draw())


def draw_tables(interval=5):
    os.system('clear')

    print(datetime.datetime.now())
    print('Updating every {} seconds'.format(interval))

    draw_username_table(usernames)
    draw_password_table(passwords)
    draw_combination_table(combinations)
    draw_location_table(locations)

    threading.Timer(interval, draw_tables).start()



if __name__ == "__main__":
    draw_tables()