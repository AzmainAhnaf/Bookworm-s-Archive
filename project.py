import json
import requests
import sys


def main():
    # Welcome Message
    print(
        "Greetings, user! Welcome to the programme. You can search for books and books related information in this programme"
    )
    print("First time users are recommended to read the README.md file to know more")
    print("Disclaimer: datas are taken from Open Library")
    while True:
        try:
            # General command available to user
            print("--------------------------------")
            print("Type 'B' to search for books")
            print("Type 'Q' to exit")
            print("--------------------------------")

            # Taking input from user
            user_input = input("Action --> ").upper().strip()

            # Comparing input and available actions
            if user_input == "Q" or user_input == "QUIT":
                sys.exit("Thanks for using the programme")
            elif user_input == "B" or user_input == "BOOK":
                book = input("Search book --> ")

                # Storing the json file in "data" variable
                data = search_book(book)

                # Searching for the availability of the book in the database
                if data == f"{book} was not found in the database":
                    print("------------------------------------------")
                    print(data)
                    continue
                print("------------------------------------------")
                print(f"\"{data["docs"][0]["title"]}\" was found")

                # Checking if book key exist and print if exist
                try:
                    print(f"Open Library key: {get_book_key(data)}")
                except KeyError:
                    print("Couldn't fetch book key")

                print("------------------------------------------")
                command_list()

                # Prompting for extra information of the book
                while True:
                    # Taking user input
                    user_input = input("Action --> ").lower().strip()

                    # Comparing user input with command list
                    if user_input == "q" or user_input == "quit":
                        break
                    elif (
                        user_input == "l"
                        or user_input == "list"
                        or user_input == "command list"
                        or user_input == "help"
                    ):
                        command_list()
                    elif user_input == "a" or user_input == "author":
                        # Fetching Author from json file
                        try:
                            names = get_authors(data)
                        except KeyError:
                            print("---------------------------------")
                            print("Couldn't find Author")
                            print("---------------------------------")
                            continue

                        # Fetching Author keys from json file
                        try:
                            keys = get_author_key(data)
                        except KeyError:
                            print("Couldn't fetch Author keys")
                            keys = ["No key found" for name in names]
                        print("---------------------------------")
                        print("Author(s): (with Open Library keys)")
                        for i in range(len(names)):
                            print(f"{names[i]} ({keys[i]})")
                        print("---------------------------------")

                    elif (
                        user_input == "r"
                        or user_input == "ratings"
                        or user_input == "rating"
                    ):
                        # fetching rating from json file
                        try:
                            ratings = get_ratings(data)
                        except KeyError:
                            print("Couldn't fetch ratings")
                            continue

                        print("---------------------------------")
                        print(f"rating: {ratings[0]}")
                        print(f"⭐⭐⭐⭐⭐ : {ratings[5]}")
                        print(f"⭐⭐⭐⭐   : {ratings[4]}")
                        print(f"⭐⭐⭐     : {ratings[3]}")
                        print(f"⭐⭐       : {ratings[2]}")
                        print(f"⭐         : {ratings[1]}")
                        print("---------------------------------")

                    elif user_input == "s" or user_input == "sentence":
                        # Fetching first sentence from json file
                        try:
                            sentence = get_first_sentence(data)
                            if len(sentence.strip()) == 0:
                                raise KeyError
                        except KeyError:
                            print("Couldn't fetch data")
                            continue
                        print("---------------------------------")
                        print(sentence)
                        print("---------------------------------")

                    elif (
                        user_input == "am"
                        or user_input == "amazon"
                        or user_input == "amazon id"
                    ):
                        # Fetching amazon ids from json file
                        try:
                            amazon_ids = get_amazon_id(data)
                        except KeyError:
                            print("Couldn't fetch amazon id")
                            continue
                        print("---------------------------------")
                        print(f"Amazon id(s):")
                        for amazon_id in amazon_ids:
                            if amazon_id == "":
                                continue
                            print(amazon_id)
                        print("---------------------------------")

                    elif (
                        user_input == "p"
                        or user_input == "place"
                        or user_input == "places"
                    ):
                        # Fetching places from json file
                        try:
                            places = get_place(data)
                        except KeyError:
                            print("Couldn't fetch place")
                            continue
                        print("________")
                        print("|Places|")
                        print("---------------------------------")
                        for i, place in enumerate(places, start=1):
                            print(i, "-", place)
                        print("---------------------------------")

                    elif (
                        user_input == "t"
                        or user_input == "time"
                        or user_input == "times"
                    ):
                        # Fetching times from json file
                        try:
                            times = get_time(data)
                        except KeyError:
                            print("Couldn't fetch time")
                            continue
                        print("_______")
                        print("|Times|")
                        print("---------------------------------")
                        for i, time in enumerate(times, start=1):
                            print(i, "-", time)
                        print("---------------------------------")

                    elif (
                        user_input == "c"
                        or user_input == "character"
                        or user_input == "characters"
                    ):
                        # Fetching characters from json file
                        try:
                            characters = get_character(data)
                        except KeyError:
                            print("Couldn't fetch characters")
                            continue
                        print("____________")
                        print("|Characters| ")
                        print("---------------------------------")
                        for i, character in enumerate(characters, start=1):
                            print(i, "-", character)
                        print("---------------------------------")

                    elif user_input == "pa" or user_input == "page" or user_input == "pages":
                        # Getting number of pages from json file
                        try:
                            page = get_page(data)
                        except KeyError:
                            print("Couldn't fetch number of pages")
                        print("---------------------------------")
                        print(f"Number of pages: {page}")
                        print("---------------------------------")

                    else:
                        print("Invalid action")

            else:
                print("Invalid action")
        except KeyError:
            print("Sorry, we were unable to find the data in the database")
            print("Forced exit to main menu")


# Getting json file of the book from Open Library api
def search_book(book):
    """
    search for specified book in openlibrary api
    """
    response = requests.get("https://openlibrary.org/search.json?q=" + book)
    data = json.loads(response.text)
    if data["numFound"] == 0:
        return f"{book} was not found in the database"
    return data


# Get author name
def get_authors(data):
    return data["docs"][0]["author_name"]


# Get Open Library keys of the Author
def get_author_key(data):
    return data["docs"][0]["author_key"]


# Get Open Library key of the book
def get_book_key(data):
    return data["docs"][0]["cover_edition_key"]


# Get Open Library Ratings
def get_ratings(data):
    ratings = data["docs"][0]
    return [
        float(str(ratings["ratings_average"])[:4]),
        ratings["ratings_count_1"],
        ratings["ratings_count_2"],
        ratings["ratings_count_3"],
        ratings["ratings_count_4"],
        ratings["ratings_count_5"],
    ]


# Get first  sentence of the book
def get_first_sentence(data):
    return data["docs"][0]["first_sentence"][0]


# Get Amazon id of the book
def get_amazon_id(data):
    return data["docs"][0]["id_amazon"]


# Get places mentioned in the books
def get_place(data):
    return data["docs"][0]["place"]


# Get the time of the incidents of the book
def get_time(data):
    return data["docs"][0]["time"]


# Get the character mentioned in the book
def get_character(data):
    return data["docs"][0]["person"]


# Get number of pages of the book
def get_page(data):
    return data["docs"][0]["number_of_pages_median"]


def command_list():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Press (A) to get Author's info                       |")
    print("Press (R) to get book's rating                       |")
    print("Press (S) to get the first sentence of the book      |")
    print("Press (PA) to get the page number of the book        |")
    print("Press (AM) to get the amazon id of the book          |")
    print("Press (P) to get the location mentioned in the book  |")
    print("Press (T) to get the time frame of the book          |")
    print("Press (C) to get the characters' name of the book    |")
    print("Press (Q) to exit to menu                            |")
    print("Press (L) for command list                           |")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


if __name__ == "__main__":
    main()
