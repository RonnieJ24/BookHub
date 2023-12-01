from flask import Flask, render_template, request, redirect, url_for, flash
from db_manager import DBManager
from api_handler import fetch_book_details

app = Flask(__name__)
app.secret_key = (
    "my_secret_key"  # We can replace this with a real secret key for production
)

db_manager = DBManager()


@app.route("/books")
def books():
    sort_by = request.args.get(
        "sort_by", "title"
    )  # 'sort_by' determines the attribute to sort the books by, defaulting to 'title'.
    order = request.args.get(
        "order", "asc"
    )  # 'order' specifies the sorting order, either 'asc' for ascending or 'desc' for descending.
    filter_by = request.args.get(
        "filter", None
    )  # 'filter_by' applies a filter to the book attributes if provided.
    books = db_manager.get_books_sorted_filtered(
        sort_by, order, filter_by
    )  # The 'get_books_sorted_filtered' method in 'db_manager' will handle the query construction.
    return render_template("index.html", books=books)


@app.route("/")
def index():  # Route to display the home page with the book catalog. Includes sorting functionality.
    books = db_manager.get_all_books()
    return render_template("index.html", books=books)


@app.route("/book/<int:book_id>")
def book_detail(book_id):
    book = db_manager.get_book_by_id(book_id)
    if book:
        return render_template("book_detail.html", book=book)
    else:
        flash(f"No book found with ID: {book_id}")
        return redirect(url_for("index"))


@app.route("/add", methods=["POST"])
def add_book():
    title_or_isbn = request.form["title_or_isbn"]
    book_data = fetch_book_details(title_or_isbn)
    if book_data:
        db_manager.add_book(book_data)
        flash(f"Added book: {book_data['title']}")
    else:
        flash("Failed to add book.")
    return redirect(url_for("index"))


@app.route("/update/<int:book_id>", methods=["GET", "POST"])
def update_book(book_id):
    if request.method == "POST":
        title_or_isbn = request.form["title_or_isbn"]
        book_data = fetch_book_details(title_or_isbn)
        if book_data:
            db_manager.update_book(book_id, book_data)
            flash(f"Updated book: {book_data['title']}")
            return redirect(url_for("index"))
        else:
            flash("Failed to update book.")

    book = db_manager.get_book_by_id(book_id)
    if book:
        return render_template("update_book.html", book=book)
    else:
        flash(f"No book found with ID: {book_id}")
        return redirect(url_for("index"))


@app.route("/delete/<int:book_id>")
def delete_book(book_id):
    db_manager.delete_book(book_id)
    flash(f"Deleted book with ID: {book_id}")
    return redirect(url_for("index"))


@app.route("/search")
def search():
    query = request.args.get("query")
    if query:
        books = db_manager.search_books(query)
        return render_template("index.html", books=books)
    return redirect(url_for("index"))


@app.route("/reports")
def reports():
    report_data = db_manager.generate_report()
    return render_template("reports.html", report_data=report_data)


if __name__ == "__main__":
    app.run(debug=True)
