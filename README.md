# Code-Challenge-Articles---without-SQLAlchemy

## Overview

This project models the relationship between **Authors**, **Articles**, and **Magazines** using raw SQL queries within Python classes, **without using SQLAlchemy** or any ORM. The data is persisted in an SQLite database.

The domain rules:
- An Author can write many Articles.
- A Magazine can publish many Articles.
- An Article belongs to both an Author and a Magazine.
- The Author–Magazine relationship is many-to-many (via Articles).

---

## Features

- Database schema creation and setup with raw SQL.
- Python classes (`Author`, `Magazine`, `Article`) with methods to save, find, and query related data.
- Complex relationship queries using SQL joins.
- Transaction management for atomic operations.
- Simple CLI/debug script to run and test your code.
- Debugging support with `ipdb`.

---

## Project Structure

code-challenge/
├── lib/
│ ├── author.py # Author class with SQL methods
│ ├── article.py # Article class with SQL methods
│ ├── magazine.py # Magazine class with SQL methods
│ └── db/
│ ├── connection.py # DB connection setup
│ ├── init.py
├── scripts/
│ ├── setup_db.py # Create database tables
│ ├── seed.py # Seed database with sample data
├── run.py # Main script demonstrating usage
├── README.md
├── requirements.txt
└── .gitignore

yaml
Copy
Edit

---

## Getting Started

### Prerequisites

- Python 3.7+
- `pipenv` (recommended) or use a virtual environment

---

### Installation

1. Clone the repository:

```bash
git clone https://github.com/FahmyyAhmed/Code-Challenge-Articles---without-SQLAlchemy.git
cd code-challenge
Install dependencies with pipenv:

bash
Copy
Edit
pipenv install
pipenv shell
Alternatively, use python -m venv env and activate it manually, then run pip install -r requirements.txt.

- Create the database and tables:

bash
Copy
Edit
python scripts/setup_db.py
(Optional) Seed the database with sample data:

bash
Copy
Edit
python scripts/seed.py
Usage
# Run the main script to test functionality:

bash
Copy
Edit
python run.py
This script demonstrates how to create authors, magazines, articles, and query their relationships.

## Models & SQL Methods
-- Author

Create/save author

Find by id or name

List articles written

List magazines contributed to

Add new articles

-- Magazine

Create/save magazine

Find by id, name, or category

List articles published

List contributors

List contributing authors with more than 2 articles

-- Article

Create/save article

Find by id, title, author, or magazine

