import requests


def fetch_book_details(title_or_isbn):
    base_url = "https://www.googleapis.com/books/v1/volumes"
    params = {"q": title_or_isbn}
    response = requests.get(base_url, params=params)

    if response.status_code == 200 and response.json()["totalItems"] > 0:
        book_info = response.json()["items"][0]["volumeInfo"]
        return {
            "title": book_info.get("title", "N/A"),
            "authors": ", ".join(book_info.get("authors", ["Unknown"])),
            "published_date": book_info.get("publishedDate", "N/A"),
            "isbn": next(
                (
                    identifier["identifier"]
                    for identifier in book_info.get("industryIdentifiers", [])
                    if identifier["type"] == "ISBN_13"
                ),
                "N/A",
            ),
            "publisher": book_info.get("publisher", "N/A"),
            "page_count": book_info.get("pageCount", "N/A"),
            "language": book_info.get("language", "N/A"),
            "description": book_info.get("description", "No description available."),
            "info_link": book_info.get("infoLink", "#"),
        }
    else:
        return None
