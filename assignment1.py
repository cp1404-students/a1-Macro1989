"""
Name: Jarred Muller
Date started: 3/11/2023
GitHub URL: https://github.com/cp1404-students/a1-Macro1989
"""
import csv


def main():
    """Takes a csv song list and allows users to either display it, add songs to it or mark songs as learned.
    Users are repeatedly prompted until they choose to exit program when any alterations they have made are saved to the csv"""

    print("Song List 1.0 - by Jarred Muller")
    song_list = create_song_list("songs.csv")
    print(song_list)
    menu_choice = display_menu()
    print(menu_choice)
    while menu_choice != "Q":
        if menu_choice == "D":
            display_song(song_list)
            menu_choice = display_menu()
        elif menu_choice == "A":
            add_song(song_list)
            menu_choice = display_menu()
        if menu_choice == "C":
            complete_song(song_list)
            menu_choice = display_menu()
        if menu_choice == "Q":
            break
    save_song_list("songs.csv", song_list)
    print("Make some music!")


def create_song_list(songs_csv: str):
    """ Creates a song list from a specified csv"""
    file = open(songs_csv, "r")
    csvreader = csv.reader(file)
    song_list = []
    for row in csvreader:
        song_list.append(row)
    file.close()
    return song_list


def save_song_list(songs_csv: str, song_list):
    """ saves a song list to a specified csv"""
    file = open(songs_csv, "w", newline="")
    csvwriter = csv.writer(file)
    for song in song_list:
        csvwriter.writerow(song)
    print(f"{len(song_list)} saved to {songs_csv}")


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
    learn_count = 0
    for song in song_list:
        if song[3] == "u":
            song_learnt = "*"

        else:
            song_learnt = " "
            learn_count = learn_count + 1

        print(f"{song_list.index(song) + 1}. {song_learnt: <2} {song[0]:<30} - {song[1]:<20} ({song[2]:})")
    unlearn_count = len(song_list) - learn_count
    print(f"{learn_count} songs learned, {unlearn_count} songs still to learn.")


def add_song(song_list):
    """ prompts the user to add a new song's title artist and year"""
    song = []
    print("Please Enter the Songs Details:")
    title = input("Title:")
    while title == "":
        print("Title cannot be blank.")
        title = input("Title")
    song.append(title)

    artist = input("Artist:")
    while artist == "":
        print("Artist cannot be blank.")
        artist = input("Artist:")
    song.append(artist)

    try:
        year = int(input("Year:"))
    except ValueError:
        print("Invalid input; enter a valid number.")
        year = int(input("Year:"))
    while year < 0:
        print("Number must be > 0.")
        year = int(input("Year"))
    song.append(year)

    song.append("u")

    print(f"{song[0]} by {song[1]} ({song[2]}) added to song list.")
    song_list.append(song)


def complete_song(song_list):
    """ prompts users to select a song that is currently unlearnt and mark as learnt"""
    try:
        song_choice = int(input("Enter the number of a song to mark as learned."))
    except ValueError:
        print("Invalid input; enter a valid number.")
        song_choice = int(input("Enter the number of a song to mark as learned."))
    while song_choice < 0:
        print("Number must be > 0.")
        song_choice = int(input("Enter the number of a song to mark as learned."))
    if song_list[song_choice - 1][3] == "l":
        print(f":you have already learned {song_list[song_choice][0]}.")
    else:
        song_list[song_choice - 1][3] = "l"


if __name__ == '__main__':
    main()
