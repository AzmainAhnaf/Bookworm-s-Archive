# Bookeworm's Archive
## Video Demo: https://youtu.be/TETFT8vkmv8
## Description:
This programme is used for searching books and book related information, you can extract the following type of information from a book:<br><br>
    &nbsp; &nbsp; &nbsp; &nbsp; 1 - Author's Information<br>
    &nbsp; &nbsp; &nbsp; &nbsp; 2 - Rating of Open Library<br>
    &nbsp; &nbsp; &nbsp; &nbsp; 3 - First Sentence of the Book<br>
    &nbsp; &nbsp; &nbsp; &nbsp; 4 - Page Numbers of the Book<br>
    &nbsp; &nbsp; &nbsp; &nbsp; 5 - Amazon ID of the Book<br>
    &nbsp; &nbsp; &nbsp; &nbsp; 6 - Places Mentioned in the Book<br>
    &nbsp; &nbsp; &nbsp; &nbsp; 7 - Timeframe of the Book<br>
    &nbsp; &nbsp; &nbsp; &nbsp; 8 - Characters of the Book<br><br>
The keys used in the applications are Open Library keys, you can use this keys to search the author or book up in Open Library.

## Programme Explaination:
All the functions are in project.py file. imported libraries: requests, json, sys.
### main():
this functions contains the main application that checks for input and give output according to it.<br>
The whole function is wrapped with a try except (KeyError) block to prevent from any unwanted exitation of programme.<br>
The programme is case insenstive toward user input.

### search_book():
This functions takes a input book as the argument and search for the book in Open Library API.<br>
returns the json file if the book is found else return a string that says that the book was not found

### get_x(): [x = authors, author_key, book_key, ratings, first_sentence, amazon_id, place, time, character]:
takes a data parameter which is a json file, extract the information and returns them to the programmer.

### command_list():
takes nothing as argument, prints the command list. Made it a function because it had to be used two times in the main programme. Returns None.

### test_project.py:
The programme has been thoroughly unit tested on test_project.py file
