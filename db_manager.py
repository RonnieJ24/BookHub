import mysql.connector
from mysql.connector import Error


class DBManager:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Study2023$",
                database="bookhub3",
            )
        except Error as e:
            print(f"Error connecting to MySQL Database: {e}")
            self.conn = None

    def execute_query(self, query, values=None):
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(query, values)
            if query.lstrip().upper().startswith("SELECT"):
                result = cursor.fetchall()
                cursor.close()
                return result
            else:
                self.conn.commit()
                cursor.close()
        except Error as e:
            print(f"Error executing query: {e}")

    def add_book(self, book_data):
        query = """INSERT INTO books (title, authors, published_date, isbn, description, info_link, 
                   publisher, language, page_count, format) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (
            book_data["title"],
            book_data["authors"],
            book_data["published_date"],
            book_data["isbn"],
            book_data["description"],
            book_data["info_link"],
            book_data["publisher"],
            book_data["language"],
            book_data["page_count"],
            book_data.get("format", "Paperback"),
        )
        self.execute_query(query, values)

    def get_all_books(self):
        return self.execute_query("SELECT id, title, authors FROM books")

    def get_book_by_id(self, book_id):
        cursor = self.conn.cursor(dictionary=True)  # Make sure to use dictionary cursor
        cursor.execute("SELECT * FROM books WHERE id = %s", (book_id,))
        book = cursor.fetchone()
        cursor.close()  # Don't forget to close the cursor
        return book if book else None

    def update_book(self, book_id, book_data):
        query = """UPDATE books SET title = %s, authors = %s, published_date = %s, isbn = %s,
                   description = %s, info_link = %s, publisher = %s, language = %s,
                   page_count = %s, format = %s WHERE id = %s"""
        values = (
            book_data["title"],
            book_data["authors"],
            book_data["published_date"],
            book_data["isbn"],
            book_data["description"],
            book_data["info_link"],
            book_data["publisher"],
            book_data["language"],
            book_data["page_count"],
            book_data.get("format", "Paperback"),
            book_id,
        )
        self.execute_query(query, values)

    def delete_book(self, book_id):
        self.execute_query("DELETE FROM books WHERE id = %s", (book_id,))

    def __del__(self):
        if self.conn:
            self.conn.close()

    def get_books_sorted_filtered(self, sort_by="title", order="asc", filter_by=None):
        # Ensure the sort_by and order parameters are safe to use in a query
        # For a production system, you'd want a safer way to handle dynamic queries to avoid SQL injection
        query = "SELECT * FROM books"
        filter_values = []
        if filter_by:
            query += " WHERE title LIKE %s OR authors LIKE %s OR published_date LIKE %s"
            filter_values.append(f"%{filter_by}%")
            filter_values.append(f"%{filter_by}%")
            filter_values.append(f"%{filter_by}%")
        query += f" ORDER BY {sort_by} {order}"
        return self.execute_query(query, filter_values)

    def search_books(self, query):
        search_query = "%" + query + "%"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM books WHERE title LIKE %s OR authors LIKE %s",
            (search_query, search_query),
        )
        result = cursor.fetchall()
        cursor.close()
        return result

    def generate_report(self):
        query = "SELECT authors, COUNT(*) as total FROM books GROUP BY authors"
        return self.execute_query(query)
