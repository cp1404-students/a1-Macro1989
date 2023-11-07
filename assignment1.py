"""
Name: Jarred Muller
Date started: 3/11/2023
GitHub URL: https://github.com/cp1404-students/a1-Macro1989
"""
import csv


def main():
    """..."""
    print("Song List 1.0 - by Jarred Muller")
    song_list = create_song_list("songs.csv")
    print(song_list)
    menu_choice = display_menu()
    print(menu_choice)
    while menu_choice != "Q":
        if menu_choice == "D":
            display_song(song_list)
        elif menu_choice == "A":
            add_song(song_list)
        if menu_choice == "C":
            complete_song(song_list)
        if menu_choice == "Q":
            return



def create_song_list(songs_csv: str):
    file = open(songs_csv)
    csvreader = csv.reader(file)
    song_list = []
    for row in csvreader:
        song_list.append(row)
    file.close()
    return song_list

    """ Creates a song list from a specified csv"""


def display_menu():
    """Displays a list of choices the users can make and returns their choice"""
    menu_choice = ""
    while menu_choice != "D" and menu_choice != "A" and menu_choice != "C" and menu_choice != "Q":
        print("""Menu:
        D - Display songs
        A - Add new song
        C - Complete a song
        Q - Quit""")
        menu_choice = input().upper()
        if menu_choice != "D" and menu_choice != "A" and menu_choice != "C" and menu_choice != "Q":
            print("invalid choice")
    return menu_choice


def display_song(song_list):
    """ Display a list of all the songs with details and a count of these songs, unlearned songs will have an *"""


def add_song(song_list):
    """ prompts the user to add a song's title artist and year"""


def complete_song(song_list):
    """ prompts the user to add a song's title artist and year"""


if __name__ == '__main__':
    main()
