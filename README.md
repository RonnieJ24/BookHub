# BookHub

**BookHub** is a web application crafted with Flask, designed to empower book lovers to manage their personal library collections. Leveraging the Google Books API, BookHub provides a robust platform for users to search, add, update, and manage book entries with ease.

## Features

- **Book Detail Retrieval**: Seamlessly fetch and display book details using the Google Books API.
- **User Data Management**: A user-friendly interface for adding, updating, and deleting book entries.
- **Data Sorting and Filtering**: Organize books in the collection using a variety of criteria.
- **Report Generation**: Generate insightful reports to analyze the book collection.

## Getting Started

Follow these instructions to get a local copy of BookHub up and running on your machine.

### Prerequisites

- Python
- pip (comes with Python)
- MySQL

### Installation

1. Clone the repository: git clone https://github.com/RonnieJ24/BookHub.git
3. Navigate to the project directory and install dependencies: pip install -r requirements.txt
5. Configure the MySQL database (instructions below).
6. Run the Flask application: flask run
7. Access BookHub in your web browser at `localhost:5000`.

## MySQL Configuration

BookHub uses MySQL to store and retrieve book data. Follow these steps for configuration:

1. Create a new MySQL database named `bookhub3`.
2. Use the schema file from the repository to set up the `books` table with the necessary columns.
3. Create a MySQL user with appropriate permissions for the `bookhub3` database.
4. Update `db_manager.py` with your MySQL server and user details.

## Roadmap

Explore the [issues](https://github.com/RonnieJ24/BookHub/issues) for proposed features and known bugs.

## Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License

Distributed under the MIT License. See `LICENSE` in the repository for more information.

## Contact

Rani - [rani_yaqoob@icloud.com](mailto:rani_yaqoob@icloud.com)

Project Link: [https://github.com/RonnieJ24/BookHub](https://github.com/RonnieJ24/BookHub)

## Acknowledgements

- [Google Books API](https://developers.google.com/books)
- [Flask](https://flask.palletsprojects.com/)
- [Bootstrap](https://getbootstrap.com/)
- [jQuery](https://jquery.com/)
- And a nod to all the bibliophiles out there who inspire us to build better book management systems!
