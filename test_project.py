from project import *
import pytest


LOTR = json.loads(requests.get("https://openlibrary.org/search.json?q=lord of the rings").text)
WIMPY_KID = json.loads(requests.get("https://openlibrary.org/search.json?q=diary of a wimpy kid").text)
COFFEE = json.loads(requests.get("https://openlibrary.org/search.json?q=before the coffee gets cold").text)
INVALID = json.loads(requests.get("https://openlibrary.org/search.json?q=mokhleser kahini").text)


def test_search_book():
    assert search_book("lord of the rings") == LOTR
    assert search_book("diary of a wimpy kid") == WIMPY_KID
    assert search_book("before the coffee gets cold") == COFFEE
    assert search_book("mokhleser kahini") == "mokhleser kahini was not found in the database"


def test_get_authors():
    assert get_authors(LOTR) == ["J.R.R. Tolkien"]
    assert get_authors(WIMPY_KID) == ["Jeff Kinney"]
    assert get_authors(COFFEE) == ["Toshikazu Kawaguchi"]
    with pytest.raises(IndexError):
        assert get_authors(INVALID)


def test_get_book_key():
    assert get_book_key(LOTR) == "OL21058613M"
    assert get_book_key(WIMPY_KID) == "OL36660032M"
    assert get_book_key(COFFEE) == "OL28203220M"
    with pytest.raises(IndexError):
        assert get_book_key(INVALID)


def test_get_ratings():
    assert get_ratings(LOTR) == [4.54, 2, 2, 6, 7, 55]
    assert get_ratings(WIMPY_KID) == [4.19, 21, 10, 30, 46, 167]
    assert get_ratings(COFFEE) == [3.88, 3, 1, 6, 11, 13]
    with pytest.raises(IndexError):
        assert get_ratings(INVALID)


def test_get_page():
    assert get_page(LOTR) == 1193
    assert get_page(WIMPY_KID) == 221
    assert get_page(COFFEE) == 239
    with pytest.raises(IndexError):
        assert get_page(INVALID)
